# import libraries:
import vrep
import time
import numpy as np
import math
from toolbox import connect, disconnect
from toolbox import set_joints_deg
from toolbox import deg2rad
from toolbox import rotm2euler

# initialize and UR5 DH parameters
d = np.array([ 0.089159,  0,      0,        0.10915,  0.09465,  0.0823])
a = np.array([ 0,         0.425,  0.39225,  0,        0,        0     ])
tool_length = 0.23
clientID = 0

# frame transformation
def T01(rad):
    mat = np.matrix([[0,  -math.sin(rad),  -math.cos(rad),   0   ],
                     [0,   math.cos(rad),  -math.sin(rad),   0   ],
                     [1,   0,               0,               d[0]],
                     [0,   0,               0,               1   ]])
    return mat

def T12(rad):
    mat = np.matrix([[math.cos(rad),  -math.sin(rad),   0,   a[1]*math.cos(rad)],
                     [math.sin(rad),   math.cos(rad),   0,   a[1]*math.sin(rad)],
                     [0,               0,               1,   0                 ],
                     [0,               0,               0,   1                 ]])
    return mat

def T23(rad):
    mat = np.matrix([[math.cos(rad),  -math.sin(rad),   0,   a[2]*math.cos(rad)],
                     [math.sin(rad),   math.cos(rad),   0,   a[2]*math.sin(rad)],
                     [0,               0,               1,   0                 ],
                     [0,               0,               0,   1                 ]])
    return mat

def T34(rad):
    mat = np.matrix([[ 0,  -math.sin(rad),  math.cos(rad),   0   ],
                     [ 0,   math.cos(rad),  math.sin(rad),   0   ],
                     [-1,   0,              0,               d[3]],
                     [ 0,   0,              0,               1   ]])
    return mat

def T45(rad):
    mat = np.matrix([[0,  -math.sin(rad),  -math.cos(rad),   0   ],
                     [0,   math.cos(rad),  -math.sin(rad),   0   ],
                     [1,   0,               0,               d[4]],
                     [0,   0,               0,               1   ]])
    return mat

def T56(rad):
    mat = np.matrix([[math.cos(rad),  -math.sin(rad),   0,   0   ],
                     [math.sin(rad),   math.cos(rad),   0,   0   ],
                     [0,               0,               1,   d[5]],
                     [0,               0,               0,   1   ]])
    return mat

# from joint 6 to weolding torch
def T6t(tool_length):
    mat = np.matrix([[1,   0,   0,   0           ],
                     [0,   1,   0,   0           ],
                     [0,   0,   1,   tool_length ],
                     [0,   0,   0,   1           ]])
    return mat


# from joint angles get cartesian position and orientation
def forward_kinematics(deg1, deg2, deg3, deg4, deg5, deg6):
    # convert from deg to rad and wrap
    theta = np.array([deg2rad(deg1), deg2rad(deg2), deg2rad(deg3), deg2rad(deg4), deg2rad(deg5), deg2rad(deg6)])
    # calculate respective transformation matrix
    Tmat_01 = T01(theta[0])
    Tmat_12 = T12(theta[1])
    Tmat_23 = T23(theta[2])
    Tmat_34 = T34(theta[3])
    Tmat_45 = T45(theta[4])
    Tmat_56 = T56(theta[5])
    Tmat_6t = T6t(tool_length)
    # combine
    T = Tmat_01 * Tmat_12 * Tmat_23 * Tmat_34 * Tmat_45 * Tmat_56 * Tmat_6t
    # move dummy to tool location to verify accuracy of forward kinematics
    move_dummy(T)
    # return
    return T

# bummy manipulation
def move_dummy(T):
    # Extract rotation and translation
    rotation_mat = T[0:3,0:3]
    translation_mat = T[0:3,3]
    # matrix to euler
    euler = rotm2euler(T)
    # get dummy handle
    res, dummy_handle = vrep.simxGetObjectHandle(clientID, 'Dummy', vrep.simx_opmode_blocking)
    if res != vrep.simx_return_ok:
    	raise Exception('Cannot get handle of dummy')
    time.sleep(1)
    # create dummy
    res = vrep.simxSetObjectPosition(clientID, dummy_handle, -1,translation_mat, vrep.simx_opmode_blocking)
    if res != vrep.simx_return_ok:
    	raise Exception('Cannot get position of dummy')
    res = vrep.simxSetObjectOrientation(clientID, dummy_handle, -1, euler, vrep.simx_opmode_blocking)
    if res != vrep.simx_return_ok:
    	raise Exception('Cannot get orientation of dummy')
    time.sleep(1)

def main():
    # connect
    clientID, _, _ = connect()
    # plan for joint angles to follow
    motion_plan = np.array([[-45,  0, 90,   0, 90,  0],
                            [ 90, 30, 60, -30, 90, 90]])
    # execution
    for i in range(0,np.size(motion_plan,0)):
        set_joints_deg(np.array([motion_plan[i,0], motion_plan[i,1], motion_plan[i,2], motion_plan[i,3], motion_plan[i,4], motion_plan[i,5]]))
        forward_kinematics(motion_plan[i,0], motion_plan[i,1], motion_plan[i,2], motion_plan[i,3], motion_plan[i,4], motion_plan[i,5])
        time.sleep(1)
    # disconnect
    disconnect()

if __name__ == "__main__":
    main()
    print("Demo 2 Complete !!!")
