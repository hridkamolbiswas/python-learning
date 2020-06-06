import simpy
from datetime import date, time,datetime,timedelta
import numpy as np

from config import config, tick_to_time, time_to_tick
from objects import Sim, Car, reporting


env = simpy.Environment()
sim= Sim()

for i in range(0,20):
    ob = Car(env,2,10)
    sim.car_list.append(ob)


car = Car(env,2,5)
env.process(reporting(env, ob, sim))

env.run(until=time_to_tick(30))





