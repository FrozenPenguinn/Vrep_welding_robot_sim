# testing
import numpy as np
import math
import vrep
from helper_functions import forward_kinematics

goal = np.array([0,0,0,0,0,0])
forward_kinematics(goal)
