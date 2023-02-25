FROM python:3.9.5

#maintainer
LABEL Author="Andre Hangalo"
ENV   PYTHONUNBUFFERED 1
RUN mkdir /user_service

COPY user_service/requirements.txt /user_service/requirements.txt
RUN pip install -r user_service/requirements.txt
COPY . /user_service
WORKDIR /user_service
EXPOSE 8000

RUN python user_service/manage.py makemigrations
RUN python user_service/manage.py migrate