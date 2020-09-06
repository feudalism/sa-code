import matplotlib.pyplot as plt
import numpy as np

from Parameters import Parameters

# Tuned parameters
g = 4.0/10
h = 1./3
	
def set_sim_parameters(t0, tf, dt, x0):
	sim_params = Parameters()
	sim_params.t0 = t0
	sim_params.tf = tf
	sim_params.dt = dt
	sim_params.x0 = x0
	return sim_params


def model(x_est, dt):
    x = x_est[0]
    xd = x_est[1]
    
    x_next = np.zeros(2)
    x_next[0] = x + xd * dt
    x_next[1] = xd
    
    return x_next

def update_step(x_est, z, g, h, dt):
    x = x_est[0]
    xd = x_est[1]
    
    residual = z - x
    
    x_est = np.zeros(2)
    x_est[0] = x + g * residual
    x_est[1] = xd + h * (residual / dt)
    return x_est
    
def plot_measurements(measurements, sim_time):
    plt.plot(np.linspace(1, sim_time, sim_time), measurements, 'ro')

def plot_estimates(estimates, sim_params):
    plt.plot(np.arange(0, sim_params.tf+1, sim_params.dt), estimates, 'gv:')

def plot_predictions(predictions, sim_params):
    plt.plot(np.arange(1, sim_params.tf+1, sim_params.dt), predictions, 'bx--')

def plot_ground_truth(tf):
    x0 = 160
    x_end = 173
    t = np.linspace(0, tf, tf+1)
    plt.plot(t, np.linspace(x0, x_end, len(t)), 'k')
    
def g_h_filter(data, g, h, sim_params):
    estimates = [sim_params.x0[0]]
    predictions = []
    
    # Initialise states
    x_prev = sim_params.x0   
    
    for z in data:
        # Predict step
        x_est = model(x_prev, sim_params.dt)
        predictions.append(x_est[0])
        
        # Update step
        x_est = update_step(x_est, z, g, h, sim_params.dt)
        estimates.append(x_est[0])
        
        x_prev = x_est
        
    return estimates
    
def plot_zx(z,x,sim_params):
    plot_measurements(z, sim_params.tf)
    plot_estimates(x, sim_params)
    plt.legend(['measurements', 'estimates'])
    plt.grid()
    plt.show()

def gen_noisy_data(x0, dx, count, amplitude):
    return [x0 + dx*i + np.random.randn()*amplitude for i in range(count)]
    
def weight_exp():
    measurements = [158.0, 164.2, 160.3, 159.9, 162.1, 164.6, 
                    169.6, 167.4, 166.4, 171.0, 171.2, 172.6]
    
    tf = len(measurements)
    dt = 1.0 # 
    
    weight_init = 160.
    weight_gain_init = -1
    x0 = [weight_init, weight_gain_init]
    
    sim_params = set_sim_parameters(0., tf, dt, x0)
    
    return measurements, sim_params
    
def noisy_exp():
    x0 = 5.
    xd0 = 2.
    n = 100
    amplitude = 100
    
    data = gen_noisy_data(x0, xd0, n, amplitude)
    
    bad_x0 = 100.
    sim_params = set_sim_parameters(0, len(data), 1, [x0, xd0])
    
    return data, sim_params

if __name__ == '__main__':
    # measurements, sim_params = weight_exp()  
    #plot_ground_truth(sim_params.tf)    
    
    z, sim_params = noisy_exp()   
    x = g_h_filter(z, g, h, sim_params)
    plot_zx(z, x, sim_params)