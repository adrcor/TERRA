from flask import Blueprint, request
from model import PracticeProgress, PracticeGrade
from flask_jwt_extended import jwt_required, get_jwt_identity

PracticeBlueprint = Blueprint('PracticeBlueprint', __name__)

@PracticeBlueprint.route('/progress/<region>', methods=['GET'])
@jwt_required()
def current_progress(region: str):
    id_user = get_jwt_identity()
    data = PracticeProgress.get_progress(id_user, region)
    return data

@PracticeBlueprint.route('/data/<region>', methods=['GET'])
@jwt_required()
def data(region: str):
    id_user = get_jwt_identity()
    data = PracticeGrade.get_data(id_user, region)
    return data

@PracticeBlueprint.route('/update/<region>', methods=['POST'])
@jwt_required()
def update(region: str):
    id_user = get_jwt_identity()
    if not request.json:
        return 'unvalid paramters'
    params = request.json.get('params')
    print(params)
    data = PracticeGrade.update_grades(id_user, region, params)
    return data
