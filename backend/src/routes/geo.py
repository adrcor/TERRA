from flask import Blueprint, abort, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from client import client
import re

GeoBlueprint = Blueprint('GeoBlueprint', __name__)

@GeoBlueprint.route('/all', methods=['GET'])
def get_all():
    response = client.table('geo').select('country', 'capital', 'region').execute()
    return response.data