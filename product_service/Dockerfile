FROM python:3.9.5

#maintainer
LABEL Author="Andre Hangalo"
ENV   PYTHONUNBUFFERED 1
RUN mkdir /product_service

COPY product_service/requirements.txt /product_service/requirements.txt
RUN pip install -r product_service/requirements.txt
COPY . /product_service
WORKDIR /product_service
EXPOSE 3001

RUN python product_service/manage.py makemigrations
RUN python product_service/manage.py migrate