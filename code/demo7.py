# import libraries:
import vrep
import time
import numpy as np
from toolbox import deg2rad

# initialize
clientID = 0
joint_handles = np.zeros(6, dtype = np.int)

# connect and get handles
# just in case, stop all prior connection
vrep.simxFinish(-1)
print(joint_handles[0])
# connect to vrep server
clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
if clientID != -1:  # check if client connection successful
    print("Connected successful")
else:
    raise Exception("Failed to connect")
# start simulation
vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot)

# get handles
res, joint_handles[0] = vrep.simxGetObjectHandle(clientID, 'Kuka_joint1', vrep.simx_opmode_blocking)
if res != vrep.simx_return_ok:
    raise Exception("Cannot get handle of first joint")
else:
    print("joint 1 connection successful")
res, joint_handles[1] = vrep.simxGetObjectHandle(clientID, 'Kuka_joint2', vrep.simx_opmode_blocking)
if res != vrep.simx_return_ok:
    raise Exception("Cannot get handle of second joint")
else:
    print("joint 2 connection successful")
res, joint_handles[2] = vrep.simxGetObjectHandle(clientID, 'Kuka_joint3', vrep.simx_opmode_blocking)
if res != vrep.simx_return_ok:
    raise Exception("Cannot get handle of third joint")
else:
    print("joint 3 connection successful")
res, joint_handles[3] = vrep.simxGetObjectHandle(clientID, 'Kuka_joint4', vrep.simx_opmode_blocking)
if res != vrep.simx_return_ok:
    raise Exception("Cannot get handle of fourth joint")
else:
    print("joint 4 connection successful")
res, joint_handles[4] = vrep.simxGetObjectHandle(clientID, 'Kuka_joint5', vrep.simx_opmode_blocking)
if res != vrep.simx_return_ok:
    raise Exception("Cannot get handle of fifth joint")
else:
    print("joint 5 connection successful")
res, joint_handles[5] = vrep.simxGetObjectHandle(clientID, 'Kuka_joint6', vrep.simx_opmode_blocking)
if res != vrep.simx_return_ok:
    raise Exception("Cannot get handle of sixth joint")
else:
    print("joint 6 connection successful")

print("these are joint handles: ")
print(joint_handles)

# move six joints at once
vrep.simxSetJointTargetPosition(clientID, joint_handles[0], deg2rad(90), vrep.simx_opmode_oneshot)
vrep.simxSetJointTargetPosition(clientID, joint_handles[1], deg2rad(30), vrep.simx_opmode_oneshot)
'''
vrep.simxSetJointTargetPosition(clientID, joint_handles[2], deg2rad(0), vrep.simx_opmode_oneshot)
vrep.simxSetJointTargetPosition(clientID, joint_handles[3], deg2rad(0), vrep.simx_opmode_oneshot)
vrep.simxSetJointTargetPosition(clientID, joint_handles[4], deg2rad(0), vrep.simx_opmode_oneshot)
vrep.simxSetJointTargetPosition(clientID, joint_handles[5], deg2rad(0), vrep.simx_opmode_oneshot)
'''

time.sleep(2)


print("demo 7 done !!!")
# stop simulation
vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot)
# make sure StopSimulation arrives
vrep.simxGetPingTime(clientID)
# disconnect from vrep server
vrep.simxFinish(clientID)
