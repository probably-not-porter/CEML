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