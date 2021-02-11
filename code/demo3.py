# import libraries:
import vrep
import time
import numpy as np
import math
from connection import *
from helper_functions import *

# connect and get handles
clientID, joint_handle, end_effector_handle = Connect()

# initialize
current_angles = [0,0,0,0,0,0]
goal_angles = np.zeros(6)
dtheta = 1e-12
tool_length = 0.13

# Solving Ax=b
def inverse_kinematics(pos_ori_mat):
    # Find error vector
    # current PR_mat
    count = 0
    while (count < 10):
        count = count + 1
        print('F1')
        for i in range(0,6):
            _, current_angles[i] = vrep.simxGetJointPosition(clientID, joint_handle[i], vrep.simx_opmode_blocking)
        print('F2')
        print(current_angles[0])
        print(type(current_angles[0]))
        current_T = Forward_kinematics(current_angles[0],current_angles[1],current_angles[2],current_angles[3],current_angles[4],current_angles[5])
        current_P = current_T[0:3,3]
        current_R = np.asmatrix(rotm2euler(current_T))
        print('type of current_T: '+ str(type(current_T)))
        print('type of current_R: '+ str(type(current_R)))
        print('F3')
        current_R = current_R.shape(3,1)
        current_PR_mat = np.vstack(current_P,current_R)
        '''
        current_PR_mat = current_PR_mat.shape(6,1)
        '''
        # goal PR_mat
        goal_P = pos_ori_mat[0:3,3]
        goal_R = rotm2euler(pos_ori_mat)
        goal_PR_mat = np.stack(goal_P,goal_R)
        goal_PR_mat = goal_PR_mat.shape(6,1)
        # error vector
        error_vector = goal_PR_mat - current_PR_mat
        # check if error is small enough to quit
        if (np.linalg.norm(error_vector) < 0.01):
            break
        # Find Jacobian matrix
        # perturbation
        perturbation_T1 = Forward_kinematics(current_angles[0]+dtheta,current_angles[1],current_angles[2],current_angles[3],current_angles[4],current_angles[5])
        perturbation_T2 = Forward_kinematics(current_angles[0],current_angles[1]+dtheta,current_angles[2],current_angles[3],current_angles[4],current_angles[5])
        perturbation_T3 = Forward_kinematics(current_angles[0],current_angles[1],current_angles[2]+dtheta,current_angles[3],current_angles[4],current_angles[5])
        perturbation_T4 = Forward_kinematics(current_angles[0],current_angles[1],current_angles[2],current_angles[3]+dtheta,current_angles[4],current_angles[5])
        perturbation_T5 = Forward_kinematics(current_angles[0],current_angles[1],current_angles[2],current_angles[3],current_angles[4]+dtheta,current_angles[5])
        perturbation_T6 = Forward_kinematics(current_angles[0],current_angles[1],current_angles[2],current_angles[3],current_angles[4],current_angles[5]+dtheta)
        # extraction
        perturbation_P1 = perturbation_T1[0:3,3]
        perturbation_P2 = perturbation_T2[0:3,3]
        perturbation_P3 = perturbation_T3[0:3,3]
        perturbation_P4 = perturbation_T4[0:3,3]
        perturbation_P5 = perturbation_T5[0:3,3]
        perturbation_P6 = perturbation_T6[0:3,3]
        print("perturbation_P6: "+perturbation_P6)
        perturbation_R1 = rotm2euler(perturbation_T1)
        perturbation_R2 = rotm2euler(perturbation_T2)
        perturbation_R3 = rotm2euler(perturbation_T3)
        perturbation_R4 = rotm2euler(perturbation_T4)
        perturbation_R5 = rotm2euler(perturbation_T5)
        perturbation_R6 = rotm2euler(perturbation_T6)
        print("perturbation_R6: "+perturbation_R6)
        perturbation_R1 = perturbation_R1.shape(3,1)
        perturbation_R2 = perturbation_R2.shape(3,1)
        perturbation_R3 = perturbation_R3.shape(3,1)
        perturbation_R4 = perturbation_R4.shape(3,1)
        perturbation_R5 = perturbation_R5.shape(3,1)
        perturbation_R6 = perturbation_R6.shape(3,1)

        #  PR stack and reshape
        perturbation_PR_mat1 = np.vstack(perturbation_P1,perturbation_R1)
        perturbation_PR_mat2 = np.vstack(perturbation_P2,perturbation_R2)
        perturbation_PR_mat3 = np.vstack(perturbation_P3,perturbation_R3)
        perturbation_PR_mat4 = np.vstack(perturbation_P4,perturbation_R4)
        perturbation_PR_mat5 = np.vstack(perturbation_P5,perturbation_R5)
        perturbation_PR_mat6 = np.vstack(perturbation_P6,perturbation_R6)
        '''
        perturbation_PR_mat1 = perturbation_PR_mat1.shape(6,1)
        perturbation_PR_mat2 = perturbation_PR_mat2.shape(6,1)
        perturbation_PR_mat3 = perturbation_PR_mat3.shape(6,1)
        perturbation_PR_mat4 = perturbation_PR_mat4.shape(6,1)
        perturbation_PR_mat5 = perturbation_PR_mat5.shape(6,1)
        perturbation_PR_mat6 = perturbation_PR_mat6.shape(6,1)
        '''
        # Jacobian columns
        Jacobian1 = (perturbation_PR_mat1 - current_PR_mat)/dtheta
        Jacobian2 = (perturbation_PR_mat2 - current_PR_mat)/dtheta
        Jacobian3 = (perturbation_PR_mat3 - current_PR_mat)/dtheta
        Jacobian4 = (perturbation_PR_mat4 - current_PR_mat)/dtheta
        Jacobian5 = (perturbation_PR_mat5 - current_PR_mat)/dtheta
        Jacobian6 = (perturbation_PR_mat6 - current_PR_mat)/dtheta
        # Jacobian matrix
        Jacobian = np.hstack((Jacobian1,Jacobian2,Jacobian3,Jacobian4,Jacobian5,Jacobian6))
        # Solve Ax=b
        rot_theta = np.linalg.solve(Jacobian, error_vector)
        # update goal_angles
        for i in range(0,6):
            goal_angles[i] = current_angles[i] + rot_theta[i]
        Move_to_joint_position(current_angles[0],current_angles[1],current_angles[2],current_angles[3],current_angles[4],current_angles[5])
        time.sleep(2)
    if (count == 10):
        print('loop too many times')
    return

