# syntax = docker/dockerfile:1.2.1
FROM python:3.8 
RUN mkdir /code
WORKDIR /code 
COPY requirements.txt /code/ 
RUN --mount=type=cache,target=/root/.cache \
    pip3 install -r requirements.txt 
COPY . /code/
