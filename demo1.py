# Import Libraries:
import vrep
import time
import numpy as np
import math

port = 19999    #identify port number here for socket communication with vrep ,19900-19999
PI = math.pi

# following is initializing:
# initialize communition with VREP
vrep.simxFinish(-1)  # just in case, close all opened connections
clientID = vrep.simxStart('127.0.0.1', port, True, True, 5000, 5)
if clientID != -1:  # check if client connection successful
    print("Connected to remote API server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')

# get handles of youbot and arms

arm_joint_handle = [1,1,1,1,1,1] #wheel joints handle
arm_joint_status = [1,1,1,1,1,1]
arm_joint_status[0], arm_joint_handle[0] = vrep.simxGetObjectHandle(clientID, 'UR10_joint1',vrep.simx_opmode_blocking)
arm_joint_status[1], arm_joint_handle[1] = vrep.simxGetObjectHandle(clientID, 'UR10_joint2',vrep.simx_opmode_blocking)
arm_joint_status[2], arm_joint_handle[2] = vrep.simxGetObjectHandle(clientID, 'UR10_joint3',vrep.simx_opmode_blocking)
arm_joint_status[3], arm_joint_handle[3] = vrep.simxGetObjectHandle(clientID, 'UR10_joint4',vrep.simx_opmode_blocking)
arm_joint_status[4], arm_joint_handle[4] = vrep.simxGetObjectHandle(clientID, 'UR10_joint5',vrep.simx_opmode_blocking)
arm_joint_status[5], arm_joint_handle[5] = vrep.simxGetObjectHandle(clientID, 'UR10_joint6',vrep.simx_opmode_blocking)
UR10_status, UR10_handle = vrep.simxGetObjectHandle(clientID, 'UR10',vrep.simx_opmode_blocking)
print('Finish 1')

# initialize joint angle
current_arm_angle = [0,0,0,0,0,0]
# get initial arm angle (in radians)
for i in range(0,6):
    _, current_arm_angle[i] = vrep.simxGetJointPosition(clientID,arm_joint_handle[i],vrep.simx_opmode_blocking)
    current_arm_angle[i] = current_arm_angle[i] * 180 / PI
    print(current_arm_angle[i])

# move joint
def move_to_joint_position(a0,a1,a2,a3,a4,a5):
    vrep.simxSetJointTargetPosition(clientID,arm_joint_handle[0],a0*PI/180,vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,arm_joint_handle[1],a1*PI/180,vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,arm_joint_handle[2],a2*PI/180,vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,arm_joint_handle[3],a3*PI/180,vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,arm_joint_handle[4],a4*PI/180,vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,arm_joint_handle[5],a5*PI/180,vrep.simx_opmode_oneshot)
    time.sleep(1)

# This is main function
move_to_joint_position(90,90,-90,90,90,90)
move_to_joint_position(-90,45,90,135,90,90)
move_to_joint_position(0,0,0,0,0,0)
print('Done')
