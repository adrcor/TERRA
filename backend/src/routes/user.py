from flask import Blueprint, abort, request
from flask_jwt_extended import jwt_required, get_jwt_identity
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
@jwt_required()
def set_user():
    if request.json is None:
        abort(400, 'Unvalid parameters')

    id_user: str = get_jwt_identity()
    username: str = request.json.get('username')
    print(id_user, type(id_user))
    print(username, type(username))

    response = client.table('user_data').insert({'id_user': id_user, 'username': username, 'username_lower': username.lower()}).execute()
    return {'data': response.data}

@UserBlueprint.route('/get-username', methods=['GET'])
@jwt_required()
def get_username():
    id_user: str = get_jwt_identity()
    response = client.table('user_data').select('username').eq('id_user', id_user).execute()
    if len(response.data):
        username = response.data[0]['username']
        return {'username': username}
    else:
        return {'username': None}