import numpy as np
from scipy import ndimage as ndi
import argparse
import glob
import cv2
import matplotlib.pyplot as plt
import time

def image_preprocess(in_path):
    """ Takes a directory path, returns three base versions of image. """
    image = cv2.imread(in_path) 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    return blurred

def canny_wide(in_path, out_path):
    """ Take a directory path, writes result to another path """
    print("Creating canny_wide...")
    start = time.time() # timer start

    img = image_preprocess(in_path)
    cannywide = cv2.Canny(img, 10, 200)
    cv2.imwrite(out_path + '_canny_wide.jpg', cannywide)

    end = time.time() # timer end
    print("total time: " + str(round(end - start, 2)))

def canny_tight(in_path, out_path):
    """ Take a directory path, writes result to another path """
    print("Creating canny_tight...")
    start = time.time() # timer start

    img = image_preprocess(in_path)
    cannytight = cv2.Canny(img, 225, 250)
    cv2.imwrite(out_path + '_canny_tight.jpg', cannytight)

    end = time.time() # timer end
    print("total time: " + str(round(end - start, 2)))

def canny_auto(in_path, out_path, sigma=0.33):
    """ Take a directory path, writes result to another path """
    print("Creating canny_auto...")
    start = time.time() # timer start

    img = image_preprocess(in_path)
    v = np.median(img)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    cannyauto = cv2.Canny(img, lower, upper)
    cv2.imwrite(out_path + '_canny_auto.jpg', cannyauto)

    end = time.time() # timer end
    print("total time: " + str(round(end - start, 2)))

def laplacian(in_path, out_path):
    """ Take a directory path, writes result to another path """
    print("Creating laplacian...")
    start = time.time() # timer start

    img = image_preprocess(in_path)
    lap = cv2.Laplacian(img,cv2.CV_64F)
    cv2.imwrite(out_path + '_laplacian.jpg', lap)

    end = time.time() # timer end
    print("total time: " + str(round(end - start, 2)))

def sobel_x(in_path, out_path):
    """ Take a directory path, writes result to another path """
    print("Creating sobel_x...")
    start = time.time() # timer start

    img = image_preprocess(in_path)
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
    cv2.imwrite(out_path + '_sobel_x.jpg', sobelx)

    end = time.time() # timer end
    print("total time: " + str(round(end - start, 2)))

def sobel_y(in_path, out_path):
    """ Take a directory path, writes result to another path """
    print("Creating sobel_y...")
    start = time.time() # timer start

    img = image_preprocess(in_path)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y
    cv2.imwrite(out_path + '_sobel_y.jpg', sobely)

    end = time.time() # timer end
    print("total time: " + str(round(end - start, 2)))

def prewitt(in_path, out_path):
    """ Take a directory path, writes result to another path """
    print("Creating prewitt...")
    start = time.time() # timer start

    img = image_preprocess(in_path)
    p = ndi.prewitt(img) 
    cv2.imwrite(out_path + '_prewitt.jpg', p)

    end = time.time() # timer end
    print("total time: " + str(round(end - start, 2)))

# test case
test_image_path = "/home/porter/Dev/SRSD/paper_images/original.JPG"
test_out_path = "/home/porter/Dev/SRSD/paper_images/stod_2018"

# function tests
canny_auto(test_image_path,test_out_path)
canny_wide(test_image_path,test_out_path)
canny_tight(test_image_path,test_out_path)
laplacian(test_image_path,test_out_path)
sobel_x(test_image_path,test_out_path)
sobel_y(test_image_path,test_out_path)
prewitt(test_image_path,test_out_path)