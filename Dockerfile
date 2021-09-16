FROM python:3.8-alpine

WORKDIR /django-rest

ADD . .

RUN pip install -r requirements.txt

