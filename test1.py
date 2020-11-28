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

#get handles of four wheels and vision sensor
armJoints = [1,1,1,1] #wheel joints handle
ret1, armJoints[0] = vrep.simxGetObjectHandle(clientID, 'youBotArmJoint0',vrep.simx_opmode_oneshot_wait)
ret2, armJoints[1] = vrep.simxGetObjectHandle(clientID, 'youBotArmJoint1',vrep.simx_opmode_oneshot_wait)
ret3, armJoints[2] = vrep.simxGetObjectHandle(clientID, 'youBotArmJoint2',vrep.simx_opmode_oneshot_wait)
ret4, armJoints[3] = vrep.simxGetObjectHandle(clientID, 'youBotArmJoint3',vrep.simx_opmode_oneshot_wait)
youBot = vrep.simxGetObjectHandle(clientID, 'youBot',vrep.simx_opmode_oneshot_wait)
youBot = youBot[1]
time.sleep(0.5)    #initialize the visionsensor

# Move armJoint
def arm_move(a1,a2,a3,a4):
    vrep.simxSetJointPosition(clientID,armJoints[0],a1*PI/180,vrep.simx_opmode_streaming)
    time.sleep(0.5)
    vrep.simxSetJointPosition(clientID,armJoints[1],a2*PI/180,vrep.simx_opmode_streaming)
    time.sleep(0.5)
    vrep.simxSetJointPosition(clientID,armJoints[2],a3*PI/180,vrep.simx_opmode_streaming)
    time.sleep(0.5)
    vrep.simxSetJointPosition(clientID,armJoints[3],a4*PI/180,vrep.simx_opmode_streaming)
    time.sleep(0.5)
    print('Done')
    #simSetJointPosition(armJoints[1],90*PI/180)
    #simSetJointPosition(armJoints[2],90*PI/180)
    #simSetJointPosition(armJoints[3],90*PI/180)
# def constant_arm_move(a1,a2,a3,a4):
#     for ()

# def smooth_arm_move():


t= time.time()

if (ret1 == 0 and ret2 == 0 and ret3 == 0 and ret4 == 0):
    arm_move(0,0,0,0)
    time.sleep(0.5)
    arm_move(90,90,90,90)
    time.sleep(0.5)
    arm_move(0,0,0,0)
    time.sleep(0.5)
    arm_move(90,90,90,90)
    time.sleep(0.5)
    arm_move(0,0,0,0)
    time.sleep(0.5)
    arm_move(90,90,90,90)
    time.sleep(0.5)
    arm_move(0,0,0,0)
    time.sleep(0.5)
    arm_move(90,90,90,90)
    # if k == 27: break  # esc pressed
