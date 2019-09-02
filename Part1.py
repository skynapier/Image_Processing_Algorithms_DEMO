import cv2
import numpy as np
import math
import fractions
from Methods import *


def edge(img):
    full_new_graph = []
    row_mask = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    col_mask = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])

    for i in range(0, 3):
        channel = get_single_channel_matrix(img, i)

        new_channel = []
        rowbound, colbound = len(channel), len(channel[0])
        for row in range(0, rowbound):
            new_row = []
            for col in range(0, colbound):
                temp_matrix = create_temp_matrix(row, col, channel, rowbound, colbound)
                s1 = inner_product(row_mask, temp_matrix)
                s2 = inner_product(col_mask, temp_matrix)
                new_s = math.sqrt((s1 ** 2 + s2 ** 2))

                new_row.append(new_s)
            new_channel.append(new_row)

        full_new_graph.append(new_channel)

    new_img = merge_channels(np.array(full_new_graph))
    return new_img

def Enhance(img):
    full_new_graph = []
    e_mask = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])


    for i in range(0, 3):
        channel = get_single_channel_matrix(img, i)

        new_channel = []
        rowbound, colbound = len(channel), len(channel[0])
        for row in range(0, rowbound):
            new_row = []
            for col in range(0, colbound):
                temp_matrix = create_temp_matrix(row, col, channel, rowbound, colbound)
                s = inner_product(e_mask, temp_matrix)

                new_row.append(s)
            new_channel.append(new_row)

        full_new_graph.append(new_channel)

    new_img = merge_channels(np.array(full_new_graph))
    return new_img

def mean_filter(img):
    full_new_graph = []
    e = fractions.Fraction(1, 9)
    mean_mask = np.array([[e, e, e],
                          [e, e, e],
                          [e, e, e]])

    for i in range(0, 3):
        channel = get_single_channel_matrix(img, i)
        new_channel = []
        rowbound, colbound = len(channel), len(channel[0])
        for row in range(0, rowbound):
            new_row = []
            for col in range(0, colbound):
                temp_matrix = create_temp_matrix(row, col, channel, rowbound, colbound)
                s = float(inner_product(mean_mask, temp_matrix))
                new_row.append(s)
            new_channel.append(new_row)

        full_new_graph.append(new_channel)

    new_img = merge_channels( np.array(full_new_graph) )
    return new_img

def median_filter(img):
    full_new_graph = []

    for i in range(0, 3):
        channel = get_single_channel_matrix(img, i)
        new_channel = []
        rowbound, colbound = len(channel), len(channel[0])
        for row in range(0, rowbound):
            new_row = []
            for col in range(0, colbound):
                temp_matrix = create_temp_matrix(row, col, channel, rowbound, colbound)
                s = median_matrix(temp_matrix)
                new_row.append(s)
            new_channel.append(new_row)

        full_new_graph.append(new_channel)

    new_img = merge_channels( np.array(full_new_graph) )
    return new_img


if __name__ == '__main__':

    #Part 1.1 Edge Detection
    edge_im = cv2.imread('./Images/test-pattern.tif')
    new_edge_im = edge(edge_im)
    cv2.imwrite('./Images/test-pattern-output.tif',new_edge_im)

    # Part 1.3 Enhancement
    enhan_im = cv2.imread('./Images/blurry-moon.tif')
    new_enhan_im = Enhance(enhan_im)
    cv2.imwrite('./Images/blurry-moon-output.tif', new_enhan_im)

    #Part 1.2 Noise
    noise_im = cv2.imread('./Images/ckt-board-saltpep.tif')

    mean_noise_im, median_noise_im = mean_filter(noise_im), median_filter(noise_im)

    cv2.imwrite('./Images/ckt-board-saltpep-mean-output.tif', mean_noise_im)
    cv2.imwrite('./Images/ckt-board-saltpep-median-output.tif', median_noise_im)


