# import libraries:
import vrep
from time import sleep
import numpy as np
from math import pi, cos, sin, atan2, sqrt, acos
from numpy.linalg import norm

# initialize and DH darameters
clientID = 0
joint_handles = np.zeros(4, dtype = np.int)
PI = pi
# base
r1 = 0.063247
h1 = 0.10601
# link1
r2 = 0.11345
h2 = 0.10561
l2 = 0.154998
theta2 = 0.749624 # 42.95
origin2 = 1.850049 # 106.00
# link2
r3 = 0.16145
h3 = -0.079190
l3 = 0.179825
theta3 = -0.456013 # -26.128
origin3 = 0.645772 # 37.00
# link3 (tool)
r4 = 0.035278
h4 = -0.029195


motion_plan = np.zeros(3*700).reshape(700,3)
change_plan = motion_plan.copy()
motion_length = 0

# connect and get handles
def connect():
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

# move six joints at once
def set_joints_deg(a0, a1, a2):
    vrep.simxSetJointTargetPosition(clientID, joint_handles[0], deg2rad(a0), vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID, joint_handles[1], deg2rad(a1), vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID, joint_handles[2], deg2rad(a2), vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID, joint_handles[3], deg2rad(-a1-a2), vrep.simx_opmode_oneshot)

def set_joints_rad(r0, r1, r2):
    vrep.simxSetJointTargetPosition(clientID, joint_handles[0], r0, vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID, joint_handles[1], r1, vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID, joint_handles[2], r2, vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID, joint_handles[3], -r1-r2, vrep.simx_opmode_oneshot)

# convert angle from degree to radian
def deg2rad(deg):
    return deg * PI / 180

def rad2deg(rad):
    return rad * 180 / PI

# forward kinematics
def forward_kinematics(deg1, deg2, deg3):
    rad1, rad2, rad3 = deg2rad(deg1), deg2rad(deg2), deg2rad(deg3)
    arm_r = r1 + l2 * cos(rad2 + theta2) + l3 * cos(rad2 + rad3 + theta3) + r4
    x = round(arm_r * cos(rad1), 4)
    y = round(arm_r * sin(rad1), 4)
    z = round(h1 + l2 * sin(rad2 + theta2) + l3 * sin(rad2 + rad3 + theta3) + h4, 4)
    # print("x, y, z = " + str(x) + " " + str(y) + " " + str(z))
    return x, y, z

# inverse kinematics
def inverse_kinematics(x, y, z):
    # solving for theta 1
    rad1 = round(atan2(y, x), 4)
    # solving for theta 2 and 3
    r = sqrt(pow(x, 2) + pow(y, 2)) - r1 - r4
    h = z - h1 - h4
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

# record joint rads
def record_rads(rad1, rad2, rad3):
    global motion_plan, motion_length
    motion_plan[motion_length][0] = rad1
    motion_plan[motion_length][1] = rad2
    motion_plan[motion_length][2] = rad3
    motion_length += 1

# reset
def seperate(start_rad, end_rad):
    dif = [abs(end_rad[0]-start_rad[0]), abs(end_rad[1]-start_rad[1]), abs(end_rad[2]-start_rad[2])]
    max_dif = max(dif)
    speed = (10.0 * PI) / (20 * 180) # 10 deg per second
    N = int((max_dif/speed)+1)
    print("N = " + str(N))
    drad1 = (end_rad[1] - start_rad[1])/N
    drad2 = (end_rad[2] - start_rad[2])/N
    for i in range(1,N+1):
        record_rads(end_rad[0], start_rad[1] + drad1 * i, start_rad[2] + drad2 * i)


# draw circle
def draw_circle(current_pos, radius):
    # velocity should be set in meters per second, then converted to distance per 50ms(step in simulation)
    center_x = current_pos[0]
    center_y = current_pos[1]
    center_z = current_pos[2]
    #print("x: " + str(center_x))
    #print("y: " + str(center_y))
    #print("z: " + str(center_z))
    circumference = 2 * PI * radius
    velocity = 5e-2 / 20 # 1cm/s divided into 50ms steps
    N = int((circumference / velocity)+1)
    #print("N in circle = " + str(N))
    dtheta = 2 * PI / N
    theta = 0
    # move from center of circle to side
    goal_pos = current_pos.copy()
    goal_pos[2] = goal_pos[2] + 0.02 # lift up
    lerp(current_pos, goal_pos)
    side_pos = goal_pos.copy()
    #sleep(1)
    goal_pos = side_pos.copy()
    goal_pos[0] = side_pos[0] + radius # move to side
    lerp(side_pos, goal_pos)
    side_pos = goal_pos.copy()
    #sleep(1)
    goal_pos = side_pos.copy()
    goal_pos[2] = side_pos[2] - 0.02 # lift up
    lerp(side_pos, goal_pos)
    side_pos = goal_pos.copy()
    #sleep(1)
    for i in range(1, N+1):
        t = i / N
        #print("Progress: " + str(format(100*t,".1f")) + "%")
        #print("radius: " + str(radius))
        #print("theta: " + str(theta))
        current_x = center_x + radius * cos(theta)
        current_y = center_y + radius * sin(theta)
        #print("current_x : " + str(current_x))
        #print("current_y : " + str(current_y))
        theta = theta + dtheta
        current_pos[0] = current_x
        current_pos[1] = current_y
        current_pos[2] = 0
        motion_rads = inverse_kinematics(current_pos[0],current_pos[1],current_pos[2])
        record_rads(motion_rads[0],motion_rads[1],motion_rads[2])
        #sleep(0.02)
    return

