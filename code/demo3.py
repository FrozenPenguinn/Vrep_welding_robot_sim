# import libraries:
import vrep
import time
import numpy as np
import math
from connection import *
from helper_functions import *

# connect and get handles
clientID, joint_handle, end_effector_handle = Connect()

# initialize
current_angles = np.zeros(6)
goal_angles = np.zeros(6)

# Solving Ax=b
def inverse_kinematics(pos_ori_mat):
    # Find error vector
    # current PR_mat
    for i in range(0,6):
        current_angles[i] = simxGetJointPosition(clientID, joint_handle[i], vrep.simx_opmode_blocking)
    current_T = Forward_kinematics(current_angles[0],current_angles[1],current_angles[2],current_angles[3],current_angles[4],current_angles[5])
    current_P = current_T[0:3,3]
    current_R = rotm2euler(current_T)
    current_PR_mat = np.stack(current_P,current_R)
    current_PR_mat = current_PR_mat.shape(6,1)
    # goal PR_mat
    goal_P = pos_ori_mat[0:3,3]
    goal_R = rotm2euler(pos_ori_mat)
    goal_PR_mat = np.stack(goal_P,goal_R)
    goal_PR_mat = goal_PR_mat.shape(6,1)
    # error vector
    error_vector = goal_PR_mat - current_PR_mat

    # Find Jacobian matrix
    # Already have PR0, find PR1, using numerical method, not analytical
    current_T = Forward_kinematics(current_angles[0],current_angles[1],current_angles[2],current_angles[3],current_angles[4],current_angles[5])
    

    # Solve Ax=b
    return

def move_dummy(x,y,z,rx,ry,rz):
    position = np.array([x,y,z])
    orientation = np.array([rx,ry,rz])
    # get dummy handle
    status, dummy_handle = vrep.simxGetObjectHandle(clientID, 'Dummy', vrep.simx_opmode_blocking)
    if status!= vrep.simx_return_ok:
    	raise Exception('Cannot get handle of dummy')
    time.sleep(1)
    # move dummy
    status = vrep.simxSetObjectPosition(clientID,dummy_handle,-1,position,vrep.simx_opmode_blocking)
    if status != vrep.simx_return_ok:
    	raise Exception('Cannot get position of dummy')
    status = vrep.simxSetObjectOrientation(clientID,dummy_handle,-1,orientation,vrep.simx_opmode_blocking)
    if status != vrep.simx_return_ok:
    	raise Exception('Cannot get orientation of dummy')
    time.sleep(1)

def Forward_kinematics(deg1,deg2,deg3,deg4,deg5,deg6):
    # convert from deg to rad and wrap
    theta = np.array([Deg2rad(deg1),Deg2rad(deg2),Deg2rad(deg3),Deg2rad(deg4),Deg2rad(deg5),Deg2rad(deg6)])
    # calculate respective transformation matrix
    Tmat_01 = T01(theta[0])
    Tmat_12 = T12(theta[1])
    Tmat_23 = T23(theta[2])
    Tmat_34 = T34(theta[3])
    Tmat_45 = T45(theta[4])
    Tmat_56 = T56(theta[5])
    Tmat_6t = T6t(tool_length)
    # combine
    T = Tmat_01*Tmat_12*Tmat_23*Tmat_34*Tmat_45*Tmat_56*Tmat_6t
    # cut
    T_reduced = T[0:3]
    show_dummy(T_reduced)
    # print
    print("Theoretical result: ")
    print(T)
    print('euler of T: ')
    print(rotm2euler(T_reduced))
    # return
    return T

move_dummy(1,1,1,0,0,0)
move_dummy(1,-1,1,0,0,0)

print('Done3')

# stop simulation and close connections
Disconnect(clientID)
