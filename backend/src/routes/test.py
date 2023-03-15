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
    test: Test = Test.new(id_user, **data).add() # type: ignore
    if test.is_new_highscore():
        Highscore.add(test)
    return test.as_dict()
