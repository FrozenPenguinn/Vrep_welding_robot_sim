import cv2
import numpy as np
import math
import time
import vrep
from tsp_solver.greedy import solve_tsp
from time import sleep
from math import pi, cos, sin, atan2, sqrt, acos
from numpy.linalg import norm

# arm parameters
clientID = 0
joint_handles = np.zeros(4, dtype = int)
PI = pi
# base
r1 = 0.063247
h1 = 0.10601
# link1
r2 = 0.09881
h2 = 0.09198
l2 = 0.135 # 135mm
theta2 = 0.749624 # 42.95
origin2 = 101.0 / 180 * pi # 101.00
# link2
r3 = 0.15263
h3 = -0.07486
l3 = 0.179825 # 170mm
theta3 = -0.456013 # -26.128
origin3 = 34.0 / 180 * pi # 34.00
# link3 (tool)
r4 = 0.035278
h4 = -0.029195
# steper motor plans
motion_plan = np.zeros(3*3500).reshape(3500,3)
change_plan = motion_plan.copy()
motion_length = 0
steps_count = 0
rad1_remainder = 0
rad2_remainder = 0
rad3_remainder = 0

def distance(x1, y1, x2, y2):
    dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return dist

def inverse_kinematics(x, y, z):
    global steps_count
    steps_count += 1
    # solving for theta 1
    rad1 = round(atan2(y, x), 4)
    # solving for theta 2 and 3
    r = sqrt(pow(x, 2) + pow(y, 2)) - r1 - r4
    h = z - h1 - h4
    #print(r)
    #print(h)
    beta = atan2(h, r)
    phi = acos((pow(r, 2) + pow(h, 2) + pow(l2, 2) - pow(l3, 2))/(2 * l2 * sqrt(pow(r, 2) + pow(h, 2))))
    rad2 = beta + phi
    rad3 = atan2(h - l2 * sin(rad2), r - l2 * cos(rad2))
    #print("rad3 = " + str(rad3))
    # solving for theta 4
    rad4 = - (rad2 + rad3)
    # correction with initial angles
    rad2 = round(rad2 - theta2, 4)
    rad3 = round(rad3 - theta3 - rad2, 4)
    #print("rad3 = " + str(rad3))
    return rad1, rad2, rad3

def deg2rad(deg):
    return deg * PI / 180

def rad2deg(rad):
    return rad * 180 / PI

def set_joints_rad(r0, r1, r2):
    vrep.simxSetJointTargetPosition(clientID, joint_handles[0], r0, vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID, joint_handles[1], r1, vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID, joint_handles[2], r2, vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID, joint_handles[3], -r1-r2, vrep.simx_opmode_oneshot)

def locate_pen(x, y, z):
    #print(x,y,z)
    rad1, rad2, rad3 = inverse_kinematics(x + 0.27, y, z)
    record_rads(rad1, rad2, rad3)
    #set_joints_rad(rad1, rad2, rad3)

def image_processing_optimization(img = 'Images/write.png', factor = 0.5, size = 350):
    print("Program running")
    rgb_img = cv2.imread(img)
    x, y, _ = rgb_img.shape
    max_value = max(x, y)

    desired_size = [size, size]
    desired =   [desired_size[0]*(y/max_value),
                desired_size[1]*(x/max_value),
                3]

    scale = [desired[0]/y,
            desired[1]/x]

    rgb_img = cv2.resize(rgb_img,
                        None,
                        fx=scale[0],
                        fy=scale[1],
                        interpolation = cv2.INTER_CUBIC)

    gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray_img, 0, 255, apertureSize = 3)
    #cv2.imshow('Image', edges)
    print("Image Processed")

    new_x, new_y, _ = rgb_img.shape
    edges = edges.tolist()

    point_x=[]
    point_y=[]

    for row in range(1, new_y):
        for column in range(1, new_x):
            if edges[column][row] == 255:
                point_x.append(row)
                point_y.append(column)

    points = list(zip(point_x, point_y))
    r  = [[0 for x in range(len(point_x))] for y in range(len(point_x))]

    print(str(len(point_x))+" Points Obtained")

    for p1 in range(1,len(point_x)):
        for p2 in range(1,len(point_x)):
            x1, y1= points[p1]
            x2, y2= points[p2]
            r[p1][p2]=distance(x1,y1,x2,y2)

    print("Distances calculated")

    #TSP - library
    print("Solving TSP")
    path = solve_tsp(r)
    print("TSP Done")

    np_points = np.array(points)
    np_points = np_points*factor
    points = np_points.tolist()

    return factor, path, points, new_x, new_y

