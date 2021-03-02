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
pos_or_mat = np.zeros(12)
euler = np.zeros(3)
max_torque = 200
tool_length = 0.23

# connect and get handles
clientID, joint_handle, end_effector_handle = connect()

# set max torque
for i in range(6):
    vrep.simxSetJointForce(clientID,joint_handle[i],max_torque,vrep.simx_opmode_blocking)

# initialize UR5 parameters
d = np.array([0.089159,0,0,0.10915,0.09465,0.0823])
a = np.array([0,0.425,0.39225,0,0,0])
alpha = np.array([0,-PI/2,0,0,PI/2,-PI/2])

# theoretical result
def Forward_kinematics(deg1,deg2,deg3,deg4,deg5,deg6):
    # convert from deg to rad and wrap
    theta = np.array([deg2rad(deg1),deg2rad(deg2),deg2rad(deg3),deg2rad(deg4),deg2rad(deg5),deg2rad(deg6)])
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

def show_dummy(T):
    # Extract rotation and translation
    rotation_mat = T[0:3,0:3]
    translation_mat = T[0:3,3]
    print('translation_mat: ')
    print(translation_mat)
    # matrix to euler
    euler = rotm2euler(T)
    # get dummy handle
    status, dummy_handle = vrep.simxGetObjectHandle(clientID, 'Dummy', vrep.simx_opmode_blocking)
    if status!= vrep.simx_return_ok:
    	raise Exception('Cannot get handle of dummy')
    time.sleep(1)
    # create dummy
    status = vrep.simxSetObjectPosition(clientID,dummy_handle,-1,translation_mat,vrep.simx_opmode_blocking)
    if status != vrep.simx_return_ok:
    	raise Exception('Cannot get position of dummy')
    status = vrep.simxSetObjectOrientation(clientID,dummy_handle,-1,euler,vrep.simx_opmode_blocking)
    if status != vrep.simx_return_ok:
    	raise Exception('Cannot get orientation of dummy')
    time.sleep(1)

# experimental vritification
def Move_to_joint_position(a0,a1,a2,a3,a4,a5):
    vrep.simxSetJointTargetPosition(clientID,joint_handle[0],deg2rad(a0),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[1],deg2rad(a1),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[2],deg2rad(a2),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[3],deg2rad(a3),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[4],deg2rad(a4),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[5],deg2rad(a5),vrep.simx_opmode_oneshot)
    time.sleep(2)

def Get_object_pos_ori_mat():
    _,end_pos = vrep.simxGetObjectPosition(clientID,end_effector_handle,-1,vrep.simx_opmode_blocking)
    _,end_ori = vrep.simxGetObjectOrientation(clientID,end_effector_handle,-1,vrep.simx_opmode_blocking)
    print('position in meters: ')
    print(end_pos)
    print('orientation in radians: ')
    print(end_ori)

# verify
Move_to_joint_position(90,30,60,-30,90,90)
Forward_kinematics(90,30,60,-30,90,90)
print('gripper pos and ori')
Get_object_pos_ori_mat()
print('Done2')

# stop simulation and close connections
disconnect()
