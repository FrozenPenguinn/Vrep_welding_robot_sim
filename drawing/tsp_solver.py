import cv2
import numpy as np
import math
import time
from greedy import solve_tsp
import pickle

def distance(x1, y1, x2, y2):
    '''
    This fucntion calculates the  Euclidian distance between 2 points

    Args:
        x1 (float): X value of the first point
        y1 (float): Y value of the first point
        x2 (float): X value of the second point
        y2 (float): Y value of the secons point

    Returns:
        dist (float): Euclidian distance between point 1 and 2
    '''
    dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return dist

def image_processing_optimization(img = 'birthday_2.png', factor = 1, size = 350):
    '''
    This function process an image obtaining the edges ussing canny.
    It also optimizes the path that will be draw using an ecternal library (tsp-solver).
    Args:
        img (str):
            The desired image source location
        factor (int):
            Reduction or scaling factor (1 is normal, less for reduce (ex 0.5), more increases (1.5))
        size (int):
            The size of the draw (in the given simulation 200 is little and 350 maximum) - but depends of the draw size also

    Returns:
        factor(int):
            Reduction or scaling factor (1 is normal, less for reduce, more increases)
        points (list):
            List of the draw points lists of [x, y] positions
        path (list) :
            Optimized sequence of path for the points list

    Example:
        image_processing_optimization('Images/LAIR.jpg', 1, 200)
    '''
    print("Program running")
    rgb_img = cv2.imread(img)
    x, y, _ = rgb_img.shape
    max_value = max(x, y)

    desired_size = [size, size]
    desired =   [desired_size[0]*(y/max_value),
                desired_size[1]*(x/max_value),
                3]

    scale = [desired[0]/y,
            desired[1]/x]

    rgb_img = cv2.resize(rgb_img,
                        None,
                        fx=scale[0],
                        fy=scale[1],
                        interpolation = cv2.INTER_CUBIC)

    gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray_img, 0, 255, apertureSize = 3)
    cv2.imshow('Image', edges)
    print("Image Processed")

    new_x, new_y, _ = rgb_img.shape
    edges = edges.tolist()

    point_x=[]
    point_y=[]

    for row in range(1, new_y):
        for column in range(1, new_x):
            if edges[column][row] == 255:
                point_x.append(row)
                point_y.append(column)

    points = list(zip(point_x, point_y))
    r  = [[0 for x in range(len(point_x))] for y in range(len(point_x))]

    print(str(len(point_x))+" Points Obtained")

    for p1 in range(1,len(point_x)):
        for p2 in range(1,len(point_x)):
            x1, y1= points[p1]
            x2, y2= points[p2]
            r[p1][p2]=distance(x1,y1,x2,y2)

    print("Distances calculated")


    #TSP - library
    print("Solving TSP")
    path = solve_tsp(r)
    print("TSP Done")

    np_points = np.array(points)
    np_points = np_points*factor
    points = np_points.tolist()

    print("factor = " + str(factor))
    print("new_x = " + str(new_x))
    print("new_y = " + str(new_y))

    file = open(r'./path.pkl', 'wb')
    pickle.dump(path, file)
    file.close()

    file = open(r'./points.pkl', 'wb')
    pickle.dump(points, file)
    file.close()

    return factor, path, points, new_x, new_y

image_processing_optimization()
