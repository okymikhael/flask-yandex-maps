# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-yandex/

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /python-yandex/

CMD [ "python", "/python-yandex/__init__.py" ]