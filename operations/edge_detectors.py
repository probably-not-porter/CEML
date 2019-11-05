import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi

import cv2
import matplotlib.pyplot as plt

def caney_edge(image, outdir):
    im = cv2.imread(image)
    edges = cv2.Canny(im,50,100,L2gradient=True)
    plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    fig = plt.figure(frameon=False)
    fig.set_size_inches(10,8)

    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    for ax in plt.gcf().axes:
        ax.get_lines()[0].set_color("black")
    fig.add_axes(ax)
    ax.imshow(edges)
    fig.savefig(outdir,facecolor='w', edgecolor='w', dpi=400)

def caney_edge_test(image, outdir,x):
    im = cv2.imread(image)
    edges = cv2.Canny(im,90,110,100,L2gradient=False)
    plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    fig = plt.figure(frameon=False)
    fig.set_size_inches(10,8)

    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    for ax in plt.gcf().axes:
        ax.get_lines()[0].set_color("black")
    fig.add_axes(ax)
    ax.imshow(edges)
    fig.savefig(outdir,facecolor='w', edgecolor='w', dpi=1000)

for x in range(1):
    print(x)
    caney_edge_test("/home/porter/Dev/SRSD/images/DJI_0018.JPG", "/home/porter/Dev/SRSD/test_images/test" + str(x),x)