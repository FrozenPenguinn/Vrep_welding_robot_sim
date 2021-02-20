# testing
import numpy as np
import math
import vrep
from toolbox import forward_kinematics, jacobian

goal = np.array([0,0,0,0,0,0])
# forward_kinematics(goal)

jacobian(goal)
