import json, numpy
from sense_hat import SenseHat
from websocket import create_connection
from format_datetime import Format_Datetime
from pixel import Pixel

def Initialize_Array():
    return numpy.array([[i, 0] for i in range(0, 60)])

Sense_Hat = SenseHat()
Sense_Hat_Pixel = Pixel()
Datetime = Format_Datetime()

Seconds = Initialize_Array()
Sense_Hat.clear()

Coinbase_WebSocket = create_connection("wss://ws-feed.exchange.coinbase.com")
Coinbase_WebSocket.send(json.dumps({"type": "subscribe", "product_ids": ["ETH-USD"], "channels": ["matches"]}))

while True:

    if (Datetime.Current_Time.second == 0):
        Sense_Hat.clear(0, 0, 0)
        Seconds = Initialize_Array()

    Index = Datetime.Current_Time.second
    Sum = Seconds[Index][1]

    Row = Index % 8
    Column = Index // 8

    ETH_Data = json.loads(Coinbase_WebSocket.recv())

    if "match" in ETH_Data["type"]:

        Sum += float(ETH_Data["size"])

    Sense_Hat_Pixel.Pixel_Color = Sum
    Sense_Hat.set_pixel(Row, Column, Sense_Hat_Pixel.Pixel_Color)