def connect():
    global clientID
    # just in case, stop all prior connection
    vrep.simxFinish(-1)
    # connect to vrep server
    clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
    if clientID != -1:  # check if client connection successful
        print("Connected successful")
    else:
        raise Exception("Failed to connect")
    # start simulation
    vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot)
    # get handles
    res, joint_handles[0] = vrep.simxGetObjectHandle(clientID, 'Robot_joint1', vrep.simx_opmode_blocking)
    if res != vrep.simx_return_ok:
        raise Exception("Cannot get handle of first joint")
    res, joint_handles[1] = vrep.simxGetObjectHandle(clientID, 'Robot_joint2', vrep.simx_opmode_blocking)
    if res != vrep.simx_return_ok:
        raise Exception("Cannot get handle of second joint")
    res, joint_handles[2] = vrep.simxGetObjectHandle(clientID, 'Robot_joint3', vrep.simx_opmode_blocking)
    if res != vrep.simx_return_ok:
        raise Exception("Cannot get handle of third joint")
    res, joint_handles[3] = vrep.simxGetObjectHandle(clientID, 'Robot_joint4', vrep.simx_opmode_blocking)
    if res != vrep.simx_return_ok:
        raise Exception("Cannot get handle of fourth joint")
    # return
    return clientID, joint_handles

def disconnect():
    # stop simulation
    vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot)
    # make sure StopSimulation arrives
    vrep.simxGetPingTime(clientID)
    # disconnect from vrep server
    vrep.simxFinish(clientID)

def draw_VREP(factor, path, points, Z_draw, x, y):
    # Start VREP connection
    clientID, joint_handles = connect()

    print("Drawing Optimizated image")
    destination_points = np.array([0.294, 0.026, 0])
    rad1, rad2, rad3 = inverse_kinematics(destination_points[0], destination_points[1], destination_points[2])
    seperate([0,origin2-theta2,origin3-theta3-(origin2-theta2)],[0,0,0])
    seperate([0,0,0],[rad1, rad2, rad3])
    #locate_pen(0, 0, Z_draw+0.1)
    #cv2.waitKey(2)

    img_result = np.zeros((x*factor, y*factor, 3), np.uint8)
    for each in range(1,(len(path))-1):
        x1, y1 = points[path[each]]
        x2, y2 = points[path[each+1]]
        if distance(x1, y1, x2, y2) <= 2:
            locate_pen(y1/1000, x1/1000, Z_draw)
            #time.sleep(0.01)
            # Draw the progress on an external canvas
            cv2.line(img_result,
                    tuple(points[path[each]]),
                    tuple(points[path[each+1]]),
                    (255, 0, 0),
                    1)
            cv2.imshow('Optimized', img_result)
            #cv2.waitKey(1)
            locate_pen(y2/1000, x2/1000, Z_draw)
            #time.sleep(0.01)
            #cv2.waitKey(1)
        else:
            print(x1,y1)
            print(x2,y2)
            #time.sleep(0.01)
            locate_pen(y1/1000, x1/1000, Z_draw+0.002)
            start_rad1, start_rad2, start_rad3 = inverse_kinematics(0.27+y1/1000, x1/1000, Z_draw+0.002)
            end_rad1, end_rad2, end_rad3 = inverse_kinematics(0.27+y2/1000, x2/1000, Z_draw+0.002)
            seperate([start_rad1, start_rad2, start_rad3],[end_rad1, end_rad2, end_rad3])
            #locate_pen(y2/1000, x2/1000, Z_draw+0.002)
            #time.sleep(0.05)

    # Go to the initial position
    locate_pen(0.017, 0.191, Z_draw+0.02)
    time.sleep(1)
    print("Draw finished")

