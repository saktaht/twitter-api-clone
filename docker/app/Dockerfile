FROM python:3.12

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /root/app

WORKDIR /root/app

RUN pip install --upgrade pip \
    && pip install --upgrade setuptools 

COPY requirements.txt /root/app/

RUN pip install -r requirements.txt