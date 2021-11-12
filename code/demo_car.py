import vrep
import time
import cv2
import array

# constants and handles
clientID, fl_handle, fr_handle, cam_handle = 0

def connect():
    global clientID, fl_handle, fr_handle, cam_handle
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
    res, fl_handle = vrep.simxGetObjectHandle(clientID, 'fl_joint', vrep.simx_opmode_blocking)
    if res != vrep.simx_return_ok:
        raise Exception("Cannot get handle of front left wheel")
    res, fr_handle = vrep.simxGetObjectHandle(clientID, 'fr_joint', vrep.simx_opmode_blocking)
    if res != vrep.simx_return_ok:
        raise Exception("Cannot get handle of front right wheel")
    res, cam_handle = vrep.simxGetObjectHandle(clientID, 'vision_sensor', vrep.simx_opmode_blocking)
    if res != vrep.simx_return_ok:
        raise Exception("Cannot get handle of vision sensor")
    return

def set_velocity(fl_velocity, fr_velocity):
    vrep.simxSetJointTargetVelocity(clientID, fl_handle, fl_velocity, vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetVelocity(clientID, fr_handle, fr_velocity, vrep.simx_opmode_oneshot)
    return

def get_frame():
    ret, reso, frame = vrep.simxGetVisionSensorImage(clientID, cam_handle, 0, vrep.simx_opmode_buffer)
    image_byte_array = array.array('b',frame)
    im = Image.frombuffer('RGB', (256,144), image_byte_array, "raw", "RGB", 0, 1)
    im.show()
    time.sleep(15)

# stop simulation
vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot)
# make sure StopSimulation arrives
vrep.simxGetPingTime(clientID)
# disconnect from vrep server
vrep.simxFinish(clientID)
