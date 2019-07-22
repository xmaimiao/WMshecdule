import datetime
from common.context import replace,Context
class Setting:
    def get_time(self):
        starttime = datetime.datetime.now().strftime("%H:%M")
        endtime = (datetime.datetime.now()+ datetime.timedelta(minutes=60)).strftime("%H:%M")
        startday = datetime.datetime.now().strftime("%Y-%m-%d")
        nextday = (datetime.datetime.now()+ datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        setattr(Context,"starttime",starttime)
        setattr(Context,"endtime",endtime)
        setattr(Context,"startday",startday)
        setattr(Context,"nextday",nextday)


