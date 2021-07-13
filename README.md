Windows needs
- pip install gevent --pre
- pip install auto-py-to-exe
- pip install yandex-geocoder

Positive Case
host: http://localhost:5000/api/address
method: POST
bodyType: raw
data: {
    "address1": "Москва Льва Толстого 16",
    "address2": "Settlement of Arkhangelskoe"
}

host: http://localhost:5000/api/coordinate
method: POST
bodyType: raw
data: {
    "latitude1": "55.730174",
    "longitude1": "37.574317",
    "latitude2": "55.745619",
    "longitude2": "37.278659"
}

Negative Case
host: http://localhost:5000/api/address
method: POST
bodyType: raw
data: {
    "address1": "Москва Льва Толстого 16",
    "address2": "Settlement of Arkhangelskoe"
}

host: http://localhost:5000/api/coordinate
method: POST
bodyType: raw
data: {
    "latitude1": "55.730174",
    "longitude1": "37.574317",
    "latitude2": "55.730174",
    "longitude2": "37.574317"
}