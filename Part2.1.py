import Part1 as p1
from Methods import *
import cv2
import matplotlib.pyplot as plt

def frequency_list(img):
    freq_list,pixel_list = [],[]
    for i in range(0, 3):
        channel = get_single_channel_matrix(img, i)
        rowbound, colbound = len(channel), len(channel[0])
        for row in range(0, rowbound):
            for col in range(0, colbound):
                pixel_list.append(float(channel[row][col]))

    for c in range(0,255):
        freq_list.append(count_color_freq(c,pixel_list))
    return freq_list

def count_color_freq(color,pixel_list):
    freq = 0
    for i in pixel_list:
        if i == color:
            freq += 1
    return freq

def pick_threhold(freq_list):
    thre = 999
    for i in range(30,225):
        left, right = 0,0
        for offset in range(0,30):
            left += freq_list[i-offset]
            right += freq_list[i+offset]
        divisor = float(float(left) / right)
        if divisor < 2 and divisor > 1.80 and divisor < thre:
            thre = i
    return thre

def apply_thre_on_img(threshold,img):
    full_new_graph = []

    for i in range(0, 3):
        channel = get_single_channel_matrix(img, i)
        new_channel = []
        rowbound, colbound = len(channel), len(channel[0])
        for row in range(0, rowbound):
            new_row = []
            for col in range(0, colbound):
                s = 0
                if channel[row][col] >= threshold:
                    s = 254
                new_row.append(s)
            new_channel.append(new_row)

        full_new_graph.append(new_channel)

    new_img = merge_channels(np.array(full_new_graph))
    return new_img

if __name__ == '__main__':
    hubble = cv2.imread('./Images/hubble-output.tif')
    # mean_hubble = p1.mean_filter(hubble)

    freq_list = frequency_list(hubble)
    thre = pick_threhold(freq_list)
    print ('threshold ',thre)
    thre_hubble = apply_thre_on_img(thre,hubble)
    cv2.imwrite('./Images/hubble-threshold-output.tif', thre_hubble)