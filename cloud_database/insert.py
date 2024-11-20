from google.cloud import bigtable
from datetime import datetime, timedelta, timezone
import pymongo, os

Mongo_URI = os.getenv('MONGO_URI')

Mongo_Client = pymongo.MongoClient(Mongo_URI)
MongoDB = Mongo_Client["coinbase"]
ETH_Collection = MongoDB["ETH"]

Project_ID = "terraform-441517"
BigTable_Instance_ID = "bigtable-instance"
zone = "us-central1-a"

BigTable_Client = bigtable.Client(project=Project_ID, admin=True)
BigTable_Instance = BigTable_Client.instance(BigTable_Instance_ID)

table_id = "coinbase"
table = BigTable_Instance.table(table_id)

Sum_Key = "sum"
UTF8 = "utf-8"

def Convert_Float_to_Bytes(value) -> str:
    return str(value).encode(UTF8)

def Insert_Data(Document) -> None:

    DateTime = Document['_id']['datetime']
    sum_value = Document[Sum_Key]

    # Converting timestamp to bytes 
    Row_Key = str(DateTime.timestamp()).encode(UTF8)

    Row = table.row(Row_Key)

    Row.set_cell('eth', Sum_Key, Convert_Float_to_Bytes(sum_value))

    Row.commit()

def Rounding_Down_to_Nearest_Minute() -> datetime:

    Seconds = 60
    DateTime = Get_Current_Time()
    DateTime_Seconds = DateTime.second

    return datetime.strptime((DateTime - timedelta(seconds=(Seconds + DateTime_Seconds) % Seconds)).strftime('%Y-%m-%d %H:%M'), '%Y-%m-%d %H:%M')

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
                Color.Pixel_Color = Document["sum"]
                Document["color"] = Color.Pixel_Color
                Insert_Data(Document)

        Status = True
    
    elif Get_Current_Time().second != 0:
        Status = False