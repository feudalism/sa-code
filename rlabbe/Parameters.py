# Parameters.py

class Parameters(object):
	"""Structure to store parameters as attributes."""
	
	def append(self, params):
		new_attributes = dict(params)
		self.__dict__.update(new_attributes)
		
	def __iter__(self):
		""" Allow object to be iterable """
		for attr, value in self.__dict__.items():
			yield attr, value
            
def set_sim_parameters(t0, tf, dt, x0):
	sim_params = Parameters()
	sim_params.t0 = t0
	sim_params.tf = tf
	sim_params.dt = dt
	sim_params.x0 = x0
	return sim_params