# import libraries:
import vrep
from time import sleep
import numpy as np
from math import sin, cos, pi
from toolbox import connect, disconnect
from toolbox import set_joints_deg
from toolbox import deg2rad
from toolbox import rotm2euler

# initialize and UR5 DH parameters
# d = np.array([ 0.089159,  0,      0,        0.10915,  0.09465,  0.0823])
# a = np.array([ 0,         0.425,  0.39225,  0,        0,        0     ])
# initialize and Kuka DH parameters
d = np.array([   0.352,      0,      0,  0.380,     0,   0.045])
a = np.array([   0.070,  0.360,      0,      0,     0,       0])
alp = np.array([ -pi/2,      0,  -pi/2,   pi/2,  pi/2,       0])
tool_length = 0.08
clientID = 0

# frame transformation
def Twr():
    joint_base_displacement_x = 6.8974e-02
    joint_base_displacement_y = -3.7329e-05
    mat = np.matrix([[ 1,  0,   0,   joint_base_displacement_x],
                     [ 0,  1,   0,   joint_base_displacement_y],
                     [ 0,  0,   1,                           0],
                     [ 0,  0,   0,                           1]])
    return mat

def T_im1_i(theta):
    mat = np.matrix([[ cos(theta),  -sin(theta)*cos(alpha),   sin(theta)*sin(alpha),   a*cos(theta)],
                     [ sin(theta),   cos(theta)*cos(alpha),  -cos(theta)*sin(alpha),   a*sin(theta)],
                     [ 0,            sin(alpha),              cos(alpha),              d           ],
                     [ 0,            0,                       0,                       1           ]])
    return mat

def T01(rad):
    mat = np.matrix([[ cos(rad),   0,    -sin(rad),   a[0]*cos(rad)],
                     [ sin(rad),   0,     cos(rad),   a[0]*sin(rad)],
                     [ 0,         -1,     0,          d[0]         ],
                     [ 0,          0,     0,          1            ]])
    return mat

def T12(rad):
    rad = - rad - pi/2
    mat = np.matrix([[ cos(rad),  -sin(rad),     0,   a[1]*cos(rad)],
                     [ sin(rad),   cos(rad),     0,   a[1]*sin(rad)],
                     [ 0,          0,            1,   d[1]         ],
                     [ 0,          0,            0,   1            ]])
    return mat

def T23(rad):
    rad = - rad
    mat = np.matrix([[ cos(rad),   0,    -sin(rad),   a[2]*cos(rad)],
                     [ sin(rad),   0,     cos(rad),   a[2]*sin(rad)],
                     [ 0,         -1,     0,          d[2]         ],
                     [ 0,          0,     0,          1            ]])
    return mat

def T34(rad):
    mat = np.matrix([[ cos(rad),   0,     sin(rad),   a[3]*cos(rad)],
                     [ sin(rad),   0,    -cos(rad),   a[3]*sin(rad)],
                     [ 0,          1,     0,          d[3]         ],
                     [ 0,          0,     0,          1            ]])
    return mat

def T45(rad):
    rad =  - rad + pi
    mat = np.matrix([[ cos(rad),   0,     sin(rad),   a[4]*cos(rad)],
                     [ sin(rad),   0,    -cos(rad),   a[4]*sin(rad)],
                     [ 0,          1,     0,          d[4]         ],
                     [ 0,          0,     0,          1            ]])
    return mat

def T56(rad):
    #rad = - rad
    mat = np.matrix([[ cos(rad),  -sin(rad),     0,   a[5]*cos(rad)],
                     [ sin(rad),   cos(rad),     0,   a[5]*sin(rad)],
                     [ 0,          0,            1,   d[5]         ],
                     [ 0,          0,            0,   1            ]])
    return mat

# from joint 6 to welding torch
def T6t(tool_length):
    mat = np.matrix([[-1,   0,    0,   0           ],
                     [ 0,   1,    0,   0           ],
                     [ 0,   0,   -1,   tool_length ],
                     [ 0,   0,    0,   1           ]])
    return mat


# from joint angles get cartesian position and orientation
def forward_kinematics(deg1, deg2, deg3, deg4, deg5, deg6):
    # convert from deg to rad and wrap
    theta = np.array([deg2rad(deg1), deg2rad(deg2), deg2rad(deg3), deg2rad(deg4), deg2rad(deg5), deg2rad(deg6)])
    # calculate respective transformation matrix
    Tmat_wr = Twr()
    Tmat_01 = T01(theta[0])
    Tmat_12 = T12(theta[1])
    Tmat_23 = T23(theta[2])
    Tmat_34 = T34(theta[3])
    Tmat_45 = T45(theta[4])
    Tmat_56 = T56(theta[5])
    Tmat_6t = T6t(tool_length)
    # combine
    T = Tmat_wr * Tmat_01 * Tmat_12 * Tmat_23 * Tmat_34 * Tmat_45 * Tmat_56 * Tmat_6t
    #T = Tmat_wr * Tmat_01 * Tmat_12 * Tmat_23 * Tmat_34 * Tmat_45 * Tmat_56
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
    res, dummy_handle = vrep.simxGetObjectHandle(clientID, 'dummy_test', vrep.simx_opmode_blocking)
    if res != vrep.simx_return_ok:
    	raise Exception('Cannot get handle of dummy')
    sleep(1)
    # create dummy
    res = vrep.simxSetObjectPosition(clientID, dummy_handle, -1,translation_mat, vrep.simx_opmode_blocking)
    if res != vrep.simx_return_ok:
    	raise Exception('Cannot get position of dummy')
    res = vrep.simxSetObjectOrientation(clientID, dummy_handle, -1, euler, vrep.simx_opmode_blocking)
    if res != vrep.simx_return_ok:
    	raise Exception('Cannot get orientation of dummy')
    sleep(1)

" ==================================== 主函数 ==================================== "

def main():
    # connect
    clientID, _ = connect()
    # plan for joint angles to follow
    '''
    motion_plan = np.array([[  0,   0,   0,   0,   0,   0]])
    '''
    motion_plan = np.array([[   0,  0,  0,   0,  0,  0],
                            [  45,  0, 30,   0, 40,  0],
                            [  90, 30,  0, -30, 70, 90]])

    # execution
    for i in range(0,np.size(motion_plan,0)):
        set_joints_deg(np.array([motion_plan[i,0], motion_plan[i,1], motion_plan[i,2], motion_plan[i,3], motion_plan[i,4], motion_plan[i,5]]))
        forward_kinematics(motion_plan[i,0], motion_plan[i,1], motion_plan[i,2], motion_plan[i,3], motion_plan[i,4], motion_plan[i,5])
        sleep(2)
    # disconnect
    if (input("Press any key to quit: ") != '|'):
        disconnect()

if __name__ == "__main__":
    main()
    print("Demo 2 Complete !!!")
