# 工具箱简介    : toolbox content summary
# 弧角转换      : radian - degree transformations
# 位姿表达转换   : orientation representation transformations
# 参照系变换     : frame transformations
# 机械臂解算     : robotic arm motion resoutions
# 机械臂运动     : robotic arm manipulations
# 轨迹插补       : path interpolation
# 假人操作       : bummy manipulations
# 通信          : communications
# 辅助函数      :  helper functions

# import libraries
import vrep
import math
import time
import numpy as np
import numpy.linalg as lg

# constants and DH parameters
PI = math.pi
d = np.array([0.089159,  0,      0,        0.10915,  0.09465,  0.0823])
a = np.array([0,         0.425,  0.39225,  0,        0,        0])
joint_angles = [0.0,0.0,0.0,0.0,0.0,0.0]
tool_length = 0.23
wait_time = 0

# ID and handles
clientID = 0
joint_handles = np.array(6, dtype=int)
welding_torch_handle = 0

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
    euler = np.array([a, b, g])
    return euler # 之后要用matrix来打包

def euler2rotm(a, b, g):
    rot_x = np.matrix([[1,  0,          0        ],
                       [0,  np.cos(a), -np.sin(a)],
                       [0,  np.sin(a),  np.cos(a)]])
    rot_y = np.matrix([[ np.cos(b),  0,  np.sin(b)],
                       [ 0,          1,  0        ],
                       [-np.sin(b),  0,  np.cos(b)]])
    rot_z = np.matrix([[np.cos(g), -np.sin(g),  0],
                       [np.sin(g),  np.cos(g),  0],
                       [0,          0,          1]])
    temp = np.matmul(rot_y, rot_z)
    mat = np.matmul(rot_x, temp)
    return mat

# 四元数可以平滑地表示姿态，不会出现突变问题（本项目中采用的四元数为Hamilton形式，即右手系）
def rotm2quat(mat):
    w = mat[0,0] + mat[1,1] + mat[2,2]
    x = mat[0,0] - mat[1,1] - mat[2,2]
    y = -mat[0,0] + mat[1,1] - mat[2,2]
    z = -mat[0,0] - mat[1,1] + mat[2,2]
    axis = max(w, x, y, z)
    if (w == axis):
        w = math.sqrt(mat[0,0] + mat[1,1] + mat[2,2] + 1) / 2
        x = (mat[1,2] - mat[2,1]) / (4 * w)
        y = (mat[2,0] - mat[0,2]) / (4 * w)
        z = (mat[0,1] - mat[1,0]) / (4 * w)
    elif (x == axis):
        x = math.sqrt(mat[0,0] - mat[1,1] - mat[2,2]+1) / 2
        w = (mat[1,2] - mat[2,1]) / (4 * x)
        y = (mat[0,1] + mat[1,0]) / (4 * x)
        z = (mat[2,0] + mat[0,2]) / (4 * x)
    elif (y == axis):
        y = math.sqrt(-mat[0,0] + mat[1,1] - mat[2,2] + 1) / 2
        w = (mat[2,0] - mat[0,2]) / (4 * y)
        x = (mat[0,1] + mat[1,0]) / (4 * y)
        z = (mat[1,2] + mat[2,1]) / (4 * y)
    else:
        z = math.sqrt(-mat[0,0] - mat[1,1] + mat[2,2] + 1) / 2
        w = (mat[0,1] - mat[1,0]) / (4 * z)
        x = (mat[2,0] + mat[0,2]) / (4 * z)
        y = (mat[1,2] + mat[2,1]) / (4 * z)
    quat = np.array([w, x, y, z])
    return quat

