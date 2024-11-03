import tracemalloc
from websocket import create_connection
import json, pymongo
from datetime import datetime


Mongo_Client = pymongo.MongoClient(host='coinbase_mongodb',
                        port=27017, 
                        username='root', 
                        password='example',
                        authSource="admin")
MongoDB = Mongo_Client["coinbase"]

ETH_Collection = MongoDB["ETH"]

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
        Memory_Usage = tracemalloc.get_traced_memory()
        if Memory_Usage[0] >= 300000:
            pass
        else:              
            ETH_Data = json.loads(Socket.recv())

            if "match" in ETH_Data["type"]:
                Data =  {
                            "datetime": datetime.strptime(ETH_Data["time"], "%Y-%m-%dT%H:%M:%S.%fZ"),
                            "side": ETH_Data["side"],
                            "size": float(ETH_Data["size"]),
                            "price": float(ETH_Data["price"])
                        }

                ETH_Collection.insert_one(Data)
