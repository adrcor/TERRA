from client import client
from dataclasses import asdict, dataclass

@dataclass
class Geo:
    country: str
    capital: str
    region: str
    code: str | None = None

    @staticmethod
    def get_all() -> list['Geo']:
        response = client.table('geo').select('country', 'capital', 'region').execute()
        return [Geo(**obj) for obj in response.data]
    
    @staticmethod
    def get_by_region(region: str) -> list['Geo']:
        response = client.table('geo').select('country', 'capital', 'code', 'region').eq('region', region.upper()).order('code').execute()
        return [Geo(**obj) for obj in response.data]
    
    def to_dict(self) -> dict[str, str]:
        if self.code:
            return asdict(self)
        else:
            return {'country': self.country, 'capital': self.capital, 'region': self.region}