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

# connect and get handles
clientID, joint_handle = Connect()

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
    # combine
    T = T01*T12*T23*T34*T45*T56
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

def Exp_veri(a0,a1,a2,a3,a4,a5):
    print("Experimental result: ")
    Move_to_joint_position(a0,a1,a2,a3,a4,a5)
    _,pos_or_mat = vrep.simxGetJointMatrix(clientID,joint_handle[5],vrep.simx_opmode_blocking)
    matrix = np.array(pos_or_mat).reshape((3,4))
    print(matrix)

# verify
Forward_kinematics(-90,45,90,135,90,90)
Exp_veri(-90,45,90,135,90,90)
time.sleep(1)

Move_to_joint_position(0,0,0,0,0,90)
time.sleep(1)
Move_to_joint_position(0,0,0,0,0,-90)
time.sleep(1)
Move_to_joint_position(0,0,0,0,0,90)
time.sleep(1)
Move_to_joint_position(0,0,0,0,0,-90)
time.sleep(1)

print('Done2')

# stop simulation and close connections
Disconnect(clientID)