# draw line
def lerp(start_pos, goal_pos):
    velocity = 0.05 / 20 # 5cm/s divided into 50ms steps
    error_len = goal_pos[0] - start_pos[0]
    if (error_len < 0.00001):
        error_len = goal_pos[2] - start_pos[2]
    N = abs(int((error_len / velocity)+1))
    #print("N in lerp = " + str(N))
    dx = (goal_pos[0] - start_pos[0]) / N
    dy = (goal_pos[1] - start_pos[1]) / N
    dz = (goal_pos[2] - start_pos[2]) / N
    for i in range(1, N+1):
        t = i / N
        # print("Progress: " + str(format(100*t,".1f")) + "%")
        start_pos[0] = start_pos[0] + dx
        start_pos[1] = start_pos[1] + dy
        start_pos[2] = start_pos[2] + dz
        motion_rads = inverse_kinematics(start_pos[0],start_pos[1],start_pos[2])
        record_rads(motion_rads[0],motion_rads[1],motion_rads[2])
        #sleep(0.02)
    print("lerp done")
    return

def move_dummy(goal_pos):
    # get dummy handle
    res, dummy_handle = vrep.simxGetObjectHandle(clientID, 'Dummy', vrep.simx_opmode_blocking)
    if res != vrep.simx_return_ok:
    	raise Exception('Cannot get handle of dummy')
    sleep(1)
    # move dummy
    # print("1")
    res = vrep.simxSetObjectPosition(clientID, dummy_handle, -1, goal_pos, vrep.simx_opmode_blocking)
    if res != vrep.simx_return_ok:
    	raise Exception('Cannot set position of dummy')
    # print("2")
    sleep(1)

def save():
    f = open('./motion_plan','w')
    for i in range(0,motion_length):
        f.write("{:.4f}".format(change_plan[i][0]) + "," + "{:.4f}".format(change_plan[i][1]) + "," + "{:.4f}".format(change_plan[i][2]) + "\n")
    f.write(" ")

" ==================================== 主函数 ==================================== "

def main():
    # declare global
    print("hello")
    global clientID, joint_handles
    # connect
    clientID, joint_handles = connect()
    print("connect")
    # plan for joint angles to follow
    destination_points = np.array([0.32342, 0, 0.0])
    # execution
    # print(destination_points)
    #move_dummy(destination_points)
    rad1, rad2, rad3 = inverse_kinematics(destination_points[0], destination_points[1], destination_points[2])
    # print(forward_kinematics(rad1, rad2, rad3))
    # print("rad1 = " + str(rad1))
    # print("rad2 = " + str(rad2))
    # print("rad3 = " + str(rad3))
    #print("deg1 = "+ str(round(rad2deg(rad1),4)))
    #print("deg2 = "+ str(round(rad2deg(rad2),4)))
    #print("deg3 = "+ str(round(rad2deg(rad3),4)))
    print("origin2 = " + str(origin2))
    print("origin3 = " + str(origin3))
    print("theta2 = " + str(theta2))
    print("theta3 = " + str(theta3))
    seperate([0,origin2-theta2,origin3-theta3-(origin2-theta2)],[0,0,0])
    print("these are the differences: ")
    print(origin2-theta2)
    print(origin3-theta3-(origin2-theta2))
    seperate([0,0,0],[rad1,rad2,rad3])
    draw_circle([0.32342, 0, 0.0],0.06)
    # print("done")
    #sleep(2)
    set_joints_rad(0,origin2-theta2,origin3-theta3-(origin2-theta2))
    sleep(1)
    '''
    set_joints_deg(0,0,0)
    sleep(1)
    set_joints_deg(0,20,0)
    sleep(1)
    set_joints_deg(0,0,0)
    sleep(1)
    set_joints_deg(0,0,20)
    sleep(1)
    set_joints_deg(0,0,0)
    sleep(1)
    set_joints_rad(0,origin2-theta2,origin3-theta3-(origin2-theta2))
    sleep(1)
    #print("initial position")
    #sleep(1)
    '''
    '''
    set_joints_deg(0,0,40)
    sleep(1)
    set_joints_deg(0,0,0)
    sleep(1)
    print("hello")

    '''

    for i in range(0,motion_length):
        set_joints_rad(motion_plan[i,0],motion_plan[i,1],motion_plan[i,2])
        #move_dummy(forward_kinematics(motion_plan[i,0],motion_plan[i,1],motion_plan[i,2]))
        # print("step")
        sleep(0.02)

    for i in range(0,motion_length):
        motion_plan[i][0] = round(rad2deg(motion_plan[i][0]),4)
        motion_plan[i][1] = round(rad2deg(motion_plan[i][1]),4)
        motion_plan[i][2] = round(rad2deg(motion_plan[i][2]),4)
        #print(motion_plan[i])
    # change_plan
    for i in range(0,motion_length):
        change_plan[i+1][0] = (motion_plan[i+1][0] - motion_plan[i][0])
        change_plan[i+1][1] = -(motion_plan[i+1][1] - motion_plan[i][1])
        change_plan[i+1][2] = -(motion_plan[i+1][2] - motion_plan[i][2]) + change_plan[i+1][1]
    # disconnect
    save()
    sleep(1)
    if (input("Press any key to quit: ") != '|'):
        disconnect()

if __name__ == "__main__":
    main()
    print("Demo 1 Complete !!!")