def quat2rotm(quat):
    # 解包
    w, x, y, z = quat
    mat = np.matrix([[w**2 + x**2 - y**2 - z**2,  2 * (x * y - w * z),        2 * ( x * z + w * y)     ],
                     [2 * (x*y + w*z),            w**2 - x**2 + y**2 - z**2,  2 * (y * z - w * x)      ],
                     [2 * (x*z - w*y),            2 * (y * z + w * x),        w**2 - x**2 - y**2 + z**2]])
    # 单位化
    mat[0:3,0] =  mat[0:3,0] / lg.norm(mat[0:3,0])
    mat[0:3,1] =  mat[0:3,1] / lg.norm(mat[0:3,1])
    mat[0:3,2] =  mat[0:3,2] / lg.norm(mat[0:3,2])
    # 上述过程是根据JPL四元数得到的旋转矩阵，与Hamilton形式的变换互为转置关系
    return mat.transpose()

''' frame transformations '''

def T01(rad):
    mat = np.matrix([[0,  -math.sin(rad),  -math.cos(rad),   0   ],
                     [0,   math.cos(rad),  -math.sin(rad),   0   ],
                     [1,   0,               0,               d[0]],
                     [0,   0,               0,               1   ]])
    return mat

def T12(rad):
    mat = np.matrix([[math.cos(rad),  -math.sin(rad),   0,   a[1]*math.cos(rad)],
                     [math.sin(rad),   math.cos(rad),   0,   a[1]*math.sin(rad)],
                     [0,               0,               1,   0                 ],
                     [0,               0,               0,   1                 ]])
    return mat

def T23(rad):
    mat = np.matrix([[math.cos(rad),  -math.sin(rad),   0,   a[2]*math.cos(rad)],
                     [math.sin(rad),   math.cos(rad),   0,   a[2]*math.sin(rad)],
                     [0,               0,               1,   0                 ],
                     [0,               0,               0,   1                 ]])
    return mat

def T34(rad):
    mat = np.matrix([[ 0,  -math.sin(rad),  math.cos(rad),   0   ],
                     [ 0,   math.cos(rad),  math.sin(rad),   0   ],
                     [-1,   0,              0,               d[3]],
                     [ 0,   0,              0,               1   ]])
    return mat

def T45(rad):
    mat = np.matrix([[0,  -math.sin(rad),  -math.cos(rad),   0   ],
                     [0,   math.cos(rad),  -math.sin(rad),   0   ],
                     [1,   0,               0,               d[4]],
                     [0,   0,               0,               1   ]])
    return mat

def T56(rad):
    mat = np.matrix([[math.cos(rad),  -math.sin(rad),   0,   0   ],
                     [math.sin(rad),   math.cos(rad),   0,   0   ],
                     [0,               0,               1,   d[5]],
                     [0,               0,               0,   1   ]])
    return mat

def T6t(tool_length):
    mat = np.matrix([[1,   0,   0,   0           ],
                     [0,   1,   0,   0           ],
                     [0,   0,   1,   tool_length ],
                     [0,   0,   0,   1           ]])
    return mat

''' robotic arm motion resoutions '''

# 在python中使用 *args 来进行函数的重载，不过要注意类型的转换
def forward_kinematics(rad1, rad2, rad3, rad4, rad5, rad6):
    Tmat_01 = T01(rad1)
    Tmat_12 = T12(rad2)
    Tmat_23 = T23(rad3)
    Tmat_34 = T34(rad4)
    Tmat_45 = T45(rad5)
    Tmat_56 = T56(rad6)
    Tmat_6t = T6t(tool_length)
    T = Tmat_01 * Tmat_12 * Tmat_23 * Tmat_34 * Tmat_45 * Tmat_56 * Tmat_6t
    return T

def jacobian(rads):
    # initialize
    J = np.asmatrix(np.zeros((7,6), dtype = float))
    drad = 0.001 # perturbation value
    # numerical dirivative is given by f'(x) = [f(x+dx)-f(x)]/dt
    mat_cur = forward_kinematics(rads[0],rads[1],rads[2],rads[3],rads[4],rads[5])
    pos_cur = mat_cur[0:3,3]
    ori_cur = np.asmatrix(rotm2quat(mat_cur)).reshape(4,1)
    vec_cur = np.vstack((pos_cur, ori_cur))
    for i in range(0,6):
        rads_per = rads.copy()
        rads_per[i] = rads_per[i] + drad
        mat_per = forward_kinematics(rads_per[0],rads_per[1],rads_per[2],rads_per[3],rads_per[4],rads_per[5])
        pos_per = mat_per[0:3,3]
        ori_per = np.asmatrix(rotm2quat(mat_per)).reshape(4,1)
        vec_per = np.vstack((pos_per, ori_per))
        J[0:7,i] = (vec_per - vec_cur) / drad
    return J

