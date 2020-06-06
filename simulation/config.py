from datetime import time, date, datetime, timedelta
config = {'START_TIME' :time(9,0),
'end' : time(16,0)
        }


def tick_to_time(tick):
    return datetime.combine(date.today(),config["START_TIME"]) + timedelta(seconds=tick)
    
def time_to_tick(minutes):
    return minutes*60 # convert to second




