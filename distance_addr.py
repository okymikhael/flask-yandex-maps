from decimal import Decimal
from yandex_geocoder import Client
from math import sin, cos, sqrt, atan2, radians

client = Client("529d15e0-0ebb-4898-b7f9-4575fe7e4366")

# approximate radius of earth in km
R = 6373.0

# from address
coordinates1 = client.coordinates("Москва Льва Толстого 16")
coordinates2 = client.coordinates("Settlement of Arkhangelskoe")

address1 = str(coordinates1).replace("Decimal('", '').replace("')", '').replace("(", '').replace(")", '').split(", ")
address2 = str(coordinates2).replace("Decimal('", '').replace("')", '').replace("(", '').replace(")", '').split(", ")

dlong = radians(Decimal(address2[0])) - radians(Decimal(address1[0]))
dlat = radians(Decimal(address2[1])) - radians(Decimal(address1[1]))

a = sin(dlat / 2)**2 + cos(Decimal(address1[1])) * cos(Decimal(address2[1])) * sin(dlong / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

# print("Result:", distance, "KM")
