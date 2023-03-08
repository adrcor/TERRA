from client import client

class Geo:
    @staticmethod
    def get_all() -> list[dict[str, str]]:
        response = client.table('geo').select('country', 'capital', 'region').execute()
        return response.data
    