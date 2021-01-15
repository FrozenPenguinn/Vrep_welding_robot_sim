# import libraries:
import vrep
import time
import numpy as np
import numpy.matlib
import math
from connection import *
from helper_functions import *
#from demo1 import Move_to_joint_position

# initialize
clientID = 0
joint_handle = np.zeros(6, dtype=np.int)
joint_angle = np.zeros(6)
pos_or_mat = np.zeros(12)
euler = np.zeros(3)
max_torque = 200
tool_length = -0.1173925

# connect and get handles
clientID, joint_handle, end_effector_handle = Connect()

# set max torque
for i in range(6):
    vrep.simxSetJointForce(clientID,joint_handle[i],max_torque,vrep.simx_opmode_blocking)

# initialize UR5 parameters
d = np.array([0.0892,0,0,0.10915,0.09465,0.0823])
a = np.array([0,-0.425,-0.39225,0,0,0])
alpha = np.array([PI/2,0,0,PI/2,-PI/2,0])

def show_dummy(T):
    # Extract rotation and translation
    rotation_mat = T[0:3,0:3]
    translation_mat = T[0:3,3]
    # matrix to euler
    euler = rot2euler(rotation_mat)
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

# theoretical result
def Forward_kinematics(deg1,deg2,deg3,deg4,deg5,deg6):
    # convert from deg to rad and wrap
    theta = np.array([Deg2rad(deg1),Deg2rad(deg2),Deg2rad(deg3),Deg2rad(deg4),Deg2rad(deg5),Deg2rad(deg6)])
    # calculate respective transformation matrix
    T01 = T_mat(theta[0],d[0],a[0],alpha[0])
    T12 = T_mat(theta[1],d[1],a[1],alpha[1])
    T23 = T_mat(theta[2],d[2],a[2],alpha[2])
    T34 = T_mat(theta[3],d[3],a[3],alpha[3])
    T45 = T_mat(theta[4],d[4],a[4],alpha[4])
    T56 = T_mat(theta[5],d[5],a[5],alpha[5])
    T6t = T_mat(0,0,tool_length,0)
    # combine
    T = T01*T12*T23*T34*T45*T56*T6t
    # cut
    T = T[0:3]
    show_dummy(T)
    # print
    print("Theoretical result: ")
    print(T[0:3])
    # return
    return T

# experimental vritification
def Move_to_joint_position(a0,a1,a2,a3,a4,a5):
    vrep.simxSetJointTargetPosition(clientID,joint_handle[0],Deg2rad(a0),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[1],Deg2rad(a1),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[2],Deg2rad(a2),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[3],Deg2rad(a3),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[4],Deg2rad(a4),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[5],Deg2rad(a5),vrep.simx_opmode_oneshot)
    time.sleep(2)

def Get_object_pos_ori_mat(clientID,end_effector_handle):
    print("Experimental result: ")
    Move_to_joint_position(a0,a1,a2,a3,a4,a5)
    _,end_pos = vrep.simxGetObjectPosition(clientID,joint_handle[5],vrep.simx_opmode_blocking)
    _,pos_or_mat = vrep.simxGetJointMatrix(clientID,joint_handle[5],vrep.simx_opmode_blocking)
    matrix = np.array(pos_or_mat).reshape((3,4))
    print(matrix)

# verify
Forward_kinematics(0,0,0,0,0,0)
#Exp_veri(0,0,0,0,0,0)
print(vrep.simxGetObjectPosition(clientID,end_effector_handle,-1,vrep.simx_opmode_blocking))
print(vrep.simxGetObjectOrientation(clientID,end_effector_handle,-1,vrep.simx_opmode_blocking))

time.sleep(1)

print('Done2')

# stop simulation and close connections
Disconnect(clientID)
