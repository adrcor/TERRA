from flask import Blueprint, request
from model import PracticeProgress, PracticeGrade
from flask_jwt_extended import jwt_required, get_jwt_identity
import time

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
    t1 = time.perf_counter()
    id_user = get_jwt_identity()
    if not request.json:
        return 'unvalid paramters'
    params = request.json.get('params')
    t2 = time.perf_counter()
    data = PracticeGrade.update_grades(id_user, region, params)
    t3 = time.perf_counter()
    print('\nupdate = ', t3 - t1)
    print('--params = ', t2 - t1)
    print('--update_grades = ', t3 - t2)
    return data

@PracticeBlueprint.route('/delete', methods=['DELETE'])
@jwt_required()
def delete_all():
    id_user = get_jwt_identity()
    PracticeProgress.delete_all(id_user)
    PracticeGrade.delete_all(id_user)
    return 'practice data deleted'