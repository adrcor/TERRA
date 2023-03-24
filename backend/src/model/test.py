from __future__ import annotations
from dataclasses import dataclass, asdict
from client import client
import model

@dataclass
class Test:
    id: int | None
    id_user: str
    timestamp: str | None
    region: str
    length: int
    score: int
    time: int
    speed: int

    @staticmethod
    def new(id_user: str, region: str, length: int, score: int, time: int, speed: int) -> Test:
        return Test(id=None, id_user=id_user, timestamp=None, region=region, length=length, score=score, time=time, speed=speed)
    
    def add(self) -> Test | None:
        data = {'id_user': self.id_user, 'region': self.region, 'length': self.length,
                'score': self.score, 'time': self.time, 'speed': self.speed}
        response = client.table('test').insert(data).execute()
        if response.data:
            return Test(**response.data[0])

    @staticmethod
    def get(id: int) -> Test:
        response = client.table('test').select('*').eq('id', id).execute()
        return Test(**response.data[0])
    
    def as_dict(self) -> dict:
        return asdict(self)
    
    def is_better_than(self, test: Test) -> bool:
        return self.speed > test.speed

    def is_new_highscore(self) -> bool:
        test = model.Highscore.get(self.id_user, self.region, self.length)
        if test is None:
            return True
        return self.is_better_than(test)

    @staticmethod
    def get_tests(id_user: str, region: str, length: int):
        data = {'id_user': id_user, 'region': region, 'length': length}
        response = client.table('test').select('*').match(data).order('id').execute()
        return [Test(**item) for item in response.data]