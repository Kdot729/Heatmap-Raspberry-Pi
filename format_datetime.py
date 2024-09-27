from datetime import datetime, timezone

class Format_Datetime():

    def __init__(self) -> None:
        pass

    def Get_Current_Time(self) -> datetime:
        return datetime.now(timezone.utc)
    
    @property
    def Current_Time(self) -> datetime: 
         return self.Get_Current_Time()