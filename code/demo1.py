# import libraries:
import vrep
import time
import numpy as np
from toolbox import deg2rad

# initialize
clientID = 0
joint_handles = np.zeros(6, dtype = np.int)

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
    res, joint_handles[0] = vrep.simxGetObjectHandle(clientID, 'UR5_joint1', vrep.simx_opmode_blocking)
    if res != vrep.simx_return_ok:
        raise Exception("Cannot get handle of first joint")
    res, joint_handles[1] = vrep.simxGetObjectHandle(clientID, 'UR5_joint2', vrep.simx_opmode_blocking)
    if res != vrep.simx_return_ok:
        raise Exception("Cannot get handle of second joint")
    res, joint_handles[2] = vrep.simxGetObjectHandle(clientID, 'UR5_joint3', vrep.simx_opmode_blocking)
    if res != vrep.simx_return_ok:
        raise Exception("Cannot get handle of third joint")
    res, joint_handles[3] = vrep.simxGetObjectHandle(clientID, 'UR5_joint4', vrep.simx_opmode_blocking)
    if res != vrep.simx_return_ok:
        raise Exception("Cannot get handle of fourth joint")
    res, joint_handles[4] = vrep.simxGetObjectHandle(clientID, 'UR5_joint5', vrep.simx_opmode_blocking)
    if res != vrep.simx_return_ok:
        raise Exception("Cannot get handle of fifth joint")
    res, joint_handles[5] = vrep.simxGetObjectHandle(clientID, 'UR5_joint6', vrep.simx_opmode_blocking)
    if res != vrep.simx_return_ok:
        raise Exception("Cannot get handle of sixth joint")
    res, welding_torch_handle = vrep.simxGetObjectHandle(clientID, 'Welding_torch', vrep.simx_opmode_blocking)
    if res != vrep.simx_return_ok:
    	raise Exception('Cannot get handle of welding torch')
    # return
    return clientID, joint_handles, welding_torch_handle

def disconnect():
    # stop simulation
    vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot)
    # make sure StopSimulation arrives
    vrep.simxGetPingTime(clientID)
    # disconnect from vrep server
    vrep.simxFinish(clientID)

# move six joints at once
def set_joints_deg(a0, a1, a2, a3, a4, a5):
    vrep.simxSetJointTargetPosition(clientID, joint_handles[0], deg2rad(a0), vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID, joint_handles[1], deg2rad(a1), vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID, joint_handles[2], deg2rad(a2), vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID, joint_handles[3], deg2rad(a3), vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID, joint_handles[4], deg2rad(a4), vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID, joint_handles[5], deg2rad(a5), vrep.simx_opmode_oneshot)

" ==================================== 主函数 ==================================== "

def main():
    # declare global
    global clientID, joint_handles
    # connect
    clientID, joint_handles, _ = connect()
    # plan for joint angles to follow
    motion_plan = np.array([[ 90, 90, -90,  90, 90, 90],
                            [-90, 45,  90, 135, 90, 90],
                            [  0,  0,   0,   0,  0,  0]])
    # execution
    for i in range(0,np.size(motion_plan,0)):
        set_joints_deg(motion_plan[i,0],motion_plan[i,1],motion_plan[i,2],motion_plan[i,3],motion_plan[i,4],motion_plan[i,5])
        time.sleep(1)
    # disconnect
    disconnect()

if __name__ == "__main__":
    main()
    print("Demo 1 Complete !!!")