# 注意array, matrix, list三者之间的转换
def inverse_kinematics(mat_goal):
    iteration = 0
    # current cartesian position and quaternion orientation vector from get_current_vector
    rad_cur = np.asmatrix(joint_angles)
    vec_cur = get_current_vector(welding_torch_handle)
    # goal matrix to cartesian position and quaternion orientation vector
    pos_goal = mat_goal[0:3,3]
    ori_goal = np.asmatrix(rotm2quat(mat_goal)).reshape(4,1)
    vec_goal = np.vstack((pos_goal, ori_goal))
    while (iteration < 100):
        iteration = iteration + 1
        vec_err = vec_goal - vec_cur
        if (lg.norm(vec_err) < 0.003):
            rad_cur = rad_cur.tolist()
            move_joint_rad(rad_cur[0])
            #print("Iteration = " + str(iteration))
            break
        # iteration of joint angles through Jacobian
        rad_cur = rad_cur.tolist()
        J = jacobian(rad_cur[0])
        rad_cur = np.asmatrix(rad_cur)
        f = lg.solve(J.dot(J.transpose()) + 0.04 * np.identity(7), vec_err)
        dq = np.dot(J.transpose(), f).reshape(1,6)
        rad_cur = rad_cur + dq
        mat_cur = forward_kinematics(rad_cur[0,0],rad_cur[0,1],rad_cur[0,2],rad_cur[0,3],rad_cur[0,4],rad_cur[0,5])
        pos_cur = mat_cur[0:3,3]
        ori_cur = np.asmatrix(rotm2quat(mat_cur)).reshape(4,1)
        vec_cur = np.vstack((pos_cur, ori_cur))
    if (iteration > 100):
        print("loop too many times")

''' robotic arm manipulations '''

def move_joint_deg(target_angles):
    vrep.simxSetJointTargetPosition(clientID,joint_handles[0],deg2rad(target_angles[0]),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handles[1],deg2rad(target_angles[1]),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handles[2],deg2rad(target_angles[2]),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handles[3],deg2rad(target_angles[3]),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handles[4],deg2rad(target_angles[4]),vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handles[5],deg2rad(target_angles[5]),vrep.simx_opmode_oneshot)
    joint_angles = target_angles

def move_joint_rad(target_angles):
    vrep.simxSetJointTargetPosition(clientID,joint_handles[0],target_angles[0],vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handles[1],target_angles[1],vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handles[2],target_angles[2],vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handles[3],target_angles[3],vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handles[4],target_angles[4],vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,joint_handles[5],target_angles[5],vrep.simx_opmode_oneshot)
    joint_angles = target_angles

''' path interpolation '''

def lerp(current_pos_ori, goal_pos_ori):
    current_pos = current_pos_ori[0:3,3]
    goal_pos = goal_pos_ori[0:3,3]
    velocity = 5e-2 / 20 # 1cm/s divided into 50ms steps
    error_matrix = goal_pos_ori - current_pos_ori
    error_len = np.linalg.norm(error_matrix)
    N = int((error_len / velocity)+1)
    print("N in lerp = " + str(N))
    dx = (goal_pos[0] - current_pos[0]) / N
    dy = (goal_pos[1] - current_pos[1]) / N
    dz = (goal_pos[2] - current_pos[2]) / N
    # orientation
    Q1 = rotm2quat(current_pos_ori)
    Q2 = rotm2quat(goal_pos_ori)
    for i in range(1, N+1):
        t = i / N
        print("Progress: " + str(format(100*t,".1f")) + "%")
        current_pos_ori[0,3] = current_pos_ori[0,3] + dx
        current_pos_ori[1,3] = current_pos_ori[1,3] + dy
        current_pos_ori[2,3] = current_pos_ori[2,3] + dz
        Qt = (1-t)*Q1 + t*Q2
        rotm = quat2rotm(Qt)
        current_pos_ori[0:3,0:3] = rotm
        inverse_kinematics(current_pos_ori)
    error_matrix = goal_pos_ori - current_pos_ori
    error_len = np.linalg.norm(error_matrix)
    return

