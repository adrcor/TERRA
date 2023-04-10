from flask import Blueprint
from model import Geo

GeoBlueprint = Blueprint('GeoBlueprint', __name__)

@GeoBlueprint.route('/all', methods=['GET'])
def get_all():
    data = Geo.get_all()
    return [obj.to_dict() for obj in data]