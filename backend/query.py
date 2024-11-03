from datetime import datetime, timedelta, timezone
from typing import Literal
from database import ETH_Collection
from pixel import Pixel

def Round_to_Nearest_Minute(DateTime: datetime, Direction: Literal["up", "down"]) -> datetime:

    Seoncds = 60
    DateTime_Seconds = DateTime.second
    match Direction:
        case "up":
            return datetime.strptime((DateTime + timedelta(seconds=(Seoncds - DateTime_Seconds) % Seoncds)).strftime('%Y-%m-%d %H:%M'), '%Y-%m-%d %H:%M')
        case "down":
            return datetime.strptime((DateTime - timedelta(seconds=(Seoncds + DateTime_Seconds) % Seoncds)).strftime('%Y-%m-%d %H:%M'), '%Y-%m-%d %H:%M')

def Get_Current_Time() -> datetime:
    return datetime.now(timezone.utc)

def Rounding_Minute(Current_Datetime) -> list[datetime]:
    return [Round_to_Nearest_Minute(Current_Datetime, "up"), Round_to_Nearest_Minute(Current_Datetime, "down")]

def Calculate_Sum():
    Color = Pixel()
    Current_Datetime = Get_Current_Time()
    Round_Up_DateTime, Round_Down_DateTime = Rounding_Minute(Current_Datetime)

    Pipeline = [{
                    "$match":
                    {
                        "datetime": {"$gte": Round_Down_DateTime, "$lt": Round_Up_DateTime}
                    }
                },
                {
                    "$group":
                    {"_id": {"datetime": {"$dateTrunc": {"date": "$datetime", "unit": "second","binSize": 2}}},
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
        for Entry in Data:
            Color.Pixel_Color = Entry["sum"]
            Entry["color"] = Color.Pixel_Color
        return Data
    else:
        return []