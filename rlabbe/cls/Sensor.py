import math
import numpy as np
from numpy.random import randn

class Sensor(object):
    def __init__(self, z_var=0.):
        self.z = 0
        self.z_std = math.sqrt(z_var)
        
    def measure(self, state):
        self.z = state + randn() * self.z_std
        
    def get_measurement(self, state):
        self.measure(state)
        return self.z