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
dtheta = 0.001
tool_length = 0.13

# Solving Ax=b
def inverse_kinematics(pos_ori_mat):
    count = 0
    while (count < 600):
        # limit loop times
        count = count + 1
        # print("start count = " + str(count))
        # Find error vector
        # current PR_mat
        for i in range(0,6):
            current_angles[i] = goal_angles[i]
            #print("current joint " + str(i+1) + " angle is " + str(current_angles[i]))
        current_T = Forward_kinematics(current_angles[0],current_angles[1],current_angles[2],current_angles[3],current_angles[4],current_angles[5])
        current_P = current_T[0:3,3]
        current_R = np.asmatrix(rotm2quat(current_T))
        current_R = current_R.reshape((4,1))
        current_PR_mat = np.vstack((current_P,current_R))
        #print("current_PR_mat : ")
        #print(current_PR_mat)
        # goal PR_mat
        goal_P = pos_ori_mat[0:3,3]
        goal_R = np.asmatrix(rotm2quat(pos_ori_mat))
        goal_R = goal_R.reshape((4,1))
        goal_PR_mat = np.vstack((goal_P,goal_R))
        #print("goal_PR_mat : ")
        #print(goal_PR_mat)
        # error vector
        error_vector = goal_PR_mat - current_PR_mat
        #print(error_vector)
        #print("error vector : ")
        #print(error_vector)
        # check if error is small enough to quit
        if (np.linalg.norm(error_vector) < 0.003):
            Move_to_joint_position_rad(goal_angles[0],goal_angles[1],goal_angles[2],goal_angles[3],goal_angles[4],goal_angles[5])
            #print("Arrived at goal location")
            #print("total iterations = " + str(count))
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
        #print("perturbation_P6: "+str(perturbation_P6))
        perturbation_R1 = np.asmatrix(rotm2quat(perturbation_T1)).reshape((4,1))
        perturbation_R2 = np.asmatrix(rotm2quat(perturbation_T2)).reshape((4,1))
        perturbation_R3 = np.asmatrix(rotm2quat(perturbation_T3)).reshape((4,1))
        perturbation_R4 = np.asmatrix(rotm2quat(perturbation_T4)).reshape((4,1))
        perturbation_R5 = np.asmatrix(rotm2quat(perturbation_T5)).reshape((4,1))
        perturbation_R6 = np.asmatrix(rotm2quat(perturbation_T6)).reshape((4,1))
        #print("perturbation_R6: "+str(perturbation_R6))
        #  PR stack and reshape
        perturbation_PR_mat1 = np.vstack((perturbation_P1,perturbation_R1))
        perturbation_PR_mat2 = np.vstack((perturbation_P2,perturbation_R2))
        perturbation_PR_mat3 = np.vstack((perturbation_P3,perturbation_R3))
        perturbation_PR_mat4 = np.vstack((perturbation_P4,perturbation_R4))
        perturbation_PR_mat5 = np.vstack((perturbation_P5,perturbation_R5))
        perturbation_PR_mat6 = np.vstack((perturbation_P6,perturbation_R6))
        # Jacobian columns
        Jacobian1 = (perturbation_PR_mat1 - current_PR_mat)/dtheta
        Jacobian2 = (perturbation_PR_mat2 - current_PR_mat)/dtheta
        #print("Jaco2: ")
        #print(Jacobian2)
        Jacobian3 = (perturbation_PR_mat3 - current_PR_mat)/dtheta
        Jacobian4 = (perturbation_PR_mat4 - current_PR_mat)/dtheta
        Jacobian5 = (perturbation_PR_mat5 - current_PR_mat)/dtheta
        Jacobian6 = (perturbation_PR_mat6 - current_PR_mat)/dtheta
        # Jacobian matrix
        Jacobian = np.hstack((Jacobian1,Jacobian2,Jacobian3,Jacobian4,Jacobian5,Jacobian6))
        #print("Jacobian matrix: ")
        #print(Jacobian)
        # calculuate rot_theta with Jacobian transpose method
        Jacobian_trans = Jacobian.transpose()
        JJTe = Jacobian * Jacobian_trans * error_vector
        #alpha = (np.dot(np.asarray(error_vector),np.asarray(JJTe)))/np.linalg.norm(np.asarray(JJTe))
        # reshape_error_vector = error_vector.reshape((1,6))
        #alpha = (np.dot(reshape_error_vector,JJTe))/np.linalg.norm(JJTe)
        #alpha = 0.4
        #print("alpha: ")
        #print(alpha)
        #rot_theta = np.multiply(alpha,Jacobian_trans * error_vector)
        # testing Pseudo inverse method
        #print("testing")
        #J_pseudo = np.dot(Jacobian_trans,np.linalg.inv(Jacobian.dot(Jacobian_trans)))
        #dq = J_pseudo.dot(error_vector)
        #print(dq)
        # testing Damped Least Squares Method
        #print("this is error_vector")
        #print(np.linalg.norm(error_vector))
        #print(error_vector)
        f = np.linalg.solve(Jacobian.dot(Jacobian_trans) + 0.04 * np.identity(7), error_vector)
        dq = np.dot(Jacobian_trans, f)
        #print("This is dq: ")
        #print(dq)
        #print("norm of rot_theta: ")
        #print(np.linalg.norm(rot_theta))
        #print("rot_theta: ")
        #print(rot_theta)
        # Solve Ax=b
        #rot_theta = np.linalg.solve(Jacobian, error_vector)
        # update goal_angles
        '''
        for i in range(0,6):
            goal_angles[i] = current_angles[i] + rot_theta[i]
        Move_to_joint_position_rad(goal_angles[0],goal_angles[1],goal_angles[2],goal_angles[3],goal_angles[4],goal_angles[5])
        '''
        for i in range(0,6):
            goal_angles[i] = current_angles[i] + dq[i]
        #Move_to_joint_position_rad(goal_angles[0],goal_angles[1],goal_angles[2],goal_angles[3],goal_angles[4],goal_angles[5])
        #print("goal_angle:")
        #print(goal_angles)
        #time.sleep(0.01)
        #print("end count = " + str(count))
    if (count > 200):
        print('loop too many times')
        return

