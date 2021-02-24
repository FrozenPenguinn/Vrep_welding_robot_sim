# testing
import numpy as np
import time
import math
import vrep
from toolbox import forward_kinematics, jacobian, inverse_kinematics, connect, disconnect

goal = np.array([0.0,0.0,0.0,0.0,0.0,0.0])
# forward_kinematics(goal)

#forward_kinematics(goal)
#forward_kinematics(0.0,0.0,0.0,0.0,0.0,0.0)

connect()

pos_ori_mat_1 = np.matrix([[0,   1,   0,   1.2235e-01],
                           [0,   0,   1,   0.6000e-00],
                           [1,   0,   0,   6.0000e-01],
                           [0,   0,   0,   1         ]])
#jacobian(goal)
inverse_kinematics(pos_ori_mat_1)

time.sleep(2)
print("demo 5 done!")
disconnect()
