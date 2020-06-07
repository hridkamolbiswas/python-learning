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
            sim.car_list.append(ob) #important

        yield sim.env.timeout(1)

def reporting(sim):
    while True:

        driving_drivers = len([driver for driver in sim.car_list if driver.is_driving])
        driving_parking = len([driver for driver in sim.car_list if driver.is_parking])
        #print(f"\t{tick_to_time(env.now)} driving {driving_drivers} parking {driving_parking}") 
        yield sim.env.timeout(1)

def tourplan(sim):

    while True:
        print(f"{tick_to_time(sim.env.now)} n parking cars = {sim.n_parking}")
        #print(sim.n_parking)
        # if sim.is_parking:
        #     for passenger in sim.passenger_list:
        #         if len(sim.seat_occupied) < SEAT_LIMIT:
        #             sim.seat_occupied.append(passenger)
        #             sim.passenger_list.remove(passenger)

        # print(f"passenger left = {len(sim.passenger_list)  - len(sim.seat_occupied)}")   

        yield sim.env.timeout(1)




    


    

env = simpy.Environment()
sim= Sim(env)

SEAT_LIMIT = 25

drivers_log = []
env.process(shiftplanning(sim))
env.process(reporting(sim))
env.process(tourplan(sim))

env.run(until=time_to_tick(31))

#tourplan(sim)


