# -*- coding: utf-8 -*-
# @created on : 2020/3/22 22:03
# @name       : mainBill.py
# @IDE        : PyCharm

# Import Libraries:
import vrep  # V-rep library
import sys
import time  # used to keep track of time
import numpy as np  # array library
import math
import socket
import cv2

port = 19999    #identify port number here for socket communication with vrep ,19900-19999
global persAngle
persAngle = 70  # identify maximum perspective angle of vision sensor. (degree)
#-------------------------------------------------
#socket communication with console. because i want to launch all the cars simultaneously
'''
IP = '127.0.0.1'
port_socket = 9999   #socket port for command
##初始化
try:
    client_sk = socket.socket()     # 连接服务端
    client_sk.connect((IP, port_socket))
except socket.error as msg:
    print(msg)
    sys.exit(1)
print(str(client_sk.recv(1024), encoding='utf-8'))   #连接成功，接收server的welcome
#客户端不断接收服务器发来的信息

while 1:
    #data=client_sk.recv(1024)
    #datad=data.decode('utf-8')
    #print(datad)
    if (client_sk.recv(1024)):
        break
client_sk.close()
'''

#---------------------------------------------
#begin the main1 code next:

# following is initializing:
# initialize communition with VREP
PI = math.pi  # pi=3.14..., constant
vrep.simxFinish(-1)  # just in case, close all opened connections
clientID = vrep.simxStart('127.0.0.1', port, True, True, 5000, 5)
if clientID != -1:  # check if client connection successful
    print("Connected to remote API server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')

# get handles of youbot and arms
arm_joint_handle = [1,1,1,1] #wheel joints handle
arm_joint_status = [1,1,1,1]
arm_joint_status[0], arm_joint_handle[0] = vrep.simxGetObjectHandle(clientID, 'youBotArmJoint0',vrep.simx_opmode_oneshot_wait)
arm_joint_status[1], arm_joint_handle[1] = vrep.simxGetObjectHandle(clientID, 'youBotArmJoint1',vrep.simx_opmode_oneshot_wait)
arm_joint_status[2], arm_joint_handle[2] = vrep.simxGetObjectHandle(clientID, 'youBotArmJoint2',vrep.simx_opmode_oneshot_wait)
arm_joint_status[3], arm_joint_handle[3] = vrep.simxGetObjectHandle(clientID, 'youBotArmJoint3',vrep.simx_opmode_oneshot_wait)
youBot_status, youBot_handle = vrep.simxGetObjectHandle(clientID, 'youBot',vrep.simx_opmode_oneshot_wait)
time.sleep(0.5)

# get initial arm angle (in radians)
current_arm_angle = [0,0,0,0]
for i in range(0,4):
    _, current_arm_angle[i] = vrep.simxGetJointPosition(clientID,arm_joint_handle[i],vrep.simx_opmode_blocking)
# convert to degress
for i in range(0,4):
    current_arm_angle[i] = current_arm_angle[i] * 180 / PI
# show
for i in range(0,4):
    print(current_arm_angle[i])

# get current joint angles (toolbox function)

# Move armJoint in absolute position (P system setting)
def arm_move_absolute(a0=current_arm_angle[0],a1=current_arm_angle[1],a2=current_arm_angle[2],a3=current_arm_angle[3]):
    vrep.simxSetJointPosition(clientID,arm_joint_handle[0],a0*PI/180,vrep.simx_opmode_streaming)
    vrep.simxSetJointPosition(clientID,arm_joint_handle[1],a1*PI/180,vrep.simx_opmode_streaming)
    vrep.simxSetJointPosition(clientID,arm_joint_handle[2],a2*PI/180,vrep.simx_opmode_streaming)
    vrep.simxSetJointPosition(clientID,arm_joint_handle[3],a3*PI/180,vrep.simx_opmode_streaming)
    time.sleep(0.5)
    print('Done')

def arm_move_relative(a0,a1,a2,a3):
    current_arm_angle = [0,0,0,0]


# arm_move_absolute demo on joint0
def demo_move_1():
    arm_move_absolute(a0=0)
    arm_move_absolute(a0=90)
    arm_move_absolute(a0=180)
    arm_move_absolute(a0=-90)
    arm_move_absolute(a0=-180)
    arm_move_absolute(a0=0)

# This is main function
if (arm_joint_status[0] == 0 and arm_joint_status[1] == 0 and arm_joint_status[2] == 0 and arm_joint_status[3] == 0):
    demo_move_1();
