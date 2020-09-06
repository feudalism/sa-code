# Function to test the implementation of a basic multivariate Kalman filter
# for 1D tracking, using 1 sensor

from cls import Parameters, set_sim_parameters
from cls import KalmanFilter
from cls import Dog

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Simulation parameters
t0 = 0
tf = 1
dt = 0.1
x0 = 0
sim_params = set_sim_parameters(t0, tf, dt, x0)

# Initial conditions
x0 = 10. # [m]
v0 = 4.5 # [m/s]
IC = np.array([[x0], [v0]])

# # Define inital variances
var_pos = 500. # [m^2] - uncertain about x0

dog_max_speed = 21. # [m/s]
std_vel = dog_max_speed / 3. # [m/s] - 99.7% chance
var_vel = std_vel**2

cov_pos_vel = 0 # no knowledge
P = np.diag([var_pos, var_vel])

# Model
dog = Dog(x=x0, v=v0, state_cov=P, dt=sim_params.dt)
filter = KalmanFilter(system=dog, IC=IC)

# Simulation
print("Dog Tracking")
x_est = [x0]
count = 3
measurements = np.ones(count)

for i, z in enumerate(measurements):    
    filter.predict()
    filter.update(z)
    
    print(f"Update {i}")
    filter.print_info()
    
    x_est.append(filter.x[0][0])
    
    # dog.plot_covariance(ax)
    
    # plt.draw()
    # plt.pause(plot_dt)
    
    # plt.clf()

# Plotting
fig, ax = plt.subplots(1,figsize=(6,6))
plot_dt = 0.1

t_est = np.linspace(0, count*dt, count+1)
ax.plot(t_est, x_est)

t_meas = np.linspace(dt, count*dt, count)
ax.plot(t_meas, measurements, 'ko')

plt.xlabel('time in s')
plt.ylabel('position in m')

plt.legend(['$x_{est}$', '$z$'])
plt.show()