FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt requirements.txt 

RUN pip3 install --no-cache-dir -r requirements.txt

# Change json file name to match your json
COPY terraform-441517-7c57012e3f82.json /app/terraform-441517-7c57012e3f82.json

ENV GOOGLE_APPLICATION_CREDENTIALS="/app/terraform-441517-7c57012e3f82.json"

COPY . /app

EXPOSE 8000