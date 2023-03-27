from client import client

class Geo:
    @staticmethod
    def get_all() -> list[dict[str, str]]:
        response = client.table('geo').select('country', 'capital', 'region').execute()
        return response.data
    
    @staticmethod
    def get_by_region(region: str, limit: int | None = None):
        query = client.table('geo').select('country', 'capital', 'code', 'region').eq('region', region.upper()).order('code')
        if limit:
            query.limit(limit)
        response = query.execute()
        return response.data