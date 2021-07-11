from decimal import Decimal
from yandex_geocoder import Client
from math import sin, cos, sqrt, atan2, radians

R = 6373.0
client = Client("529d15e0-0ebb-4898-b7f9-4575fe7e4366")
address1_lat = radians(Decimal("55.733969"))
address1_long = radians(Decimal("55.733969"))
address2_lat = radians(Decimal("55.733969"))
address2_long = radians(Decimal("55.733969"))

dlong = address2_long - address1_long
dlat = address2_lat - address1_lat

a = sin(dlat / 2)**2 + cos(address1_lat) * cos(address2_lat) * sin(dlong / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print("Result:", distance, "KM")
