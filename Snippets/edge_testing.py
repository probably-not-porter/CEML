import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
import argparse
import glob

import cv2
import matplotlib.pyplot as plt

import time

# This is my testing file for different edge detectors
# Should be similar to the edge_detectors.py, but less
# formatted and cleaned up, and not hooked into the GUI.

def file_controller(in_path, out_path):
    """ ---------- pre-process image ---------- """
    image = cv2.imread(in_path) 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    """ ---------- create cv2 canny detections ---------- """
    start = time.time()
    cannywide = cv2.Canny(blurred, 10, 200)
    end = time.time()
    print("canny_wide: " + str(end - start))
    
    start = time.time()
    cannytight = cv2.Canny(blurred, 225, 250)
    end = time.time()
    print("canny_tight: " + str(end - start))

    start = time.time()
    cannyauto = auto_canny(blurred)              # uses auto_canny function with sigma
    end = time.time()
    print("canny_auto: " + str(end - start))

    """ ---------- create laplacian detection ---------- """
    start = time.time()
    lap = cv2.Laplacian(blurred,cv2.CV_64F)
    end = time.time()
    print("laplacian: " + str(end - start))

    """ ---------- create sobel operations ---------- """
    start = time.time()
    sobelx = cv2.Sobel(blurred,cv2.CV_64F,1,0,ksize=5)  # x
    end = time.time()
    print("sobel_x: " + str(end - start))

    start = time.time()
    sobely = cv2.Sobel(blurred,cv2.CV_64F,0,1,ksize=5)  # y
    end = time.time()
    print("sobel_y: " + str(end - start))

    """ ---------- create prewitt operator ---------- """
    start = time.time()
    prewitt = ndi.prewitt(blurred)    
    end = time.time()
    print("prewitt: " + str(end - start))

    """ ---------- write detections to files ---------- """
    start = time.time()
    cv2.imwrite(out_path + '_canny_auto.jpg', cannyauto)
    cv2.imwrite(out_path + '_canny_tight.jpg', cannytight)
    cv2.imwrite(out_path + '_canny_wide.jpg', cannywide)
    cv2.imwrite(out_path + '_laplacian.jpg', lap)
    cv2.imwrite(out_path + '_sobel_x.jpg', sobelx)
    cv2.imwrite(out_path + '_sobel_y.jpg', sobely)
    cv2.imwrite(out_path + '_prewitt.jpg', prewitt)
    end = time.time()
    print("Writing images out: " + str(end - start))


def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
 
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
 
	# return the edged image
	return edged


# test case
test_image_path = "/home/porter/Dev/SRSD/images/vli_1.JPG"
test_out_path = "/home/porter/Dev/SRSD/test_images/stod_2018"
file_controller(test_image_path,test_out_path)
