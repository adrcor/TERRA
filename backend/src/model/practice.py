from dataclasses import dataclass
from model.geo import Geo
from model.grades import Grades
from model.progress import Progress

@dataclass
class Practice:
    geo: Geo
    grades: Grades
    unlocked: bool

    def to_dict(self):
        return {**self.geo.to_dict(), 'unlocked': self.unlocked, 'grades': self.grades.to_dict()}
    
    @staticmethod
    def get_data(id_user: str, region: str) -> list['Practice']:

        geos = Geo.get_by_region(region)
        progress = Progress.get(id_user, region)
        grades = Grades.get_grades(id_user, region)

        if progress == Grades.get_progress_from_grades(grades):
            progress = Progress.update(id_user, region, progress + 3)

        data: list[Practice] = []
        for index, geo in enumerate(geos):
            data.append(Practice(geo, grades[geo.country], index < progress))

        return data
    
    @staticmethod
    def update(id_user: str, region: str, data: list[dict]) -> list['Practice']:
        grades = Grades.get_grades(id_user, region)
        for entry in data:
            grades[entry['country']].update(entry)
        Grades.set_grades(id_user, region, grades)
        return Practice.get_data(id_user, region)
    

    @staticmethod
    def delete_all(id_user):
        Progress.delete_all(id_user)
        Grades.delete_all(id_user)