# record joint rads
def record_rads(rad1, rad2, rad3):
    global motion_plan, motion_length
    print(motion_length)
    motion_plan[motion_length][0] = rad1
    motion_plan[motion_length][1] = rad2
    motion_plan[motion_length][2] = rad3
    motion_length += 1

# reset
def seperate(start_rad, end_rad):
    dif = [abs(end_rad[0]-start_rad[0]), abs(end_rad[1]-start_rad[1]), abs(end_rad[2]-start_rad[2])]
    max_dif = max(dif)
    speed = 2 * (3.0 * PI) / (20 * 180) # 10 deg per second
    N = int((max_dif/speed)+1)
    #print("N = " + str(N))
    drad1 = (end_rad[1] - start_rad[1])/N
    drad2 = (end_rad[2] - start_rad[2])/N
    for i in range(1,N+1):
        record_rads(end_rad[0], start_rad[1] + drad1 * i, start_rad[2] + drad2 * i)

def trans2stepcode(motion_plan):
    global rad1_remainder, rad2_remainder, rad3_remainder
    for i in range(0,motion_length):
        motion_plan[i][0] = round(rad2deg(motion_plan[i][0]),4)
        motion_plan[i][1] = round(rad2deg(motion_plan[i][1]),4)
        motion_plan[i][2] = round(rad2deg(motion_plan[i][2]),4)
        #rad1_remainder += (motion_plan[i][0] % 0.01)
        #rad2_remainder += (motion_plan[i][1] % 0.01)
        #rad3_remainder += (motion_plan[i][2] % 0.01)
        #motion_plan[i][0] = motion_plan[i][0] + (rad1_remainder//0.01) * 100
        #motion_plan[i][1] = motion_plan[i][1] + (rad2_remainder//0.01) * 100
        #motion_plan[i][2] = motion_plan[i][2] + (rad3_remainder//0.01) * 100
        #rad1_remainder -= (rad1_remainder//0.01) * 100
        #rad2_remainder -= (rad2_remainder//0.01) * 100
        #rad2_remainder -= (rad3_remainder//0.01) * 100
        #print(motion_plan[i])
    # change_plan
    for i in range(0,motion_length):
        change_plan[i+1][0] = (motion_plan[i+1][0] - motion_plan[i][0])
        change_plan[i+1][1] = -(motion_plan[i+1][1] - motion_plan[i][1])
        change_plan[i+1][2] = -(motion_plan[i+1][2] - motion_plan[i][2]) + change_plan[i+1][1]

def run_motion_plan():
    for i in range(0,motion_length):
        set_joints_rad(motion_plan[i,0],motion_plan[i,1],motion_plan[i,2])
        #move_dummy(forward_kinematics(motion_plan[i,0],motion_plan[i,1],motion_plan[i,2]))
        # print("step")
        sleep(0.02)

def save():
    f = open('./motion_plan','w')
    print(motion_length)
    for i in range(0,motion_length):
        f.write("{:.4f}".format(change_plan[i][0]) + "," + "{:.4f}".format(change_plan[i][1]) + "," + "{:.4f}".format(change_plan[i][2]) + "\n")
    f.write(" ")

if __name__ == "__main__":
    # Drawing plane Height Constant - According to the VREP model
    Z_draw = 0 # writing plane height
    print("1")
    factor, path, points, x, y = image_processing_optimization(img = 'Images/write.png', factor = 1, size = 200) # Restriction -> factor*size < 350
    print("2")
    # Start Drawing
    draw_VREP(factor, path, points, Z_draw, x, y)
    print("3")
    print(motion_length)
    # Wait until a key press
    run_motion_plan()
    trans2stepcode(motion_plan)
    save()
    cv2.waitKey()
################################################################################
