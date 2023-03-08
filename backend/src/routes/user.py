from flask import Blueprint, abort, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from client import client
import re
from model import User

UserBlueprint = Blueprint('UserBlueprint', __name__)

@UserBlueprint.route('/verify/<username>', methods=['GET'])
def verify_username(username):

    if not User.verify_length(username):
        return {'valid': False, 'message': 'Username must be between 4 and 16 characters'}
    
    if not User.verify_chars(username):
        return {'valid': False, 'message': "Username can only contains letters, digits, '_' and '-'"}
    
    if not User.verify_available(username):
        return {'valid': False, 'message': 'Username is already taken'}
    
    return {'valid': True, 'message': 'Username is valid'}


@UserBlueprint.route('/set', methods=['POST'])
@jwt_required()
def set_user():
    if request.json is None:
        abort(400, 'Unvalid parameters')

    id_user: str = get_jwt_identity()
    username: str = request.json.get('username')

    user = User.new(id_user, username)
    new_user = user.add()

    return {'new_user': new_user.as_dict() if new_user else None}

@UserBlueprint.route('/get-username', methods=['GET'])
@jwt_required()
def get_username():
    id_user: str = get_jwt_identity()
    user = User.get(id_user)
    return {'username': user.username if user else None}