def Move_to_joint_position(a0,a1,a2,a3,a4,a5):
    vrep.simxSetJointTargetPosition(clientID,joint_handle[0],Deg2rad(a0),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[1],Deg2rad(a1),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[2],Deg2rad(a2),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[3],Deg2rad(a3),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[4],Deg2rad(a4),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[5],Deg2rad(a5),vrep.simx_opmode_oneshot)

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

def Forward_kinematics(deg1,deg2,deg3,deg4,deg5,deg6):
    # convert from deg to rad and wrap
    theta = np.array([Deg2rad(deg1),Deg2rad(deg2),Deg2rad(deg3),Deg2rad(deg4),Deg2rad(deg5),Deg2rad(deg6)])
    # calculate respective transformation matrix
    Tmat_01 = T01(theta[0])
    Tmat_12 = T12(theta[1])
    Tmat_23 = T23(theta[2])
    Tmat_34 = T34(theta[3])
    Tmat_45 = T45(theta[4])
    Tmat_56 = T56(theta[5])
    Tmat_6t = T6t(tool_length)
    # combine
    T = Tmat_01*Tmat_12*Tmat_23*Tmat_34*Tmat_45*Tmat_56*Tmat_6t
    # cut
    T_reduced = T[0:3]
    # show_dummy(T_reduced)
    # print
    print("Theoretical result: ")
    print(T)
    print('euler of T: ')
    print(rotm2euler(T_reduced))
    # return
    return T

# test
pos_ori_mat = np.matrix([[1,   0,   0,   3.2235e-01],
                         [0,   1,   0,  -7.3685e-05],
                         [0,   0,   1,   1.0012e+00],
                         [0,   0,   0,   1         ]])
inverse_kinematics(pos_ori_mat)

print('Done3')

# stop simulation and close connections
Disconnect(clientID)
