import os
import sys

import cv2
import numpy as np

input_file = 'letter.data'


#define visualization paramters

img_resize_factor = 12
start = 6
end = -1
height,width = 16,8

with open(input_file, 'r') as f:
    for line in f.readlines():
        data = np.array([255 * float(x) for x in line.split('\t')[start:end]])
        #Reshape the data into a 2D image
        img = np.reshape(data, (height, width))
        #Scale the image
        img_scaled = cv2.resize(img, None,fx=img_resize_factor,fy=img_resize_factor)
        #Display the image
        cv2.imshow('Image', img_scaled)

        c = cv2.waitKey()
        if c == 27:
            break