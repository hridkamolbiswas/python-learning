import simpy
import numpy as np
from config import tick_to_time, time_to_tick

class Sim:
    def __init__(self, env):
        self.env = env
        self.n_driving=[]
        self.n_parking=[]
        self.car_list=[]

class Car:
    
    def __init__(self, sim, start_time, parking_time, driving_time):
        self.sim = sim
        self.start_time = start_time
        self.parking_time = np.random.randint(3,6)
        self.driving_time =  np.random.randint(10,15)
        self.is_driving = False
        self.is_parking = True
        self.sim.car_list
        self.action = self.sim.env.process(self.car_working())


    def car_working(self):
        while True:
            #print('\tStart parking at %s' % tick_to_time(self.env.now))
            self.is_parking = True
            self.is_driving = False
            yield self.sim.env.timeout(time_to_tick(self.parking_time))

            self.is_parking = False
            self.is_driving = True
            #print('Start driving at %s' % tick_to_time(self.env.now))
            yield self.sim.env.timeout(time_to_tick(self.driving_time))

