FROM python:3.9.5

#maintainer
LABEL Author="Andre Hangalo"
ENV   PYTHONUNBUFFERED 1
RUN mkdir /shipment_service

COPY shipment_service/requirements.txt /shipment_service/requirements.txt
RUN pip install -r shipment_service/requirements.txt
COPY . /shipment_service
WORKDIR /shipment_service
EXPOSE 5000

RUN python shipment_service/manage.py makemigrations
RUN python shipment_service/manage.py migrate