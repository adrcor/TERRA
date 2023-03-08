from flask import Blueprint
from model import Geo

GeoBlueprint = Blueprint('GeoBlueprint', __name__)

@GeoBlueprint.route('/all', methods=['GET'])
def get_all():
    data = Geo.get_all()
    return data