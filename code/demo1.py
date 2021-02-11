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
max_torque = 150

# connect and get handles
clientID, joint_handle, _ = Connect()

# move joint
def Move_to_joint_position(a0,a1,a2,a3,a4,a5):
    vrep.simxSetJointTargetPosition(clientID,joint_handle[0],Deg2rad(a0),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[1],Deg2rad(a1),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[2],Deg2rad(a2),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[3],Deg2rad(a3),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[4],Deg2rad(a4),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[5],Deg2rad(a5),vrep.simx_opmode_oneshot)

# This is main function
Move_to_joint_position(90,90,-90,90,90,90)
time.sleep(1)
Move_to_joint_position(-90,45,90,135,90,90)
time.sleep(1)
Move_to_joint_position(0,0,0,0,0,0)
time.sleep(1)
print('Done1')

# stop simulation and close connections
Disconnect(clientID)