def Move_to_joint_position_deg(a0,a1,a2,a3,a4,a5):
    vrep.simxSetJointTargetPosition(clientID,joint_handle[0],Deg2rad(a0),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[1],Deg2rad(a1),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[2],Deg2rad(a2),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[3],Deg2rad(a3),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[4],Deg2rad(a4),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[5],Deg2rad(a5),vrep.simx_opmode_oneshot)

def Move_to_joint_position_rad(a0,a1,a2,a3,a4,a5):
    vrep.simxSetJointTargetPosition(clientID,joint_handle[0],a0,vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[1],a1,vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[2],a2,vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[3],a3,vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[4],a4,vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handle[5],a5,vrep.simx_opmode_oneshot)

def lerp(current_pos_ori, goal_pos_ori):
    current_pos = current_pos_ori[0:3,3]
    goal_pos = goal_pos_ori[0:3,3]
    velocity = 3e-04
    error_vector = goal_pos - current_pos
    error_len = np.linalg.norm(error_vector)
    N = (error_len / velocity)+1
    dx = (goal_pos[0] - current_pos[0]) / N
    dy = (goal_pos[1] - current_pos[1]) / N
    dz = (goal_pos[2] - current_pos[2]) / N
    for _ in range(0,int(N)):
        current_pos_ori[0,3] = current_pos_ori[0,3] + dx
        current_pos_ori[1,3] = current_pos_ori[1,3] + dy
        current_pos_ori[2,3] = current_pos_ori[2,3] + dz
        inverse_kinematics(current_pos_ori)
    current_pos = current_pos_ori[0:3,3]
    goal_pos = goal_pos_ori[0:3,3]
    error_vector = goal_pos - current_pos
    error_len = np.linalg.norm(error_vector)
    print("error length is: " + str(error_len))
    print('lerp done!')
    return

def draw_circle(current_pos_ori, radius):
    center_pos = current_pos_ori[0:3,3]
    center_x = center_pos[0]
    center_y = center_pos[1]
    center_z = center_pos[2]
    circumference = 2 * math.pi * radius
    velocity = 3e-03
    N = (circumference / velocity)+1
    dtheta = 2 * math.pi / N
    theta = 0
    #print("dtheta is : " + str(dtheta))
    for _ in range(0,int(N)):
        current_x = center_x + radius * math.cos(theta)
        #print("current_x: " + str(current_x))
        current_y = center_y + radius * math.sin(theta)
        #print("current_y: " + str(current_y))
        theta = theta + dtheta
        #print("old pos ori: ")
        #print(current_pos_ori)
        current_pos_ori[0,3] = current_x
        current_pos_ori[1,3] = current_y
        #print("1")
        inverse_kinematics(current_pos_ori)
        #print("new pos ori: ")
        #print(current_pos_ori)
        #print("2")
        time.sleep(0.02)
    # use get angle for joints and FK to check error
    #current_pos = current_pos_ori[0:3,3]
    #error_vector = center_pos - current_pos
    #error_len = np.linalg.norm(error_vector)
    #print("error length is: " + str(error_len))
    print("draw circle done!")
    return

