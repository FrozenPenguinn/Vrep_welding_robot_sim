# testing
import numpy as np
import time
import math
import vrep
from toolbox import *

goal = np.array([0.0,0.0,0.0,0.0,0.0,0.0])
# forward_kinematics(goal)

#forward_kinematics(goal)
#forward_kinematics(0.0,0.0,0.0,0.0,0.0,0.0)

connect()
pos_ori_mat_1 = np.matrix([[0,   1,   0,  -1.2235e-01],
                           [1,   0,   0,   0.7000e-00],
                           [0,   0,  -1,   0.0000e-02],
                           [0,   0,   0,   1         ]])
pos_ori_mat_2 = np.matrix([[0,   1,   0,  -1.2235e-01],
                           [1,   0,   0,   0.4000e-00],
                           [0,   0,  -1,   0.0000e-02],
                           [0,   0,   0,   1         ]])
pos_ori_mat_3 = np.matrix([[0,   1,   0,  -1.2235e-01],
                           [1,   0,   0,   0.5000e-00],
                           [0,   0,  -1,   0.0000e-01],
                           [0,   0,   0,   1         ]])
set_goal(pos_ori_mat_1)
#jacobian(goal)
inverse_kinematics(pos_ori_mat_1)


set_goal(pos_ori_mat_2)
lerp(pos_ori_mat_1,pos_ori_mat_2)
time.sleep(0.5)

set_goal(pos_ori_mat_3)
inverse_kinematics(pos_ori_mat_3)

draw_circle(pos_ori_mat_3, 2.0000e-01)

time.sleep(1)
print("demo 5 done!")
#disconnect()
