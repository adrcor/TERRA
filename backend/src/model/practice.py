from client import client
from model import Geo

class PracticeProgress:
    
    @staticmethod
    def get_progress(id_user: str, region: str) -> int:
        response = client.table('practice_progress').select('*').match({'id_user': id_user, 'region': region}).execute()
        if not response.data:
            return PracticeProgress.init_progress(id_user, region)
        return response.data[0]['progress']
    
    @staticmethod
    def init_progress(id_user: str, region: str):
        response = client.table('practice_progress').insert({'id_user': id_user, 'region': region, 'progress': 5}).execute()
        return response.data[0]['progress']


class PracticeGrade:

    @staticmethod
    def init_grades(id_user: str, region: str):
        countries = [dic['country'] for dic in Geo.get_by_region(region)]
        response = client.table('practice_grade').upsert({
            'id_user': id_user,
            region: {country: {'count': 0, 'reaction': 0, 'typing': 0, 'score': 0} for country in countries}
            }).execute()
        return response.data[0][region]
    
    @staticmethod
    def set_grades(id_user: str, region: str, grades: dict):
        response = client.table('practice_grade').upsert({
            'id_user': id_user,
            region: grades
            }).execute()
        return response.data[0][region]

    @staticmethod
    def get_grades(id_user: str, region: str):
        response = client.table('practice_grade').select(region).execute()
        if not response.data or not response.data[0][region]:
            return PracticeGrade.init_grades(id_user, region)
        return response.data[0][region]
    
    
    @staticmethod
    def get_data(id_user: str, region: str):

        data = Geo.get_by_region(region)
        progress = PracticeProgress.get_progress(id_user, region)
        grades = PracticeGrade.get_grades(id_user, region)

        for index, obj in enumerate(data):
            obj['grades'] = grades[obj['country']]
            obj['unlocked'] = index < progress

        return data
    
    @staticmethod
    def update_grades(id_user: str, region: str, data: list[dict]):
        # data = [{'country': 'France', 'reaction': 823, 'typing': 300}]
        grades = PracticeGrade.get_grades(id_user, region)

        for entry in data:
            current_rating = grades[entry['country']]
            grades[entry['country']] = PracticeGrade.get_new_grades(current_rating, entry)
            
        PracticeGrade.set_grades(id_user, region, grades)
        return PracticeGrade.get_data(id_user, region)
    
    @staticmethod
    def get_new_grades(current_rating: dict, entry: dict):
        if current_rating['count'] == 0:
            return {
                'count': 1,
                'typing': entry['typing'],
                'reaction': entry['reaction'],
                'score': int(PracticeGrade.calculate_score(entry['reaction'], entry['typing']) / 5)
                }

        if current_rating['count'] < 10:
            count = current_rating['count'] + 1
            typing = int((current_rating['typing'] * current_rating['count'] + entry['typing']) / count)
            reaction = int((current_rating['reaction'] * current_rating['count'] + entry['reaction']) / count)
            score = int(PracticeGrade.calculate_score(reaction, typing) * min(count, 5) / 5)
            return {'count': count, 'typing': typing, 'reaction': reaction, 'score': score}
        
        else:
            count = current_rating['count'] + 1
            typing = int((current_rating['typing'] * 9 + entry['typing']) / 10)
            reaction = int((current_rating['reaction'] * 9 + entry['reaction']) / 10)
            score = PracticeGrade.calculate_score(reaction, typing)
            return {'count': count, 'typing': typing, 'reaction': reaction, 'score': score}


    @staticmethod
    def calculate_score(reaction: int, typing: int):
        reaction = min(max(reaction, 500), 2500) #  clip reaction within [500:2500]
        typing = min(typing, 500) # clip typing within [0:500]
        score_reaction = - reaction / 2000 * 60 + 75
        score_typing = typing / 500
        return min(score_reaction + score_typing, 100)