# import libraries:
import vrep
import time
import numpy as np
import math
from connection import *
from helper_functions import *
#from demo1 import Move_to_joint_position

# initialize
clientID = 0
joint_handle = np.zeros(6, dtype=np.int)
joint_angle = np.zeros(6)

# connect and get handles
clientID, joint_handle = Connect()

# initialize UR5 parameters
d = np.array([89.2,0,0,109.15,94.65,82.3])
a = np.array([0,-425,-392.25,0,0,0])
alpha = np.array([PI/2,0,0,PI/2,-PI/2,0])

def forward_kinematics(deg1,deg2,deg3,deg4,deg5,deg6):
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

# verify
print("First theoretical result: ")
forward_kinematics(90,90,-90,90,90,90)
print("First experimental result: ")
#Move_to_joint_position(90,90,-90,90,90,90)

print("Second theoretical result: ")
forward_kinematics(-90,45,90,135,90,90)
print("Second experimental result: ")
#Move_to_joint_position(-90,45,90,135,90,90)

print('Done')

# stop simulation and close connections
Disconnect(clientID)
