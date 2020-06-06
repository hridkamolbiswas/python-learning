from datetime import time, date, datetime, timedelta

config = {"START_TIME": time(9, 0), 
            "end": time(16, 0)}


drivers = {time(9, 0): "hrid1", 
           time(9, 20): "hrid2", 
           time(9, 30): "hrid3"}

passengers = 100


def tick_to_time(tick):
    return (datetime.combine(date.today(), config["START_TIME"]) + timedelta(seconds=tick)).time()


def time_to_tick(minutes):
    return minutes * 60  # convert to second

#print(tick_to_time(5))


