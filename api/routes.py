from flask import Blueprint, request
from decimal import Decimal
from yandex_geocoder import Client
from math import sin, cos, sqrt, atan2, radians

R = 6373.0
api = Blueprint('api', __name__, url_prefix='/api')
client = Client("529d15e0-0ebb-4898-b7f9-4575fe7e4366")

@api.route('/address', methods=['POST'])
def address():
    if request.method == 'POST':
        req = request.json
        addr1 = req['address1'] if 'address1' in req else None
        addr2 = req['address2'] if 'address2' in req else None
        result = distance_address(addr1, addr2)
        
        return {'status': 'success', 'message': result}

@api.route('/coordinate', methods=['POST'])
def coordinate():
    if request.method == 'POST':
        req = request.json
        latitude1 = req['latitude1'] if 'latitude1' in req else None
        longitude1 = req['longitude1'] if 'longitude1' in req else None
        latitude2 = req['latitude2'] if 'latitude2' in req else None
        longitude2 = req['longitude2'] if 'longitude2' in req else None
        result = distance_coordinates(latitude1, longitude1, latitude2, longitude2)
        
        return {'status': 'success', 'message': result}

def distance_coordinates(latitude1, longitude1, latitude2, longitude2):
    if(latitude1 is None or longitude1 is None or latitude2 is None or longitude2 is None):
        return 'Please check our documentation for using this feature'
    
    check_location1 = client.address(Decimal(longitude1), Decimal(latitude1)).split(", ")
    check_location2 = client.address(Decimal(longitude2), Decimal(latitude2)).split(", ")

    if('Москва' in check_location1 or 'Moscow' in check_location1):
        for i in range(len(check_location1)):
            if(check_location1[i] == 'Москва' or check_location1[i] == 'Moscow'):
                if('Москва' in check_location2 or 'Moscow' in check_location2):
                    for i in range(len(check_location2)):
                        if(check_location2[i] == 'Москва' or check_location2[i] == 'Moscow'):
                            return "Can't calculate between Moscow and Moscow"

    address1_lat = radians(Decimal(float(latitude1)))
    address1_long = radians(Decimal(float(longitude1)))
    address2_lat = radians(Decimal(float(latitude2)))
    address2_long = radians(Decimal(float(longitude2)))

    dlong = address2_long - address1_long
    dlat = address2_lat - address1_lat

    a = sin(dlat / 2)**2 + cos(address1_lat) * cos(address2_lat) * sin(dlong / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    
    return 'Distance between 4 coordinate is {0} KM'.format(distance)

def distance_address(addr1, addr2):
    if(addr1 is None or addr2 is None):
        return 'Please check our documentation for using this feature'
    
    coordinates1 = client.coordinates(addr1)
    coordinates2 = client.coordinates(addr2)

    address1 = str(coordinates1).replace("Decimal('", '').replace("')", '').replace("(", '').replace(")", '').split(", ")
    address2 = str(coordinates2).replace("Decimal('", '').replace("')", '').replace("(", '').replace(")", '').split(", ")

    check_location1 = client.address(Decimal(address1[0]), Decimal(address1[1])).split(", ")
    check_location2 = client.address(Decimal(address2[0]), Decimal(address2[1])).split(", ")

    if('Москва' in check_location1 or 'Moscow' in check_location1):
        for i in range(len(check_location1)):
            if(check_location1[i] == 'Москва' or check_location1[i] == 'Moscow'):
                if('Москва' in check_location2 or 'Moscow' in check_location2):
                    for i in range(len(check_location2)):
                        if(check_location2[i] == 'Москва' or check_location2[i] == 'Moscow'):
                            return "Can't calculate between Moscow and Moscow"

    dlong = radians(Decimal(address2[0])) - radians(Decimal(address1[0]))
    dlat = radians(Decimal(address2[1])) - radians(Decimal(address1[1]))

    a = sin(dlat / 2)**2 + cos(Decimal(address1[1])) * cos(Decimal(address2[1])) * sin(dlong / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    
    return 'Distance between 2 address is {0} KM'.format(distance)