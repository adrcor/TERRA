from dataclasses import dataclass
from model.geo import Geo
from model.grades import Grades
from model.progress import Progress
import asyncio

@dataclass
class Practice:
    geo: Geo
    grades: Grades
    unlocked: bool

    def to_dict(self):
        return {**self.geo.to_dict(), 'unlocked': self.unlocked, 'grades': self.grades.to_dict()}
    
    @staticmethod
    def get_data(id_user: str, region: str) -> list['Practice']:
        return asyncio.run(Practice.get_data_async(id_user, region))
    
    @staticmethod
    async def get_data_async(id_user: str, region: str) -> list['Practice']:
        loop = asyncio.get_event_loop()

        task_geos = loop.run_in_executor(None, Geo.get_by_region, region)
        task_progress = loop.run_in_executor(None, Progress.get, id_user, region)
        task_grades = loop.run_in_executor(None, Grades.get_grades, id_user, region)

        progress, grades = await asyncio.gather(task_progress, task_grades)

        if progress == Grades.get_progress_from_grades(grades):
            progress = Progress.update(id_user, region, progress + 3)

        geos = await task_geos

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