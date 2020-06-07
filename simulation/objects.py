import simpy
import numpy as np
from config import tick_to_time, time_to_tick

class Sim:
    
    def __init__(self, env):
        self.env = env
        self.n_driving=[]
        self.n_parking=[]
        self.car_list=[]
        self.passenger_list = [passenger() for item in passenger.passenger_list]
        self.seat_occupied = []


class Car:
    
    def __init__(self, sim, start_time, parking_time, driving_time):
        self.sim = sim
        self.start_time = start_time
        self.parking_time = np.random.randint(3,6)
        self.driving_time =  np.random.randint(10,15)
        self.is_driving = False
        self.is_parking = True
        #self.seat_occupied = []
        self.action = self.sim.env.process(self.car_working())


    def car_working(self):
        while True:
            #print('\tStart parking at %s' % tick_to_time(self.env.now))
            self.is_parking = True
            self.is_driving = False
            self.sim.n_parking.append(self)
            yield self.sim.env.timeout(time_to_tick(self.parking_time))

            self.is_parking = False
            self.is_driving = True
            #print('Start driving at %s' % tick_to_time(self.env.now))
            yield self.sim.env.timeout(time_to_tick(self.driving_time))


class passenger:

    passenger_list = np.arange(100)

    def __init__(self):
        self.is_Bus = False
        self.is_waiting = True

        

        

if __name__=='__main__':
    env = simpy.Environment()
    # print(passenger.passenger_list)
    # print(type(passenger.passenger_list))
    #passenger = passenger()
    pl = Sim(env).passenger_list
    for item in pl:
        print(item.is_waiting)