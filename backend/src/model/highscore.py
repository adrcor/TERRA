from client import client
from model import Test
from dataclasses import dataclass

@dataclass
class Highscore:

    @staticmethod
    def get_all_from(id_user: str) -> list[Test]:
        # Get all highscores tests for a single user
        response = client.table('highscore').select('id_test').eq('id_user', id_user).execute()
        return [Test.get(data['id_test']) for data in response.data]

    @staticmethod
    def get(id_user: str, region: str, length: int) -> Test | None:
        # Get highscore test for the given parameters
        match_data = {'id_user': id_user, 'region': region, 'length': length}
        response = client.table('highscore').select('test(*)').match(match_data).execute()
        return Test(**response.data[0]['test']) if response.data else None

    @staticmethod
    def add(test: Test) -> None:
        data = {'id_user': test.id_user, 'region': test.region, 'length': test.length, 'id_test': test.id}
        client.table('highscore').upsert(data).execute()
        
    @staticmethod
    def delete_all(id_user):
        response = client.table('highscore').delete().eq('id_user', id_user).execute()
        return len(response.data)