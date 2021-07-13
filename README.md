
Windows needs
- Python 3.8
- pip install gevent --pre
- pip install auto-py-to-exe
- pip install yandex-geocoder

![Flask Documentation](https://user-images.githubusercontent.com/22582712/125488610-4fa0390e-ba2a-4239-9100-55dedf07b300.jpg)

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
