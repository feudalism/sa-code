import numpy as np
import matplotlib.pyplot as plt

def update_belief(hallway, prior, z, z_prob):
    """
    z_prob: probability that the sensor reading is correct 
    
    Returns: posterior
    """
    scale = z_prob / (1. - z_prob)
    
    # given z, how likely is each position?
    likelihood = prior
    likelihood[hallway==z] *= scale
    
    return normalise(likelihood)
    
def normalise(data):
    return data / sum(data)

# belief that dog is at the nth position
prior = np.array([0.1] * 10)

# map of hallway
# 1 for doors, 0 for walls
hallway = np.array([1, 1, 0, 0 ,0, 0, 0, 0, 1, 0])

# if sensor outputs 1,
# we now believe that there's a 33.3% chance
#   of him being at door 0, door 1 and door 8 each
# this is an improvement compared to the previous prior
#   (higher strength of belief, and narrowing down of possibilities)
# multimodal categorical distribution
reading = 1 # door
posterior = update_belief(hallway, prior, z=reading, z_prob=.75)
print(posterior)

plt.bar(range(0,len(hallway)), posterior)
plt.ylim((0, 1))
plt.grid()
plt.show()


