import numpy as np
import math

def get_single_channel_matrix(image,channel_idx):
    channel = image[:,:,channel_idx]
    return channel

def inner_product(matrix1, matrix2):
    "the matrix1 and matrix2 must in the same shape and be a symmetric matix"
    sum = 0
    for row in range(0,len(matrix1)):
        for col in range(0, len(matrix1)):
            sum += matrix1[row][col] * matrix2[row][col]
    return sum

def create_temp_matrix(centre_row,centre_col,matrix,rowbound,colbound):
    temp_matrx = []
    for row in range(centre_row - 1, centre_row + 2):
        temp_row = []
        for col in range(centre_col - 1, centre_col + 2):
            if (row < 0 or col < 0):
                temp_row.append(0)
            elif (row >= rowbound or col >= colbound):
                temp_row.append(0)
            else:
                temp_row.append(matrix[row][col])
        temp_matrx.append(temp_row)
    return np.array(temp_matrx)

def merge_channels(f_channel_list):
    new_im = []
    row_bound, col_bound = len(f_channel_list[0]),len(f_channel_list[0][0])
    for row in range(0, row_bound):
        new_row = []
        for col in range(0,col_bound):
            temp = []
            for i in range(0,len(f_channel_list) ):
                channel = f_channel_list[i]

                temp.append(channel[row][col])
            new_row.append(temp)
        new_im.append(new_row)
    ret = np.array(new_im)
    return ret

def copy_channels(channel):
    new_img = []
    for row in range(0, len(channel)):
        new_row = []
        for col in range(0, len(channel)):
            pixel = []
            for i in range(0,3):
                pixel.append( channel[row][col])
            new_row.append(pixel)
        new_img.append(new_row)
    return np.array(new_img)

def median_matrix(matrix):
    temp_list = []
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            temp_list.append(matrix[row][col])
    list.sort(temp_list)
    median = int((len(temp_list) + 1) / 2)
    return temp_list[median]

def list_mean(t_list):
    sum = 0
    for i in t_list:
        sum += i
    mean = float(sum / len(t_list) )
    return mean

def list_std(t_list):
    mean = list_mean(t_list)
    SSE = 0
    for i in t_list:
        residual = float(i - mean)
        SSE += residual ** 2
    std = math.sqrt(SSE)
    return std