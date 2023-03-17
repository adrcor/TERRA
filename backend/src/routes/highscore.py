from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity


from model import Highscore, Test

HighscoreBlueprint = Blueprint('HighscoreBlueprint', __name__)

@HighscoreBlueprint.route('/get/<region>/<int:length>', methods=['GET'])
@jwt_required()
def get(region: str, length: int):
    id_user = get_jwt_identity()
    test = Highscore.get(id_user, region, length)
    return test.as_dict() if test else 'No highscore'
