FROM node:20.18.0-alpine

RUN mkdir -p /app

WORKDIR /app

COPY package.json .

RUN npm install

RUN npm install -g serve

COPY . .

EXPOSE 3000

RUN npm run build