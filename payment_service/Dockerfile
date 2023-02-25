FROM python:3.9.5

#maintainer
LABEL Author="Andre Hangalo"
ENV   PYTHONUNBUFFERED 1
RUN mkdir /payment_service

COPY payment_service/requirements.txt /payment_service/requirements.txt
RUN pip install -r payment_service/requirements.txt
COPY . /payment_service
WORKDIR /payment_service
EXPOSE 4001

RUN python payment_service/manage.py makemigrations
RUN python payment_service/manage.py migrate