def move_dummy(x,y,z,rx,ry,rz):
    position = np.array([x,y,z])
    orientation = np.array([rx,ry,rz])
    # get dummy handle
    status, dummy_handle = vrep.simxGetObjectHandle(clientID, 'Dummy', vrep.simx_opmode_blocking)
    if status!= vrep.simx_return_ok:
    	raise Exception('Cannot get handle of dummy')
    time.sleep(0.3)
    # move dummy
    status = vrep.simxSetObjectPosition(clientID,dummy_handle,-1,position,vrep.simx_opmode_blocking)
    if status != vrep.simx_return_ok:
    	raise Exception('Cannot get position of dummy')
    status = vrep.simxSetObjectOrientation(clientID,dummy_handle,-1,orientation,vrep.simx_opmode_blocking)
    if status != vrep.simx_return_ok:
    	raise Exception('Cannot get orientation of dummy')
    time.sleep(0.3)

def set_goal(pos_ori_mat):
    dummy_ori = rotm2euler(pos_ori_mat)
    dummy_pos = pos_ori_mat[0:3,3]
    move_dummy(dummy_pos[0],dummy_pos[1],dummy_pos[2],dummy_ori[0],dummy_ori[1],dummy_ori[2])
    return

# changed to based on radian
def Forward_kinematics(deg1,deg2,deg3,deg4,deg5,deg6):
    # convert from deg to rad and wrap
    theta = np.array([deg1,deg2,deg3,deg4,deg5,deg6])
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
    #print("Theoretical result: ")
    #print(T)
    #print('euler of T: ')
    #print(rotm2euler(T_reduced))
    # return
    return T

# test
Move_to_joint_position_deg(0,0,0,0,0,0)
# diff xyz, same ori

pos_ori_mat_1 = np.matrix([[0,   1,   0,   1.2235e-01],
                           [0,   0,   1,   0.6000e-00],
                           [1,   0,   0,   6.0000e-01],
                           [0,   0,   0,   1         ]])
set_goal(pos_ori_mat_1)
inverse_kinematics(pos_ori_mat_1)

pos_ori_mat_2 = np.matrix([[0,   1,   0,  -1.2235e-01],
                           [1,   0,   0,   0.5000e-00],
                           [0,   0,  -1,   5.0000e-01],
                           [0,   0,   0,   1         ]])
set_goal(pos_ori_mat_2)
inverse_kinematics(pos_ori_mat_2)

pos_ori_mat_3 = np.matrix([[0,   1,   0,  -1.2235e-01],
                           [1,   0,   0,   0.4000e-00],
                           [0,   0,  -1,   3.0000e-01],
                           [0,   0,   0,   1         ]])
set_goal(pos_ori_mat_3)
lerp(pos_ori_mat_2,pos_ori_mat_3)
time.sleep(0.5)
draw_circle(pos_ori_mat_3, 2.0000e-02)

pos_ori_mat_4 = np.matrix([[0,   1,   0,  -1.2235e-01],
                           [1,   0,   0,   0.7000e-00],
                           [0,   0,  -1,   3.0000e-01],
                           [0,   0,   0,   1         ]])
set_goal(pos_ori_mat_4)
lerp(pos_ori_mat_3,pos_ori_mat_4)

pos_ori_mat_5 = np.matrix([[0,   1,   0,  -3.2235e-01],
                           [1,   0,   0,   0.7000e-00],
                           [0,   0,  -1,   3.0000e-01],
                           [0,   0,   0,   1         ]])
set_goal(pos_ori_mat_5)
lerp(pos_ori_mat_3,pos_ori_mat_5)

set_goal(pos_ori_mat_2)
lerp(pos_ori_mat_5,pos_ori_mat_2)

time.sleep(1)

print('Done3')

# stop simulation and close connections
Disconnect(clientID)
