from flask import Blueprint, abort, request
from client import client
import re

UserBlueprint = Blueprint('UserBlueprint', __name__)

@UserBlueprint.route('/verify/<username>', methods=['GET'])
def verify_username(username):

    if len(username) < 4 or len(username) > 16:
        return {'valid': False, 'message': 'Username must be between 4 and 16 characters'}
    
    if not bool(re.fullmatch(r'^[a-zA-Z0-9_-]+$', username)):
        return {'valid': False, 'message': "Username can only contains letters, digits, '_' and '-'"}
    
    response = client.table('user_data').select('*').eq('username_lower', username.lower()).execute()
    if len(response.data):
        return {'valid': False, 'message': 'Username is already taken'}
    
    return {'valid': True, 'message': 'Username is valid'}


@UserBlueprint.route('/set', methods=['POST'])
def set_user():
    if request.json is None:
        abort(400, 'Unvalid parameters')

    id_user: int = request.json.get('id')
    username: str = request.json.get('username')
    print(id_user, type(id_user))
    print(username, type(username))

    response = client.table('user_data').insert({'id': id_user, 'username': username, 'username_lower': username.lower()}).execute()
    return {'data': response.data}