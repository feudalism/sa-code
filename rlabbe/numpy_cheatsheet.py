import numpy as np

# Array creation (type: numpy.ndarray)
x = np.array([1, 2, 3])
x = np.array( [ [1, 2, 3],
                [4, 5, 6] ])
x = np.asarray(existing_python_list) # or existing ndarray
                
x = np.zeros(7)
x = np.zeros((3, 2))
x = np.eye(3)

np.arange(0, 2, 0.1)
np.linspace(0, 2, 20)
                
x_transpose = x.T
x_inv = np.linalg.inv(x)
                
# Element type
x = np.array([1, 2, 3], dtype=float)

# Slicing
# zero-indexing
# all rows and columns using :
x[:, 0]
x[0, :]

x[0, 1:]
x[0, -2:]

# Multiplication
# Element wise
x * x

# Matrix mult
np.dot(x, x)
np.dpt(x, 3.)
x.dot(x)
x @ x # both must be matrices