def draw_circle(current_pos_ori, radius):
    # velocity should be set in meters per second, then converted to distance per 50ms(step in simulation)
    center_pos = current_pos_ori[0:3,3]
    center_x = center_pos[0].copy() # 注意深浅复制的区别
    center_y = center_pos[1].copy()
    center_z = center_pos[2].copy()
    print("x: " + str(center_x))
    print("y: " + str(center_y))
    print("z: " + str(center_z))
    circumference = 2 * math.pi * radius
    velocity = 5e-2 / 20 # 1cm/s divided into 50ms steps
    N = int((circumference / velocity)+1)
    print("N in circle = " + str(N))
    dtheta = 2 * math.pi / N
    theta = 0
    for i in range(0, N+1):
        t = i / N
        print("Progress: " + str(format(100*t,".1f")) + "%")
        print("radius: " + str(radius))
        print("theta: " + str(theta))
        current_x = center_x + radius * math.cos(theta)
        current_y = center_y + radius * math.sin(theta)
        print("current_x : " + str(current_x))
        print("current_y : " + str(current_y))
        theta = theta + dtheta
        current_pos_ori[0,3] = current_x
        current_pos_ori[1,3] = current_y
        inverse_kinematics(current_pos_ori)
        time.sleep(0.02)
    return

''' bummy manipulations '''

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

''' Communications '''

def connect():
    # declare global
    global clientID
    global joint_handles
    global welding_torch_handle
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
    status, welding_torch_handle = vrep.simxGetObjectHandle(clientID, 'Welding_torch', vrep.simx_opmode_blocking)
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
    return clientID, joint_handles, welding_torch_handle

def disconnect():
    vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot)
    vrep.simxGetPingTime(clientID)
    vrep.simxFinish(clientID)

''' helper functions '''

def get_current_vector(object_handle):
    # get
    status, pos_cur = vrep.simxGetObjectPosition(clientID, object_handle, -1, vrep.simx_opmode_blocking)
    if status != vrep.simx_return_ok:
        raise Exception("Cannot get position of end effector")
    status, ori_cur = vrep.simxGetObjectQuaternion(clientID, object_handle, -1, vrep.simx_opmode_blocking)
    if status != vrep.simx_return_ok:
        raise Exception("Cannot get orientation of end effector")
    # reshape
    vec_cur = np.vstack((np.asmatrix(pos_cur).reshape(3,1), np.asmatrix(ori_cur).reshape(4,1)))
    return vec_cur

def get_current_joints():
    global wait_time
    start = time.time()
    joint_angles = [0.0,0.0,0.0,0.0,0.0,0.0]
    _, joint_angles[0] = vrep.simxGetJointPosition(clientID, joint_handles[0], vrep.simx_opmode_blocking)
    _, joint_angles[1] = vrep.simxGetJointPosition(clientID, joint_handles[1], vrep.simx_opmode_blocking)
    _, joint_angles[2] = vrep.simxGetJointPosition(clientID, joint_handles[2], vrep.simx_opmode_blocking)
    _, joint_angles[3] = vrep.simxGetJointPosition(clientID, joint_handles[3], vrep.simx_opmode_blocking)
    _, joint_angles[4] = vrep.simxGetJointPosition(clientID, joint_handles[4], vrep.simx_opmode_blocking)
    _, joint_angles[5] = vrep.simxGetJointPosition(clientID, joint_handles[5], vrep.simx_opmode_blocking)
    end = time.time()
    time_dif = end - start
    wait_time = wait_time + time_dif
    print("this is time spent waiting: " + str(wait_time))

    return joint_angles
