from datetime import datetime, timezone
import json, tracemalloc
from time import sleep
from websocket import create_connection
from pixel import Pixel

tracemalloc.start()

def Get_Current_Time() -> datetime:
        return datetime.now(timezone.utc)

def Initialize_Dict():
    return {key: [0, (0,0,0)] for key in range(0, 60)}

def Write_to_JSON(Data):
    with open('data.json', 'w', encoding='utf8') as File:
        json.dump(Data, File, indent=4)

Datetime = Get_Current_Time()
Coinbase_WebSocket = create_connection("wss://ws-feed.exchange.coinbase.com")
Coinbase_WebSocket.send(json.dumps({"type": "subscribe", "product_ids": ["ETH-USD"], "channels": ["matches"]}))

Sense_Hat_Pixel = Pixel()

Seconds = Initialize_Dict()
Write_to_JSON(Seconds)

while True:

    Memory_Usage = tracemalloc.get_traced_memory()

    if Memory_Usage[0] >= 200000:
        Seconds = Initialize_Dict()
        Write_to_JSON("stop")
        sleep(0.5)
    else:
        if (Get_Current_Time().second == 0):
            Seconds = Initialize_Dict()

        Index = Get_Current_Time().second

        ETH_Data = json.loads(Coinbase_WebSocket.recv())

        if "match" in ETH_Data["type"]:

            Seconds[Index][0] += float(ETH_Data["size"])
            Seconds[Index][0] = float("{:.2f}".format(Seconds[Index][0]))
            Row = Index % 8
            Column = Index // 8

            Sense_Hat_Pixel.Pixel_Color = Seconds[Index][0]
            Seconds[Index][1] = Sense_Hat_Pixel.Pixel_Color

            Write_to_JSON(Seconds)

        else:
            pass