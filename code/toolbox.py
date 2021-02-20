# 工具箱简介    : toolbox content summary
# 弧角转换      : radian - degree transformations
# 位姿表达转换   : orientation representation transformations
# 参照系变换     : frame transformations
# 机械臂操作     : robotics arm manipulations
# 假人操作       : bummy manipulations
# 通信          : communications

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
tool_length = 0.13

# ID and handles
clientID = 0
joint_handles = [0,0,0,0,0,0]
end_effector_handle = 0

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

''' robotics arm manipulations '''

# 在python中使用 *args 来进行函数的重载，不过要注意类型的转换
def forward_kinematics(*args):
    if len(args) == 1:
        rads = deg2rad(args[0])
        Tmat_01 = T01(rads[0])
        Tmat_12 = T12(rads[1])
        Tmat_23 = T23(rads[2])
        Tmat_34 = T34(rads[3])
        Tmat_45 = T45(rads[4])
        Tmat_56 = T56(rads[5])
        Tmat_6t = T6t(tool_length)
        T = Tmat_01 * Tmat_12 * Tmat_23 * Tmat_34 * Tmat_45 * Tmat_56 * Tmat_6t
        return T
    elif len(args) == 6:
        degs = np.array([args[0], args[1], args[2], args[3], args[4], args[5]])
        return forward_kinematics(degs)
    else:
        raise Exception("numbers of parameters do not match function requirement")

def current_vector(object_handle):
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

def jacobian(degs):
    J = np.asmatrix(np.zeros((7,6), dtype = float))
    #print(type(J))
    #print(J)
    ddeg = 1
    mat_cur = forward_kinematics(degs)
    #print(mat_cur)
    pos_cur = mat_cur[0:3,3]
    #print(pos_cur)
    ori_cur = np.asmatrix(rotm2quat(mat_cur)).reshape(4,1)
    #print(ori_cur)
    vec_cur = np.vstack((pos_cur, ori_cur))
    # print(vec_cur)
    for i in range(0,6):
        #print(i)
        degs_per = degs.copy()
        #print(degs)
        #print(degs_per)
        degs_per[i] = degs_per[i] + ddeg
        #print("this is degs_per: ")
        #print(degs_per)
        mat_per = forward_kinematics(degs_per)
        pos_per = mat_per[0:3,3]
        ori_per = np.asmatrix(rotm2quat(mat_per)).reshape(4,1)
        vec_per = np.vstack((pos_per, ori_per))
        #print(type(vec_per))
        #print("this is vec_per: ")
        #print(vec_per)
        J[0:7,i] = (vec_per - vec_cur) / ddeg
    #print(J)
    return J

def inverse_kinematics(mat):
    count = 0
    while (count < 600):
        count = count + 1
        for i in range(0,6):
            current_angles[i] = goal_angles[i]
        current_T = forward_kinematics(current_angles[0],current_angles[1],current_angles[2],current_angles[3],current_angles[4],current_angles[5])
        current_P = current_T[0:3,3]
        current_R = np.asmatrix(rotm2quat(current_T))
        current_R = current_R.reshape((4,1))
        current_PR_mat = np.vstack((current_P,current_R))
        goal_P = pos_ori_mat[0:3,3]
        goal_R = np.asmatrix(rotm2quat(pos_ori_mat))
        goal_R = goal_R.reshape((4,1))
        goal_PR_mat = np.vstack((goal_P,goal_R))
        error_vector = goal_PR_mat - current_PR_mat
        if (np.linalg.norm(error_vector) < 0.003):
            Move_to_joint_position_rad(goal_angles[0],goal_angles[1],goal_angles[2],goal_angles[3],goal_angles[4],goal_angles[5])
            break
        # perterbation
        perturbation_T1 = forward_kinematics(current_angles[0]+dtheta,current_angles[1],current_angles[2],current_angles[3],current_angles[4],current_angles[5])
        perturbation_T2 = forward_kinematics(current_angles[0],current_angles[1]+dtheta,current_angles[2],current_angles[3],current_angles[4],current_angles[5])
        perturbation_T3 = forward_kinematics(current_angles[0],current_angles[1],current_angles[2]+dtheta,current_angles[3],current_angles[4],current_angles[5])
        perturbation_T4 = forward_kinematics(current_angles[0],current_angles[1],current_angles[2],current_angles[3]+dtheta,current_angles[4],current_angles[5])
        perturbation_T5 = forward_kinematics(current_angles[0],current_angles[1],current_angles[2],current_angles[3],current_angles[4]+dtheta,current_angles[5])
        perturbation_T6 = forward_kinematics(current_angles[0],current_angles[1],current_angles[2],current_angles[3],current_angles[4],current_angles[5]+dtheta)
        # extraction
        perturbation_P1 = perturbation_T1[0:3,3]
        perturbation_P2 = perturbation_T2[0:3,3]
        perturbation_P3 = perturbation_T3[0:3,3]
        perturbation_P4 = perturbation_T4[0:3,3]
        perturbation_P5 = perturbation_T5[0:3,3]
        perturbation_P6 = perturbation_T6[0:3,3]
        perturbation_R1 = np.asmatrix(rotm2quat(perturbation_T1)).reshape((4,1))
        perturbation_R2 = np.asmatrix(rotm2quat(perturbation_T2)).reshape((4,1))
        perturbation_R3 = np.asmatrix(rotm2quat(perturbation_T3)).reshape((4,1))
        perturbation_R4 = np.asmatrix(rotm2quat(perturbation_T4)).reshape((4,1))
        perturbation_R5 = np.asmatrix(rotm2quat(perturbation_T5)).reshape((4,1))
        perturbation_R6 = np.asmatrix(rotm2quat(perturbation_T6)).reshape((4,1))
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
        Jacobian3 = (perturbation_PR_mat3 - current_PR_mat)/dtheta
        Jacobian4 = (perturbation_PR_mat4 - current_PR_mat)/dtheta
        Jacobian5 = (perturbation_PR_mat5 - current_PR_mat)/dtheta
        Jacobian6 = (perturbation_PR_mat6 - current_PR_mat)/dtheta
        # Jacobian matrix
        Jacobian = np.hstack((Jacobian1,Jacobian2,Jacobian3,Jacobian4,Jacobian5,Jacobian6))
        Jacobian_trans = Jacobian.transpose()
        f = np.linalg.solve(Jacobian.dot(Jacobian_trans) + 0.04 * np.identity(7), error_vector)
        dq = np.dot(Jacobian_trans, f)
        for i in range(0,6):
            goal_angles[i] = current_angles[i] + dq[i]
    if (count > 200):
        print('loop too many times')
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

def Disconnect(clientID):
    vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot)
    time.sleep(1)
    vrep.simxFinish(clientID)