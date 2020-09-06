import numpy as np

class KalmanFilter(object):
    def __init__(self, system=None, dt=None, IC=None):
        self.system = system
        self.x = np.zeros(len(system.x))
        self.initialise(IC)
        
        self.F = self.system.F
        self.P = self.system.P
        self.Q = self.system.Q
        
        self.H = np.array([[1., 0.]])
        self.R = np.array([[5.]])       # only 1 sensor
        
        if dt is None:
            self.dt = self.system.dt
        else:
            self.dt = dt
        
    def initialise(self, IC):
        self.x = np.array([IC[0],
                           IC[1]])   
        
    def print_info(self):
        print "x = {0:.2f} m, v = {1:.2f} m/s".format(self.x[0][0], self.x[1][0])
        print "{0}".format(self.P.round(decimals=2))
        
    def calculate_states(self, dt=None):
        self.x = self.system.calculate_states(dt)
        
    def calculate_covariances(self, dt=None):     
        self.P = np.linalg.multi_dot([self.F, self.P, self.F.T]) + self.Q
        
    def predict(self):
        self.calculate_states()
        self.calculate_covariances()
        
    def calculate_kalman_gain(self):
        # S: innovation covariance
        S = np.linalg.multi_dot([self.H, self.P, self.H.T]) + self.R
        return np.linalg.multi_dot([self.P, self.H.T, np.linalg.inv(S)])
        
    def update(self, z):
        res = z - np.dot(self.H, self.x)
        K = self.calculate_kalman_gain()
        
        self.x += np.dot(K, res)
        p_update_term = (np.eye(len(self.P)) - np.dot(K, self.H))
        self.P = np.dot(p_update_term, self.P)
        