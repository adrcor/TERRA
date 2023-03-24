from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity


from model import Highscore, Test

TestBlueprint = Blueprint('TestBlueprint', __name__)

@TestBlueprint.route('/add', methods=['POST'])
@jwt_required()
def add_test():
    # Log new test and update highscore if needed
    id_user = get_jwt_identity()
    data = request.json
    print(data)
    test: Test = Test.new(id_user, **data['result'], **data['param']).add() # type: ignore
    if test.is_new_highscore():
        Highscore.add(test)
    return test.as_dict()

@TestBlueprint.route('/get/region=<region>&length=<length>', methods=['GET'])
@jwt_required()
def get_test(region: str, length: int):
    print(region, length)
    id_user = get_jwt_identity()
    tests = Test.get_tests(id_user, region, length)
    return [test.as_dict() for test in tests]