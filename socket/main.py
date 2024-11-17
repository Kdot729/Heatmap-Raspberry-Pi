from websocket import create_connection
import json, pymongo, os
from datetime import datetime

Mongo_URI = os.getenv('MONGO_URI')

Mongo_Client = pymongo.MongoClient(Mongo_URI)
Mongo_Database = Mongo_Client["coinbase"]
ETH_Collection = Mongo_Database["ETH"]

Socket = create_connection("wss://ws-feed.exchange.coinbase.com")
Socket.send(
    json.dumps(
        {
            "type": "subscribe",
            "product_ids": ["ETH-USD"],
            "channels": ["matches"],
        }
    )
)

while True:
    ETH_Data = json.loads(Socket.recv())

    if "match" in ETH_Data["type"]:
        Data =  {
                    "datetime": datetime.strptime(ETH_Data["time"], "%Y-%m-%dT%H:%M:%S.%fZ"),
                    "side": ETH_Data["side"],
                    "size": float(ETH_Data["size"]),
                    "price": float(ETH_Data["price"])
                }
        ETH_Collection.insert_one(Data)