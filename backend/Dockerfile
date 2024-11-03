FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt requirements.txt 

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000