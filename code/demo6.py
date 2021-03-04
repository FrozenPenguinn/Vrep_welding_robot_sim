# testing
import numpy as np
import time
import math
import vrep
from toolbox import *

clientID, joint_handles, welding_torch_handle = connect()
joint_angles = [0.0,0.0,0.0,0.0,0.0,0.0]

status1, joint_angles[0] = vrep.simxGetJointPosition(clientID, joint_handles[0], vrep.simx_opmode_streaming)
status2, joint_angles[1] = vrep.simxGetJointPosition(clientID, joint_handles[1], vrep.simx_opmode_streaming)
status3, joint_angles[2] = vrep.simxGetJointPosition(clientID, joint_handles[2], vrep.simx_opmode_streaming)
status4, joint_angles[3] = vrep.simxGetJointPosition(clientID, joint_handles[3], vrep.simx_opmode_streaming)
status5, joint_angles[4] = vrep.simxGetJointPosition(clientID, joint_handles[4], vrep.simx_opmode_streaming)
status6, joint_angles[5] = vrep.simxGetJointPosition(clientID, joint_handles[5], vrep.simx_opmode_streaming)
# time.sleep(5)

while True:
    if (status1 & status2 & status3 & status4 & status5 & status6 == 1):
        print(joint_angles)
        deg1 = [90,0,0,0,0,0]
        move_joint_deg(deg1)
        print(joint_angles)
        time.sleep(3)
        print(joint_angles)
        print("demo 6 done !")
        break
    else:
        print("waiting")
        time.sleep(0.5)

disconnect()
