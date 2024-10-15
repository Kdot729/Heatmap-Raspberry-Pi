from fastapi import FastAPI
import json
from websocket import create_connection
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

Coinbase_WebSocket = create_connection("wss://ws-feed.exchange.coinbase.com")
Coinbase_WebSocket.send(json.dumps({"type": "subscribe", "product_ids": ["ETH-USD"], "channels": ["matches"]}))
Response = []

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Router = APIRouter()

@app.get("/")
def table():
    while True:
        ETH_Data = json.loads(Coinbase_WebSocket.recv())
        if "match" in ETH_Data["type"]:
            Response.append({"size": ETH_Data["size"], "price": ETH_Data["price"], "time": ETH_Data["time"]})
            return {"data": Response}
        else:
            return {}