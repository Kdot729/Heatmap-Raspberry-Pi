from google.cloud import bigtable
from datetime import datetime, timedelta, timezone
import pymongo, os
from pixel import Pixel

Mongo_URI = os.getenv("MONGO_URI")

Mongo_Client = pymongo.MongoClient(Mongo_URI)
MongoDB = Mongo_Client["coinbase"]
ETH_Collection = MongoDB["ETH"]

Project_ID = "terraform-441517"
BigTable_Instance_ID = "bigtable-instance"
Zone = "us-central1-a"

BigTable_Client = bigtable.Client(project=Project_ID, admin=True)
BigTable_Instance = BigTable_Client.instance(BigTable_Instance_ID)

Table_ID = "coinbase"
Table = BigTable_Instance.table(Table_ID)

Sum_Key = "sum"
Color_Key = "color"
UTF8 = "utf-8"
Column_Family = "eth"

def Convert_Float_to_Bytes(value) -> str:
    return str(value).encode(UTF8)

def Insert_Data(Document) -> None:

    DateTime = Document["_id"]["datetime"]
    sum_value = Document[Sum_Key]

    # Converting timestamp to bytes 
    Row_Key = str(DateTime.timestamp()).encode(UTF8)

    Row = Table.row(Row_Key)

    RGB_String = ",".join(map(str, Document[Color_Key]))

    Row.set_cell(Column_Family, Sum_Key, Convert_Float_to_Bytes(sum_value))
    Row.set_cell(Column_Family, Color_Key, RGB_String)

    Row.commit()

def Rounding_Down_to_Nearest_Minute() -> datetime:

    Seconds = 60
    DateTime = Get_Current_Time()
    DateTime_Seconds = DateTime.second

    return datetime.strptime((DateTime - timedelta(seconds=(Seconds + DateTime_Seconds) % Seconds)).strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")

def Get_Current_Time() -> datetime:
    return datetime.now(timezone.utc)

Status = False
Color = Pixel()

while True:

    if Get_Current_Time().second == 0 and not Status:

        Round_Down_DateTime = Rounding_Down_to_Nearest_Minute()
        GTE_Datetime = Round_Down_DateTime - timedelta(seconds=60)
        LT_Datetime = Round_Down_DateTime - timedelta(seconds=1)

        Pipeline = [{
                    "$match":
                    {
                        "datetime": {"$gte": GTE_Datetime, "$lt": LT_Datetime}
                    }
                },
                {
                    "$group":
                    {"_id": {"datetime": {"$dateTrunc": {"date": "$datetime", "unit": "second","binSize": 1}}},
                        "sum": {"$sum": "$size"}
                    }
                },
                {
                    "$project": {"_id": 1, "sum": {"$round": ["$sum", 2]}}
                },
                {
                    "$sort": {"_id.datetime": 1}
                }
            ]
        Result = ETH_Collection.aggregate(Pipeline)

        Data = list(Result)
        if Data:
            for Document in Data:
                Color.Pixel_Color = Document[Sum_Key]
                Document[Color_Key] = Color.Pixel_Color
                Insert_Data(Document)

        Status = True
    
    elif Get_Current_Time().second != 0:
        Status = False