import vrep
import math
import numpy as np

PI = math.pi

def Deg2rad(deg):
    return deg * PI / 180

def Rad2deg(rad):
    return rad * 180 / PI

def rot2euler(rotation_mat):
    if rotation_mat[0,2] < 1:
        if rotation_mat[0,2] > -1:
            beta = np.arcsin(rotation_mat[0,2])
            alpha = np.arctan2(-rotation_mat[1,2],rotation_mat[2,2])
            garma = np.arctan2(-rotation_mat[0,1],rotation_mat[0,0])
        else:
            beta = -PI/2
            alpha = np.arctan2(rotation_mat[1,0],rotation_mat[1,1])
            garma = 0
    else:
        beta = PI/2
        alpha = np.arctan2(rotation_mat[1,0],rotation_mat[1,1])
        garma = 0
    # warpping
    euler = np.array([alpha,beta,garma])
    return euler

def T_mat(theta,d,a,alpha):
    mat = np.matrix([[math.cos(theta), -math.sin(theta)*math.cos(alpha),  math.sin(theta)*math.sin(alpha),  a*math.cos(theta)],
                     [math.sin(theta),  math.cos(theta)*math.cos(alpha), -math.cos(theta)*math.sin(alpha),  a*math.sin(theta)],
                     [0              ,  math.sin(alpha)                ,  math.cos(alpha)                ,  d                ],
                     [0              ,  0                              ,  0                              ,  1                ]])
    return mat

#def Arr2mat(arr):
# reference
def rotm2euler(R) :

    sy = math.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
    singular = sy < 1e-6

    if  not singular :
        x = math.atan2(R[2,1] , R[2,2])
        y = math.atan2(-R[2,0], sy)
        z = math.atan2(R[1,0], R[0,0])
    else :
        x = math.atan2(-R[1,2], R[1,1])
        y = math.atan2(-R[2,0], sy)
        z = 0

    return np.array([x, y, z])
