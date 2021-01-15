import sys
import vrep
import time
import numpy as np

def Connect():
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
    status, joint1_handle = vrep.simxGetObjectHandle(clientID, 'UR5_joint1',vrep.simx_opmode_blocking)
    if status != vrep.simx_return_ok:
        raise Exception("Cannot get handle of first joint")

    status, joint2_handle = vrep.simxGetObjectHandle(clientID, 'UR5_joint2',vrep.simx_opmode_blocking)
    if status != vrep.simx_return_ok:
        raise Exception("Cannot get handle of second joint")

    status, joint3_handle = vrep.simxGetObjectHandle(clientID, 'UR5_joint3',vrep.simx_opmode_blocking)
    if status != vrep.simx_return_ok:
        raise Exception("Cannot get handle of third joint")

    status, joint4_handle = vrep.simxGetObjectHandle(clientID, 'UR5_joint4',vrep.simx_opmode_blocking)
    if status != vrep.simx_return_ok:
        raise Exception("Cannot get handle of fourth joint")

    status, joint5_handle = vrep.simxGetObjectHandle(clientID, 'UR5_joint5',vrep.simx_opmode_blocking)
    if status != vrep.simx_return_ok:
        raise Exception("Cannot get handle of fifth joint")

    status, joint6_handle = vrep.simxGetObjectHandle(clientID, 'UR5_joint6',vrep.simx_opmode_blocking)
    if status != vrep.simx_return_ok:
        raise Exception("Cannot get handle of sixth joint")

    status, end_effector_handle = vrep.simxGetObjectHandle(clientID, 'End_effector', vrep.simx_opmode_blocking)
    if status!= vrep.simx_return_ok:
    	raise Exception('Cannot get handle of end effector')

    # wrapping
    joint_handles = np.zeros(6, dtype=np.int)
    joint_handles[0] = joint1_handle
    joint_handles[1] = joint2_handle
    joint_handles[2] = joint3_handle
    joint_handles[3] = joint4_handle
    joint_handles[4] = joint5_handle
    joint_handles[5] = joint6_handle

    # return
    return clientID, joint_handles, end_effector_handle

def Disconnect(clientID):
    vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot)
    time.sleep(1)
    vrep.simxFinish(clientID)
