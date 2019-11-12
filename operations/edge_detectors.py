import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi

import cv2
import matplotlib.pyplot as plt

import time

myres = 1000 #output DPI

# hooked up to GUI for tests
def caney_edge(image, outdir):
    im = cv2.imread(image)
    height, width = im.shape[:2]
    edges = cv2.Canny(im,50,100,L2gradient=True)
    plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    fig = plt.figure(frameon=False,figsize=(width // my_dpi, height // my_dpi), dpi=300)

    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    for ax in plt.gcf().axes:
        ax.get_lines()[0].set_color("black")
    fig.add_axes(ax)
    ax.imshow(edges)
    fig.savefig(outdir,facecolor='w', edgecolor='w', dpi=400)


# actual testing implementations


def caney_edge_test(image, outdir): # testing version of caney function, times execution.
    start = time.time()

    im = cv2.imread(image)
    height, width = im.shape[:2]
    edges = cv2.Canny(im,90,110,100,L2gradient=False)
    plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    fig = plt.figure(frameon=False,figsize=(4,3))

    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    for ax in plt.gcf().axes:
        ax.get_lines()[0].set_color("black")
    fig.add_axes(ax)
    ax.imshow(edges)
    fig.savefig(outdir,facecolor='w', edgecolor='w', dpi=myres)
    end = time.time()
    print("Total time: " + str(end - start))

def laplacian_edge_test(image,outdir):
    start = time.time()

    img0 = cv2.imread(image)
    gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(gray,(3,3),0)

    edges = cv2.Laplacian(img,cv2.CV_64F)

    plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    fig = plt.figure(frameon=False,figsize=(4,3))

    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    for ax in plt.gcf().axes:
        ax.get_lines()[0].set_color("black")
    fig.add_axes(ax)
    ax.imshow(edges)
    fig.savefig(outdir,facecolor='white', edgecolor='white', dpi=myres)
    end = time.time()
    print("Total time: " + str(end - start))

def sobel_edge_x_test(image,outdir):
    start = time.time()

    img0 = cv2.imread(image)
    gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(gray,(3,3),0)

    edges = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x

    plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    fig = plt.figure(frameon=False,figsize=(4,3))

    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    for ax in plt.gcf().axes:
        ax.get_lines()[0].set_color("black")
    fig.add_axes(ax)
    ax.imshow(edges)
    fig.savefig(outdir,facecolor='w', edgecolor='w', dpi=myres)
    end = time.time()
    print("Total time: " + str(end - start))

def sobel_edge_y_test(image,outdir):
    start = time.time()

    img0 = cv2.imread(image)
    gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(gray,(3,3),0)

    edges = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y

    plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    fig = plt.figure(frameon=False,figsize=(4,3))

    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    for ax in plt.gcf().axes:
        ax.get_lines()[0].set_color("black")
    fig.add_axes(ax)
    ax.imshow(edges)
    fig.savefig(outdir,facecolor=fig.get_facecolor(), edgecolor='none', dpi=myres)
    end = time.time()
    print("Total time: " + str(end - start))


caney_edge_test("/home/porter/Dev/SRSD/images/car.jpg", "/home/porter/Dev/SRSD/test_images/caney")
sobel_edge_x_test("/home/porter/Dev/SRSD/images/car.jpg", "/home/porter/Dev/SRSD/test_images/sx")
sobel_edge_y_test("/home/porter/Dev/SRSD/images/car.jpg", "/home/porter/Dev/SRSD/test_images/sy")
laplacian_edge_test("/home/porter/Dev/SRSD/images/car.jpg", "/home/porter/Dev/SRSD/test_images/l")

