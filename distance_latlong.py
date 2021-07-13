from decimal import Decimal
from yandex_geocoder import Client
from math import sin, cos, sqrt, atan2, radians

R = 6373.0
client = Client("529d15e0-0ebb-4898-b7f9-4575fe7e4366")

lat1 = "55.730174"
long1 = "37.574317"
lat2 = "55.730174"
long2 = "37.574317"
# lat2 = "55.745619"
# long2 = "37.278659"

check_location1 = client.address(Decimal(long1), Decimal(lat1)).split(", ")
check_location2 = client.address(Decimal(long2), Decimal(lat2)).split(", ")

if('Москва' in check_location1 or 'Moscow' in check_location1):
    for i in range(len(check_location1)):
        if(check_location1[i] == 'Москва' or check_location1[i] == 'Moscow'):
            if('Москва' in check_location2 or 'Moscow' in check_location2):
                for i in range(len(check_location2)):
                    if(check_location2[i] == 'Москва' or check_location2[i] == 'Moscow'):
                        
                        print("Can't calculate between Moscow and Moscow")

address1_lat = radians(Decimal(lat1))
address1_long = radians(Decimal(long1))
address2_lat = radians(Decimal(lat2))
address2_long = radians(Decimal(long2))

dlong = address2_long - address1_long
dlat = address2_lat - address1_lat

a = sin(dlat / 2)**2 + cos(address1_lat) * cos(address2_lat) * sin(dlong / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print("Result:", distance, "KM")