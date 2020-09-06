import math
import numpy as np
from numpy.random import randn

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms


class Dog(object):
    def __init__(self, x=0., v=0., state_cov=0., process_cov=0., dt=0):
        self.x = np.array([[x],
                           [v]])        
        self.dt = dt
        
        # transition matrix
        self.F = np.array([[1, dt],
                           [0, 1]])
                           
        # covariances
        self.P = state_cov
        self.Q = process_cov
        
    def calculate_states(self, dt=None):
        self.x = np.dot(self.F, self.x)
        return self.x
        
    def unpack_states(self):
        return self.x[0], self.x[1]
        
    def plot_states(self, ax):  
        pos, vel = self.unpack_states()
        ax.plot(pos, vel, 'r+')
        
    def plot_covariance(self, ax):
        """ NOT WORKING """
        
        pos, vel = self.unpack_states()
        
        self.plot_states(ax)
        
        eigvect, s, _ = np.linalg.svd(self.P)
        angle_radians = math.atan2(eigvect[1, 0], eigvect[0, 0])
        angle_deg = angle_radians * 180 / math.pi
        
        num_deviations = 1
        width = 2 * num_deviations * math.sqrt(s[0])
        height = 2 * num_deviations * math.sqrt(s[1])
        
        # width = np.sqrt(self.P[0, 0]) * 1
        # height = np.sqrt(self.P[1, 1]) * 1
        # width = 0.5
        # height = 2
        ellipse = Ellipse((pos, vel), width=width,
                                  height=height,
                                  angle=angle_deg,
                                  facecolor='blue',
                                  edgecolor='darkblue',
                                  alpha=0.3,
                                  lw=2,
                                  ls='solid')
        # transf = transforms.Affine2D().rotate_deg(45)
            # # .scale(scale_x, scale_y) \
        # ellipse.set_transform(transf)
        ax.add_patch(ellipse)
        
        plt.xlim([-1, 14])
        plt.ylim([-1, 14])
        