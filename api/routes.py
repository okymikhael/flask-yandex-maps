from flask import Blueprint, request
from decimal import Decimal
from yandex_geocoder import Client
from math import sin, cos, sqrt, atan2, radians

R = 6373.0
api = Blueprint('api', __name__, url_prefix='/api')
client = Client("529d15e0-0ebb-4898-b7f9-4575fe7e4366")

@api.route('/coordinate', methods=['POST'])
def coordinate():
    if request.method == 'POST':
        req = request.json
        latitude1 = req['latitude1']
        longitude1 = req['longitude1']
        latitude2 = req['latitude2']
        longitude2 = req['longitude2']
        result = distance_coordinates(latitude1, longitude1, latitude2, longitude2)
        message = 'Distance between 4 coordinate is {0} KM'.format(result)
        return {'status': 'success', 'message': message}
    
def distance_coordinates(latitude1, longitude1, latitude2, longitude2):
    address1_lat = radians(Decimal(float(latitude1)))
    address1_long = radians(Decimal(float(longitude1)))
    address2_lat = radians(Decimal(float(latitude2)))
    address2_long = radians(Decimal(float(longitude2)))

    dlong = address2_long - address1_long
    dlat = address2_lat - address1_lat

    a = sin(dlat / 2)**2 + cos(address1_lat) * cos(address2_lat) * sin(dlong / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance