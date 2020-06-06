import simpy
from datetime import date, time,datetime,timedelta
import numpy as np

START_TIME = time(9,0)

def tick_to_time(tick):
    return datetime.combine(date.today(),START_TIME) + timedelta(seconds=tick)
    
def time_to_tick(minutes):
    return minutes*60 # convert to second
class Sim:
    def __init__(self):
        self.n_driving=[]
        self.n_parking=[]
        self.car_list=[]

class Car:
    
    def __init__(self, env, parking_time, driving_time):
        self.env = env
        self.parking_time = np.random.randint(3,6)
        self.driving_time =  np.random.randint(10,15)
        self.is_driving = False
        self.is_parking = True
        self.action = env.process(self.car_working())


    def car_working(self):
        while True:
            #print('\tStart parking at %s' % tick_to_time(env.now))
            self.is_parking = True
            self.is_driving = False
            yield env.timeout(time_to_tick(self.parking_time))

            self.is_parking = False
            self.is_driving = True
            #print('Start driving at %s' % tick_to_time(env.now))
            yield env.timeout(time_to_tick(self.driving_time))

def reporting(env, car, sim):
    while True:

        driving_drivers = len([driver for driver in sim.car_list if driver.is_driving])
        driving_parking = len([driver for driver in sim.car_list if driver.is_parking])
        print(f"\t{tick_to_time(env.now)} driving {driving_drivers} parking {driving_parking}") 
        yield env.timeout(time_to_tick(minutes=1))

env = simpy.Environment()
sim= Sim()

for i in range(0,20):
    ob = Car(env,2,10)
    sim.car_list.append(ob)


car = Car(env,2,5)
env.process(reporting(env, ob, sim))

env.run(until=time_to_tick(30))





