# import libraries:
import vrep
import time
import numpy as np
import math
# from connection import *
from toolbox import *

# initialize
clientID = 0
joint_handle = np.zeros(6, dtype=np.int)
joint_angle = np.zeros(6)
max_torque = 150

# connect and get handles
clientID, joint_handle, end_effector_handle = connect()

# move joint
def Move_to_joint_position(a0,a1,a2,a3,a4,a5):
    vrep.simxSetJointTargetPosition(clientID,joint_handle[0],deg2rad(a0),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[1],deg2rad(a1),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[2],deg2rad(a2),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[3],deg2rad(a3),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[4],deg2rad(a4),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[5],deg2rad(a5),vrep.simx_opmode_oneshot)

#print(current_vector(end_effector_handle))

# This is main function
_, x = vrep.simxGetJointPosition(clientID, joint_handle[0], vrep.simx_opmode_blocking)
time.sleep(2)
print(0)
print(x)
Move_to_joint_position(90,90,-90,90,90,90)
time.sleep(2)
_, x = vrep.simxGetJointPosition(clientID, joint_handle[0], vrep.simx_opmode_blocking)
print(90)
print(x)
time.sleep(2)
Move_to_joint_position(-90,45,90,135,90,90)
time.sleep(2)
_, x = vrep.simxGetJointPosition(clientID, joint_handle[0], vrep.simx_opmode_blocking)
print(-90)
print(x)
Move_to_joint_position(0,0,0,0,0,0)
time.sleep(2)
_, x = vrep.simxGetJointPosition(clientID, joint_handle[0], vrep.simx_opmode_blocking)
print(0)
print(x)
print('Done1')

# stop simulation and close connections
disconnect()
