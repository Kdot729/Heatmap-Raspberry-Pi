from google.cloud import bigtable
from datetime import datetime, timedelta, timezone

def Rounding_Down_to_Nearest_Minute() -> datetime:

    Seconds = 60
    DateTime = Get_Current_Time()
    DateTime_Seconds = DateTime.second

    return datetime.strptime((DateTime - timedelta(seconds=(Seconds + DateTime_Seconds) % Seconds)).strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")

def Get_Current_Time() -> datetime:
    return datetime.now(timezone.utc)

Project_ID = "terraform-441517"
BigTable_Instance_ID = "bigtable-instance"
Zone = "us-central1-a"

BigTable_Client = bigtable.Client(project=Project_ID, admin=True)
BigTable_Instance = BigTable_Client.instance(BigTable_Instance_ID)

Table_ID = "coinbase"
Table = BigTable_Instance.table(Table_ID)

def Read_Data() -> list:

    Round_Down_DateTime = Rounding_Down_to_Nearest_Minute()
    GTE_Datetime = Round_Down_DateTime - timedelta(seconds=60)
    LT_Datetime = Round_Down_DateTime - timedelta(seconds=1)

    Unix_Start_Date = str(GTE_Datetime.timestamp())
    Unix_End_Date = str(LT_Datetime.timestamp())

    # Query the table in between the dates (inclusive)
    Rows = Table.read_rows(start_key=Unix_Start_Date, end_key=Unix_End_Date)

    Result = []

    for Row in Rows:

        Row_Key = Row.row_key.decode('utf-8')
        Timestamp = float(Row_Key)

        # Converting Unix timestamp to a datetime object
        DateTime = datetime.fromtimestamp(Timestamp)

        Row_Data = {"datetime": DateTime}

        Cells = Row.cells

        for Column_Family_ID, Columns in Cells.items():
            for Column, Cell_List in Columns.items():
                for Cell in Cell_List:

                    Column = Column.decode('utf-8') 

                    Value = Cell.value.decode('utf-8')

                    if Column == "color":

                        RGB_Values = list(Value.split(','))
                        Value = f"rgb({RGB_Values[0]}, {RGB_Values[1]}, {RGB_Values[2]})"

                    Row_Data[Column] = Value

        Result.append(Row_Data)

    return Result