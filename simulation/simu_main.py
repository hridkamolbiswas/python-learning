import simpy
from datetime import date, time,datetime,timedelta
import numpy as np

from config import config, tick_to_time, time_to_tick, drivers
from objects import Sim, Car, reporting


env = simpy.Environment()
sim= Sim()


def shiftplanning(env, drivers_log):

    while True:
        if tick_to_time(env.now) in drivers:
            print(f"{tick_to_time(env.now)} drives starting to wokr")
            ob = Car(env, tick_to_time(env.now),2,10)
            drivers_log.append(ob)
            print(drivers_log)
            for item in drivers_log:
                print('info:',item.start_time, item.parking_time, item.driving_time)
                print('\t',item.car_working())
        yield env.timeout(1)
    

# for i in range(0,len(drivers)):
#     ob = Car(env,2,10)
#     sim.car_list.append(ob)


# car = Car(env,2,5)
# env.process(reporting(env, ob, sim))



drivers_log = []
env.process(shiftplanning(env, drivers_log))

env.run(until=time_to_tick(31))


