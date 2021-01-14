# import libraries:
import vrep
import time
import numpy as np
import math
from connection import *
from helper_functions import *
#from demo1 import Move_to_joint_position

# initialize
global clientID
clientID = 0
joint_handle = np.zeros(6, dtype=np.int)
joint_angle = np.zeros(6)
pos_or_mat = np.zeros((3,4))

# connect and get handles
clientID, joint_handle = Connect()

# initialize UR5 parameters
d = np.array([89.2,0,0,109.15,94.65,82.3])
a = np.array([0,-425,-392.25,0,0,0])
alpha = np.array([PI/2,0,0,PI/2,-PI/2,0])

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
    print(T)
    print('mdzz')
    # return
    return T

def Move_to_joint_position(a0,a1,a2,a3,a4,a5):
    vrep.simxSetJointTargetPosition(clientID,joint_handle[0],Deg2rad(a0),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[1],Deg2rad(a1),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[2],Deg2rad(a2),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[3],Deg2rad(a3),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[4],Deg2rad(a4),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[5],Deg2rad(a5),vrep.simx_opmode_oneshot)
    time.sleep(1)
#def Get_pos_mat(joint_handle):

# verify
print("Zeroth experimental result: ")
print(vrep.simxGetJointMatrix(clientID,joint_handle[5],vrep.simx_opmode_blocking))
print("Zeroth theoretical result: ")
Forward_kinematics(0,0,0,0,0,0)
time.sleep(1)




print("First theoretical result: ")
Forward_kinematics(90,90,-90,90,90,90)
print("First experimental result: ")
Move_to_joint_position(90,90,-90,90,90,90)
time.sleep(1)
print(vrep.simxGetJointMatrix(clientID,joint_handle[5],vrep.simx_opmode_blocking))
'''
pos_or_mat = simxGetJointMatrix(clientID,joint_handle[5],vrep.simx_opmode_blocking)
print(pos_or_mat)
'''


print("Second theoretical result: ")
Forward_kinematics(-90,45,90,135,90,90)
print("Second experimental result: ")
Move_to_joint_position(-90,45,90,135,90,90)
time.sleep(1)
print(vrep.simxGetJointMatrix(clientID,joint_handle[5],vrep.simx_opmode_blocking))
'''
pos_or_mat = simxGetJointMatrix(clientID,joint_handle[5],vrep.simx_opmode_blocking)
print(pos_or_mat)
'''

print('Done2')

# stop simulation and close connections
Disconnect(clientID)
