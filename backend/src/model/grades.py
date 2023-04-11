from dataclasses import dataclass, asdict
from model.geo import Geo
from client import client


@dataclass
class Grades:
    count: int = 0
    reaction: int = 0 # in ms
    typing: int = 0 # in char per sec
    score: int = 0

    def to_dict(self):
        return asdict(self)

    def update(self, entry: dict):
        if entry['valid']:
            reaction = min(entry['reaction'], 10000)
            typing = entry['typing']
        else:
            reaction = 10000
            typing = 0

        if self.count == 0:
            self.count = 1
            self.typing = typing
            self.reaction = reaction
            self.update_score()

        elif self.count < 10:
            self.typing = int((self.typing * self.count + typing) / (self.count + 1))
            self.reaction = int((self.reaction * self.count + reaction) / (self.count + 1))
            self.count += 1
            self.update_score()
        
        else:
            typing = int((self.typing * 9 + typing) / 10)
            reaction = int((reaction * 9 + reaction) / 10)
            self.count += 1
            self.update_score()

    def update_score(self):
        score_reaction = self.get_reaction_score()
        score_typing = self.get_typing_score()
        score = min(score_reaction + score_typing, 100) * min(self.count / 5, 1)
        self.score = int(score)

    def get_reaction_score(self):
        reaction = min(max(self.reaction, 600), 4000)
        if reaction >= 2000:
            return int(-reaction / 80 + 50)
        if reaction >= 700:
            return int(-reaction / 52 + 63.46)
        else:
            return int(-reaction / 20 + 85)

    def get_typing_score(self):
        typing = min(self.typing, 750)
        if typing <= 150:
            return int(typing / 6)
        if typing <= 500:
            return int(typing / 14 + 14.29)
        else:
            return int(typing / 50 + 40)
    
    
    @staticmethod
    def init_grades(id_user: str, region: str) -> dict[str, 'Grades']:
        countries = [dic.country for dic in Geo.get_by_region(region)]
        response = client.table('practice_grade').upsert({
            'id_user': id_user,
            region: {country: Grades().to_dict() for country in countries}
            }).execute()
        return {key: Grades(**grades) for key, grades in response.data[0][region].items()}

    @staticmethod
    def get_grades(id_user: str, region: str) -> dict[str, 'Grades']:
        response = client.table('practice_grade').select(region).execute()
        if not response.data or not response.data[0][region]:
            return Grades.init_grades(id_user, region)
        return {key: Grades(**grades) for key, grades in response.data[0][region].items()}
    
    @staticmethod
    def set_grades(id_user: str, region: str, grades: dict[str, 'Grades']) -> dict[str, 'Grades']:
        response = client.table('practice_grade').upsert({
            'id_user': id_user,
            region: {key: g.to_dict() for key, g in grades.items()}
            }).execute()
        return {key: Grades(**grades) for key, grades in response.data[0][region].items()}
    
    @staticmethod
    def get_progress_from_grades(grades: dict[str, 'Grades']) -> int:
        scores = [grade.score for grade in grades.values() if grade.score >= 50]
        if len(scores) == len(grades):
            return -1
        return len(scores)
        
    @staticmethod
    def delete_all(id_user):
        response = client.table('practice_grade').delete().eq('id_user', id_user).execute()
        