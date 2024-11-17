FROM python:3.12-alpine

WORKDIR /app

# Install the required dependencies
RUN pip install google-cloud-bigtable

COPY requirements.txt requirements.txt 

RUN pip3 install --no-cache-dir -r requirements.txt

# Change json file name to match your json
COPY terraform-441517-7c57012e3f82.json /app/terraform-441517-7c57012e3f82.json

ENV GOOGLE_APPLICATION_CREDENTIALS="/app/terraform-441517-7c57012e3f82.json"

COPY . /app

RUN apk update && apk add --no-cache bash wget

RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -O /wait-for-it.sh && \
chmod +x /wait-for-it.sh