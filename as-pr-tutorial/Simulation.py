import numpy as np

class Simulation(object):
	"""
		Simulation object
	"""
	def __init__(self, sim_params):
		self.t0 = sim_params.t0
		self.tf = sim_params.tf
		self.dt = sim_params.dt
		self.x0 = sim_params.x0
		
	def simulate(self, odefunction):
		tt = self.get_time_vector()
		
		sol = sci.solve_ivp(odefunction,
			(self.t0, self.tf),
			self.x0,
			method=self.method,
			t_eval=tt,
			# events=event
			)
			
		return sol.t, sol.y.T
		
	def get_time_vector(self):
		return np.arange(self.t0, self.tf + self.dt, self.dt)
		
