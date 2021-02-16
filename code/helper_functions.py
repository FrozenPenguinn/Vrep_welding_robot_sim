# toolbox content summary
# 位姿表达转换：
# rotm2euler()
# euler2rotm()
#



import vrep
import math
import numpy as np

PI = math.pi
d = np.array([0.089159,0,0,0.10915,0.09465,0.0823])
a = np.array([0,0.425,0.39225,0,0,0])

def Deg2rad(deg):
    return deg * PI / 180

def Rad2deg(rad):
    return rad * 180 / PI

# original
'''
def T_mat(theta,d,a,alpha):
    mat = np.matrix([[math.cos(theta), -math.sin(theta)*math.cos(alpha),  math.sin(theta)*math.sin(alpha),   a*math.cos(alpha)],
                     [math.sin(theta),  math.cos(theta)*math.cos(alpha), -math.cos(theta)*math.sin(alpha),   a*math.sin(alpha)],
                     [0              ,  math.sin(alpha)                ,  math.cos(alpha)                ,   d                ],
                     [0              ,  0                              ,  0                              ,   1                ]])
    return mat
'''
def T_mat(theta,d,a,alpha):
    mat = np.matrix([[math.cos(theta)*math.cos(alpha), -math.sin(theta),  math.cos(theta)*math.sin(alpha),   a*math.cos(theta)],
                     [math.sin(theta)*math.cos(alpha),  math.cos(theta),  math.sin(theta)*math.sin(alpha),   a*math.sin(theta)],
                     [-math.sin(alpha)               ,  0              ,  math.cos(alpha)                ,   d                ],
                     [0                              ,  0              ,  0                              ,   1                ]])
    return mat

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

#def Arr2mat(arr):
# reference
# 在负角度微扰下，rotm2euler的euler值出现全差pi的情况，慎用
def rotm2euler(R) :

    if R[0,2] < 1:
        if R[0,2] > -1:
            b = np.arcsin(R[0,2])
            a = np.arctan2(-R[1,2],R[2,2])
            g = np.arctan2(-R[0,1],R[0,0])
        else:
            b = -PI/2
            a = np.arctan2(R[1,0],R[1,1])
            g = 0
    else:
        b = PI/2
        a = np.arctan2(R[1,0],R[1,1])
        g = 0

    return np.array([a, b, g])

def euler2rotm(a,b,g):

    return

def base2world():

    return

def rotm2quat(R):
    w = math.sqrt(R[0,0]+R[1,1]+R[2,2]+1)/2
    x = math.sqrt(R[0,0]-R[1,1]-R[2,2]+1)/2
    y = math.sqrt(-R[0,0]+R[1,1]-R[2,2]+1)/2
    z = math.sqrt(-R[0,0]-R[1,1]+R[2,2]+1)/2
    max_axis = max(w,x,y,z)
    if (w == max_axis):
        x = (R[1,2]-R[2,1])/(4*w)
        y = (R[2,0]-R[0,2])/(4*w)
        z = (R[0,1]-R[1,0])/(4*w)
    elif (x == max_axis):
        w = (R[1,2]-R[2,1])/(4*x)
        y = (R[0,1]+R[1,0])/(4*x)
        z = (R[2,0]+R[0,2])/(4*x)
    elif (y == max_axis):
        w = (R[2,0]-R[0,2])/(4*y)
        x = (R[0,1]+R[1,0])/(4*y)
        z = (R[1,2]+R[2,1])/(4*y)
    else:
        w = (R[0,1]-R[1,0])/(4*z)
        x = (R[2,0]+R[0,2])/(4*z)
        y = (R[1,2]+R[2,1])/(4*z)
    return np.array([w, x, y, z])
