import simpy
from datetime import date, time,datetime,timedelta
import numpy as np

from config import config, tick_to_time, time_to_tick, drivers
from objects import Sim, Car

def shiftplanning(sim):

    while True:
        if tick_to_time(sim.env.now) in drivers:
            print(f"{tick_to_time(sim.env.now)} drives starting to work")
            ob = Car(sim, tick_to_time(sim.env.now),2,10)
            sim.car_list.append(ob)

        yield sim.env.timeout(1)

def reporting(sim):
    while True:

        driving_drivers = len([driver for driver in sim.car_list if driver.is_driving])
        driving_parking = len([driver for driver in sim.car_list if driver.is_parking])
        print(f"\t{tick_to_time(env.now)} driving {driving_drivers} parking {driving_parking}") 
        yield sim.env.timeout(1)

def tourplan(sim):
    pass

env = simpy.Environment()
sim= Sim(env)

PASSENGER = 100
SEAT_LIMIT = 25

drivers_log = []
env.process(shiftplanning(sim))
env.process(reporting(sim))

env.run(until=time_to_tick(31))


