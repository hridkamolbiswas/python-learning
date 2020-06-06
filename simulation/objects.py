import simpy
import numpy as np
from config import tick_to_time, time_to_tick

class Sim:
    def __init__(self):
        self.n_driving=[]
        self.n_parking=[]
        self.car_list=[]

class Car:
    
    def __init__(self, env, start_time, parking_time, driving_time):
        self.env = env
        self.start_time = start_time
        self.parking_time = np.random.randint(3,6)
        self.driving_time =  np.random.randint(10,15)
        self.is_driving = False
        self.is_parking = True
        self.action = env.process(self.car_working())


    def car_working(self):
        while True:
            #print('\tStart parking at %s' % tick_to_time(self.env.now))
            self.is_parking = True
            self.is_driving = False
            yield self.env.timeout(time_to_tick(self.parking_time))

            self.is_parking = False
            self.is_driving = True
            #print('Start driving at %s' % tick_to_time(self.env.now))
            yield self.env.timeout(time_to_tick(self.driving_time))

def reporting(env, car, sim):
    while True:

        driving_drivers = len([driver for driver in sim.car_list if driver.is_driving])
        driving_parking = len([driver for driver in sim.car_list if driver.is_parking])
        print(f"\t{tick_to_time(env.now)} driving {driving_drivers} parking {driving_parking}") 
        yield env.timeout(time_to_tick(1))