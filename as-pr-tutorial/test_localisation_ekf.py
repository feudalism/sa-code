import numpy as np

GPS_NOISE = np.diag([0.5, 0.5]) ** 2

SIM_TIME = 50. # [s]
DT = 0.1 # [s]
vel = 1.0 # [m/s]
omega = 0.1 # [rad/s]

def motion_model(x, y):
    """ Based on xd = v cos theta
                 yd = v sin theta
             thetad = omega
        
        F and B are the jacobians w.r.t. x, u
        for the linearised state equation
             x_next = F x + B u
    """
    F = np.array([[1.0, 0, 0, 0],
                  [0, 1.0, 0, 0],
                  [0, 0, 1.0, 0],
                  [0, 0, 0, 0]])

    B = np.array([[DT * math.cos(x[2, 0]), 0],
                  [DT * math.sin(x[2, 0]), 0],
                  [0.0, DT],
                  [1.0, 0.0]])

    x_next = F @ x + B @ u
    return x_next
    
def observation_model(x):
    H = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0]
    ])

    z = H @ x

    return z

def observation(x_true, x_deadreckoning, u):
    x_true = motion_model(x_true, u)
    z = observation_model(x_true) + GPS_NOISE @ np.random.randn(2, 1)
    ...
    # return x_true, z, x_deadreckoning, ud

def get_input():
    u = np.array([[vel], [omega]])
    return u

def main():
    time = 0.0
    
    # initialise the state vectors [x y yaw v]' and covariance matrix
    x_est = np.zeros((4,1))
    x_true = np.zeros((4,1))
    x_deadreckoning = np.zeros((4, 1))
    
    P_est = np.eye(4)
    
    # initialise history (states x, observation z)
    hx_est = x_est
    hx_true = x_true
    hx_deadreckoning = x_deadreckoning
    
    # # position observation e.g. GPS
    hz = np.zeros((2, 1))
    
    while SIM_TIME > time:
        time = += DT
        u = get_input()
        
        x_true, z, x_deadreckoning, ud = observation(x_true, x_deadreckoning, u)
    


if __name__ == '__main__':
    main()