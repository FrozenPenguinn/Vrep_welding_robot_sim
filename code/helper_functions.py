# 工具箱简介    : toolbox content summary
# 弧角转换      : radian - degree transformations
# 位姿表达转换   : orientation representation transformations
# 参照系变换     : frame transformation
# 机械臂操作     : robotics arm manipulation
# 假人操作       : bummy manipulation
# 通信          : communications

# import libraries
import vrep
import math
import numpy as np
import numpy.linalg as lg

# constants and DH parameters
PI = math.pi
d = np.array([0.089159, 0, 0, 0.10915, 0.09465, 0.0823])
a = np.array([0, 0.425, 0.39225, 0, 0, 0])

''' radian - degree transformations '''

def deg2rad(deg):
    return deg * PI / 180

def rad2deg(rad):
    return rad * 180 / PI

''' orientation representation transformations '''

# 在使用欧拉角时，注意万向节死锁问题
def rotm2euler(mat):
    if mat[0,2] < 1:
        if mat[0,2] > -1:
            a = np.arctan2(-mat[1,2], mat[2,2])
            b = np.arcsin(mat[0,2])
            g = np.arctan2(-mat[0,1], mat[0,0])
        else:
            a = np.arctan2(mat[1,0], mat[1,1])
            b = -PI/2
            g = 0
    else:
        a = np.arctan2(mat[1,0], mat[1,1])
        b = PI/2
        g = 0
    return np.array([a, b, g]) # 之后要用matrix来打包

def euler2rotm(a,b,g):
    
    return

def rotm2quat(R):
    w = R[0,0]+R[1,1]+R[2,2]
    x = R[0,0]-R[1,1]-R[2,2]
    y = -R[0,0]+R[1,1]-R[2,2]
    z = -R[0,0]-R[1,1]+R[2,2]
    max_axis = max(w,x,y,z)
    if (w == max_axis):
        w = math.sqrt(R[0,0]+R[1,1]+R[2,2]+1)/2
        x = (R[1,2]-R[2,1])/(4*w)
        y = (R[2,0]-R[0,2])/(4*w)
        z = (R[0,1]-R[1,0])/(4*w)
    elif (x == max_axis):
        x = math.sqrt(R[0,0]-R[1,1]-R[2,2]+1)/2
        w = (R[1,2]-R[2,1])/(4*x)
        y = (R[0,1]+R[1,0])/(4*x)
        z = (R[2,0]+R[0,2])/(4*x)
    elif (y == max_axis):
        y = math.sqrt(-R[0,0]+R[1,1]-R[2,2]+1)/2
        w = (R[2,0]-R[0,2])/(4*y)
        x = (R[0,1]+R[1,0])/(4*y)
        z = (R[1,2]+R[2,1])/(4*y)
    else:
        z = math.sqrt(-R[0,0]-R[1,1]+R[2,2]+1)/2
        w = (R[0,1]-R[1,0])/(4*z)
        x = (R[2,0]+R[0,2])/(4*z)
        y = (R[1,2]+R[2,1])/(4*z)
    return np.array([w, x, y, z])

def quat2rotm(quat):
    w = quat[0]
    x = quat[1]
    y = quat[2]
    z = quat[3]
    R = np.matrix([[w*w+x*x-y*y-z*z, 2*(x*y-w*z)    , 2*(x*z+w*y)    ],
                   [2*(x*y+w*z)    , w*w-x*x+y*y-z*z, 2*(y*z-w*x)    ],
                   [2*(x*z-w*y)    , 2*(y*z+w*x)    , w*w-x*x-y*y+z*z]])
    # unit
    R[0:3,0] =  R[0:3,0] / np.linalg.norm(R[0:3,0])
    R[0:3,1] =  R[0:3,1] / np.linalg.norm(R[0:3,1])
    R[0:3,2] =  R[0:3,2] / np.linalg.norm(R[0:3,2])
    return R.transpose()


''' frame transformation '''

def T01(theta):
    mat = np.matrix([[0,  -math.sin(theta),  -math.cos(theta),   0   ],
                     [0,   math.cos(theta),  -math.sin(theta),   0   ],
                     [1,   0              ,   0              ,   d[0]],
                     [0,   0              ,   0              ,   1   ]])
    return mat

def T12(theta):
    mat = np.matrix([[math.cos(theta),  -math.sin(theta),   0,   a[1]*math.cos(theta)],
                     [math.sin(theta),   math.cos(theta),   0,   a[1]*math.sin(theta)],
                     [0              ,   0              ,   1,   0              ],
                     [0              ,   0              ,   0,   1              ]])
    return mat

def T23(theta):
    mat = np.matrix([[math.cos(theta),  -math.sin(theta),   0,   a[2]*math.cos(theta)],
                     [math.sin(theta),   math.cos(theta),   0,   a[2]*math.sin(theta)],
                     [0              ,   0              ,   1,   0              ],
                     [0              ,   0              ,   0,   1              ]])
    return mat

def T34(theta):
    mat = np.matrix([[ 0,  -math.sin(theta),  math.cos(theta),   0   ],
                     [ 0,   math.cos(theta),  math.sin(theta),   0   ],
                     [-1,   0              ,  0              ,   d[3]],
                     [ 0,   0              ,  0              ,   1   ]])
    return mat

def T45(theta):
    mat = np.matrix([[0,  -math.sin(theta),  -math.cos(theta),   0   ],
                     [0,   math.cos(theta),  -math.sin(theta),   0   ],
                     [1,   0              ,   0              ,   d[4]],
                     [0,   0              ,   0              ,   1   ]])
    return mat

def T56(theta):
    mat = np.matrix([[math.cos(theta),  -math.sin(theta),   0,   0   ],
                     [math.sin(theta),   math.cos(theta),   0,   0   ],
                     [0              ,   0              ,   1,   d[5]],
                     [0              ,   0              ,   0,   1   ]])
    return mat

def T6t(tool_length):
    mat = np.matrix([[1,   0,   0,   0           ],
                     [0,   1,   0,   0           ],
                     [0,   0,   1,   tool_length ],
                     [0,   0,   0,   1           ]])
    return mat

def set_goal(pos_ori_mat):
    dummy_ori = rotm2euler(pos_ori_mat)
    dummy_pos = pos_ori_mat[0:3,3]
    move_dummy(dummy_pos[0],dummy_pos[1],dummy_pos[2],dummy_ori[0],dummy_ori[1],dummy_ori[2])
    return

def move_dummy(x,y,z,rx,ry,rz):
    position = np.array([x,y,z])
    orientation = np.array([rx,ry,rz])
    # get dummy handle
    status, dummy_handle = vrep.simxGetObjectHandle(clientID, 'Dummy', vrep.simx_opmode_blocking)
    if status!= vrep.simx_return_ok:
    	raise Exception('Cannot get handle of dummy')
    time.sleep(1)
    # move dummy
    status = vrep.simxSetObjectPosition(clientID,dummy_handle,-1,position,vrep.simx_opmode_blocking)
    if status != vrep.simx_return_ok:
    	raise Exception('Cannot get position of dummy')
    status = vrep.simxSetObjectOrientation(clientID,dummy_handle,-1,orientation,vrep.simx_opmode_blocking)
    if status != vrep.simx_return_ok:
    	raise Exception('Cannot get orientation of dummy')
    time.sleep(1)
    return
