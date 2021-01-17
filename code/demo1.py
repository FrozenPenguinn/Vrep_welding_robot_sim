# import libraries:
import vrep
import time
import numpy as np
import math
from connection import *
from helper_functions import *

# initialize
clientID = 0
joint_handle = np.zeros(6, dtype=np.int)
joint_angle = np.zeros(6)
max_torque = 200

# connect and get handles
clientID, joint_handle, _ = Connect()

# get initial arm angle
for i in range(6):
    _, joint_angle[i] = vrep.simxGetJointPosition(clientID,joint_handle[i],vrep.simx_opmode_blocking)
    joint_angle[i] = Deg2rad(joint_angle[i])

# set max torque
for i in range(6):
    vrep.simxSetJointForce(clientID,joint_handle[i],max_torque,vrep.simx_opmode_blocking)

# move joint
def Move_to_joint_position(a0,a1,a2,a3,a4,a5):
    vrep.simxSetJointTargetPosition(clientID,joint_handle[0],Deg2rad(a0),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[1],Deg2rad(a1),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[2],Deg2rad(a2),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[3],Deg2rad(a3),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[4],Deg2rad(a4),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[5],Deg2rad(a5),vrep.simx_opmode_oneshot)

# This is main function
Move_to_joint_position(90,90,90,90,90,90)
time.sleep(3)
Move_to_joint_position(90,135,225,180,180,350)
time.sleep(5)
Move_to_joint_position(180,180,180,180,180,180)
time.sleep(3)
print('Done1')

# stop simulation and close connections
Disconnect(clientID)
