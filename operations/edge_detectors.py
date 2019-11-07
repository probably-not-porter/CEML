import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi

import cv2
import matplotlib.pyplot as plt

import time

def caney_edge(image, outdir):
    my_dpi = 1000
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



def caney_edge_test(image, outdir): # testing version of caney function, times execution.
    start = time.time()
    myres = 1000
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
    print("Total time: " + end - start)




caney_edge_test("/home/porter/Dev/SRSD/images/DJI_0018.JPG", "/home/porter/Dev/SRSD/test_images/test")
