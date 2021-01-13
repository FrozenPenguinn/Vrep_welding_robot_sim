import math
import numpy as np

PI = math.pi

def Deg2rad(deg):
    return deg * PI / 180

def Rad2deg(rad):
    return rad * 180 / PI

def T_mat(theta,d,a,alpha):
    mat = np.matrix([[math.cos(theta), -math.sin(theta)*math.cos(alpha),  math.sin(theta)*math.sin(alpha),  a*math.cos(theta)],
                     [math.sin(theta),  math.cos(theta)*math.cos(alpha), -math.cos(theta)*math.sin(alpha),  a*math.sin(theta)],
                     [0              ,  math.sin(alpha)                ,  math.cos(alpha)                ,  d                ],
                     [0              ,  0                              ,  0                              ,  1                ]])
    return mat
