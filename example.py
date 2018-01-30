# -*- coding: utf-8 -*-
"""
Example Test Module for Bilateral Shapley Value
"""

from mesa import Model
from mesa.time import RandomActivation
from mesa import Agent
from BilateralShapley import BSV
import numpy as np


class TestAgent(Agent):
    '''Initialize agents with values for power and preference (in this case affinity as preference)'''
    def __init__(self, unique_id, model, maxaffinity, maxeconomic, maxmilitary):
        # use Mesa agent module
        super().__init__(unique_id, model)
        # preference attribute of each agent
        self.affinity = np.random.uniform(1, maxaffinity)
        # economic value of each agent which is combined with military for power
        self.economic = np.random.uniform(1,maxeconomic)
        # military value of each agent which is combined with economic for power
        self.military = np.random.uniform(1,maxmilitary)
        # calculate power as average economic and military power
        self.power = (self.economic+self.military) / 2


class TestModel(Model):
    '''Initialize model'''
    def __init__(self, N, maxaffinity, maxeconomic, maxmilitary):
        self.numagents = N
        self.schedule = RandomActivation(self)
        for i in range(self.numagents):
            a = TestAgent(i, self, maxaffinity, maxeconomic, maxmilitary)
            self.schedule.add(a)
            
    
    '''Call the bsv module'''        
    def execution(self):
        testnet = BSV(self.schedule.agents, "power", "affinity", verbose = False)
        return testnet    
'''
THIS CALLS AND RUNS THE MAIN CLASSES FUNCTIONS
'''

#call the TestModel Class
test = TestModel(500, 20, 100, 100) #parameters are number of agents, max affinity value, max economic value and max military
#execute the bilateral shapley value
test = test.execution()
print ("Numer of Groups: ", len(test.result))
print ("Group list: ", test.result)