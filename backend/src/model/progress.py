from client import client

class Progress:
    
    @staticmethod
    def get(id_user: str, region: str) -> int:
        response = client.table('practice_progress').select('*').match({'id_user': id_user, 'region': region}).execute()
        if not response.data:
            return Progress.init(id_user, region)
        return response.data[0]['progress']
    
    @staticmethod
    def init(id_user: str, region: str) -> int:
        response = client.table('practice_progress').insert({'id_user': id_user, 'region': region, 'progress': 5}).execute()
        return response.data[0]['progress']
    
    @staticmethod
    def update(id_user: str, region: str, value: int) -> int:
        response = client.table('practice_progress').update({'progress': value}).match({'id_user': id_user, 'region': region}).execute()
        return response.data[0]['progress']

    @staticmethod
    def delete_all(id_user):
        response = client.table('practice_progress').delete().eq('id_user', id_user).execute()
