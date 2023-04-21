from flask import Blueprint, request
from model import Progress, Grades, Practice
from flask_jwt_extended import jwt_required, get_jwt_identity
import time
import asyncio

PracticeBlueprint = Blueprint('PracticeBlueprint', __name__)


@PracticeBlueprint.route('/data/<region>', methods=['GET'])
@jwt_required()
def data(region: str):
    t1 = time.perf_counter()
    id_user = get_jwt_identity()
    data = Practice.get_data(id_user, region)
    t2 = time.perf_counter()
    print('TOTAL DATA TIME: ', t2 - t1)
    return [obj.to_dict() for obj in data]

@PracticeBlueprint.route('/update/<region>', methods=['POST'])
@jwt_required()
def update(region: str):
    t1 = time.perf_counter()
    id_user = get_jwt_identity()
    if not request.json:
        return 'unvalid paramters'
    params = request.json.get('params')
    data = Practice.update(id_user, region, params)
    t2 = time.perf_counter()
    print('TOTAL UPDATE TIME: ', t2 - t1)
    return [obj.to_dict() for obj in data]

@PracticeBlueprint.route('/delete', methods=['DELETE'])
@jwt_required()
def delete_all():
    id_user = get_jwt_identity()
    Progress.delete_all(id_user)
    Practice.delete_all(id_user)
    return 'practice data deleted'