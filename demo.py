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
import matplotlib.pyplot as plt  # used for image plotting
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
wheelJoints = [1,1,1,1] #wheel joints handle
wheelJoints[0] = vrep.simxGetObjectHandle(clientID, 'rollingJoint_fl',vrep.simx_opmode_oneshot_wait)
wheelJoints[1] = vrep.simxGetObjectHandle(clientID, 'rollingJoint_rl',vrep.simx_opmode_oneshot_wait)
wheelJoints[2] = vrep.simxGetObjectHandle(clientID, 'rollingJoint_rr',vrep.simx_opmode_oneshot_wait)
wheelJoints[3] = vrep.simxGetObjectHandle(clientID, 'rollingJoint_fr',vrep.simx_opmode_oneshot_wait)
wheelJoints[0] = wheelJoints[0][1]   #because the wheelJoints[0] obtained above was a array made up by two numbers!
wheelJoints[1] = wheelJoints[1][1]
wheelJoints[2] = wheelJoints[2][1]
wheelJoints[3] = wheelJoints[3][1]
youBot = vrep.simxGetObjectHandle(clientID, 'youBot',vrep.simx_opmode_oneshot_wait)
youBot = youBot[1]
errorCode,visionSensorHandle = vrep.simxGetObjectHandle(clientID,'Vision_sensor',vrep.simx_opmode_oneshot_wait)

errprCode,resolution,rawimage = vrep.simxGetVisionSensorImage(clientID,visionSensorHandle,0,vrep.simx_opmode_streaming)
time.sleep(0.5)    #initialize the visionsensor


def actuate_car(forwBackVel,leftRightVel,rotVel):    #set four wheel speed according to vx,vy,w
    v0 = (-forwBackVel + leftRightVel + 0.38655 * rotVel) / r
    v1 = (-forwBackVel - leftRightVel + 0.38655 * rotVel) / r
    v2 = (-forwBackVel + leftRightVel - 0.38655 * rotVel) / r
    v3 = (-forwBackVel - leftRightVel - 0.38655 * rotVel) / r
    vrep.simxSetJointTargetVelocity(clientID, wheelJoints[0], v0 , vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetVelocity(clientID, wheelJoints[1], v1 , vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetVelocity(clientID, wheelJoints[2], v2 , vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetVelocity(clientID, wheelJoints[3], v3 , vrep.simx_opmode_streaming)
    time.sleep(0.2)  # loop executes once every 0.2 seconds (= 5 Hz)

def readVisionSensor():
    global resolution
    errprCode, resolution, rawimage = vrep.simxGetVisionSensorImage(clientID, visionSensorHandle, 0, vrep.simx_opmode_buffer)
    sensorImage = []
    sensorImage = np.array(rawimage, dtype=np.uint8)    #transform the raw image to uint8
    sensorImage.resize([resolution[1], resolution[0], 3])        # Process the image to the format (256,128,3)
    cv2.flip(sensorImage, 0, sensorImage)  # image upside down
    image = sensorImage
    return image
image = readVisionSensor()

#opencv ROI and establish KCFtracker
cv2.namedWindow("tracking")
tracker = cv2.MultiTracker_create()
bbox1 = cv2.selectROI('tracking', image)
ok = tracker.add(cv2.TrackerKCF_create(), image, bbox1)
#bbox2 = cv2.selectROI('tracking', image)
#ok = tracker.add(cv2.TrackerKCF_create(), image, bbox2)
#bbox3 = cv2.selectROI('tracking', image)
#ok = tracker.add(cv2.TrackerKCF_create(), image, bbox3)

# P controller for rotVel:
outlast = 0
errorlast = 0
N = 1.2
def guidance(error):
    global outlast,errorlast
    out = outlast + N * (error - errorlast)
    outlast = out
    errorlast = error
    return out * PI/180

forwBackVel = 0 # m/s
leftRightVel = 0  # m/s
rotVel =  0   #rotVel = 10 * PI/ 180  #rad/s
r = 0.05      #wheel radium (meters)


t= time.time()

while (time.time() - t) < 180:  #loop for 180 seconds
    # capture image and Process the image to the format (64,64,3)
    image = readVisionSensor()
    ok, boxes = tracker.update(image)
    target_center_x = []
    target_center_y = []
    sight_angle = []
    speed_thata = 1
    for newbox in boxes:
        p1 = (int(newbox[0]), int(newbox[1]))    #rectangle left up (x,y)
        p2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))  #rectangle right down (x+w,y+h)
        cv2.rectangle(image, p1, p2, (200, 0, 0))
        centerx = (int(newbox[0]) + int(newbox[2]) // 2)
        centery = (int(newbox[1]) + int(newbox[3]) // 2)
        target_center_x.append(centerx)
        target_center_y.append(centery)
        theta1 = (math.atan(2.0 * (centerx - resolution[0] / 2) * math.tan(persAngle * PI / 360.0) / resolution[0])) * 180 / PI  # sight angle(degree)
        sight_angle.append(theta1)   #sight angle -- left minus;right plus
        speed_thata = min(speed_thata, 1 + (centery - resolution[1] / 2) / (resolution[1] / 2))
    print('error angle is: ',sight_angle)
    print('error x distance is: ',target_center_x)

    cv2.imshow('tracking', image)

    forwBackVel = 0.12 * speed_thata  # m/s
    leftRightVel = 0  # m/s
    rotVel = guidance(-sight_angle[0]) # rotVel = 10 * PI/ 180  #rad/s
    print('rotVel is: ',rotVel*180/PI)
    print('speed is: ', forwBackVel)
    print()
    actuate_car(forwBackVel, leftRightVel, rotVel)

    k = cv2.waitKey(1)
    if k == 27: break  # esc pressed


# finish and shut down the car
actuate_car(0, 0, 0)
