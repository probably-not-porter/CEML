import argparse, cv2, os

from PIL import Image
import numpy as np
from scipy import ndimage as ndi

def main(url, cannyAuto = False, cannyWide = False, cannyTight = False, original = False, laplacian = False, sobelX = False, sobelY = False, prewitt = False):

    # Global Settings
    image_urls = {}
    types = []
    sigma=0.33


    # Create a dictionary of original images
    for classifier in os.listdir(url): # loop over each subfolder containing a classifier
        image_urls[classifier] = []
        for image in os.listdir(url + "/" + classifier):
            image_urls[classifier].append(image)
    
    if original:
        types.append("")

    if cannyAuto:
        print("Processing Canny Auto...")
        types.append("-cannyauto")
        if os.path.exists(url +"-cannyauto/") and os.path.isdir(url +"-cannyauto/"):    # check if tmp_path exists
            print("Path already exists!  (" + url +"-cannyauto/"+ ")")
        else:
            os.mkdir(url +"-cannyauto/")
            for key in image_urls:
                os.mkdir(url +"-cannyauto/" + key)
                for image in image_urls[key]:
                    img = cv2.imread(url +"/"+ key +"/"+ image)
                    v = np.median(img)
                    lower = int(max(0, (1.0 - sigma) * v))
                    upper = int(min(255, (1.0 + sigma) * v))
                    cannyauto = cv2.Canny(img, lower, upper)
                    cv2.imwrite(url +"-cannyauto/"+ key +"/"+ image, cannyauto)

    if cannyWide:
        print("Processing Canny Wide...")
        types.append("-cannywide")
        if os.path.exists(url +"-cannywide/") and os.path.isdir(url +"-cannywide/"):    # check if tmp_path exists
            print("Path already exists!  (" + url +"-cannywide/"+ ")")
        else:
            os.mkdir(url +"-cannywide/")
            for key in image_urls:
                os.mkdir(url +"-cannywide/" + key)
                for image in image_urls[key]:
                    img = cv2.imread(url +"/"+ key +"/"+ image)
                    cannywide = cv2.Canny(img, 10, 200)
                    cv2.imwrite(url +"-cannywide/"+ key +"/"+ image, cannywide)

    if cannyTight:
        print("Processing Canny Tight")
    if laplacian:
        print("Processing Laplacian")
    if sobelX:
        print("Processing Sobel (x-axis)")
    if sobelY:
        print("processing Sobel (y-axis)")
    if prewitt:
        print("processing Prewitt")
    
    _create_multichannel_image(types, image_urls, url)

def _create_multichannel_image(types, image_urls, url):
    """ Open multiple images and return a single multi channel image """
    print("Creating Multichannel Composit...")

    if os.path.exists(url +"-cannyauto/") and os.path.isdir(url +"-cannyauto/"):    # check if tmp_path exists
        print("Path already exists!  (" + url +"-composit/"+ ")")

    else:
        os.mkdir(url +"-composit/")
        for key in image_urls:
            os.mkdir(url +"-composit/" + key)
            for image in image_urls[key]:

                a = cv2.imread(url + types[0] + "/" + key + "/" + image, 0)
                b = cv2.imread(url + types[1] + "/" + key + "/" + image, 0)
                c = cv2.imread(url + types[2] + "/" + key + "/" + image, 0)

                """Create a blank image that has three channels 
                and the same number of pixels as your original input"""
                needed_multi_channel_img = np.zeros((a.shape[0], a.shape[1], 3))

                """Add the channels to the needed image one by one"""
                needed_multi_channel_img [:,:,0] = a
                needed_multi_channel_img [:,:,1] = b
                needed_multi_channel_img [:,:,2] = c
                
                cv2.imwrite(url +"-composit/"+ key +"/"+ image, needed_multi_channel_img)

if __name__ == '__main__':
    # Specify Command line args
    parser = argparse.ArgumentParser(description="jpeg altitude histogram")
    parser.add_argument('-i', '--input', help='Enter the directory of your dataset', required=True, dest="inDir")

    parser.add_argument('--canny_auto', help='Turn on preprocessor', action='store_true', dest="cannyAuto")
    parser.add_argument('--canny_wide', help='Turn on preprocessor', action='store_true', dest="cannyWide")
    parser.add_argument('--canny_tight', help='Turn on preprocessor', action='store_true', dest="cannyTight")
    parser.add_argument('--original', help='Turn on preprocessor', action='store_true', dest="original")
    parser.add_argument('--laplacian', help='Turn on preprocessor', action='store_true', dest="laplacian")
    parser.add_argument('--sobel_x', help='Turn on preprocessor', action='store_true', dest="sobelX")
    parser.add_argument('--sobel_y', help='Turn on preprocessor', action='store_true', dest="sobelY")
    parser.add_argument('--prewitt', help='Turn on preprocessor', action='store_true', dest="prewitt")

    args = parser.parse_args()
    # Assign Command line args
    inputDir = args.inDir

    cannyAuto = args.cannyAuto
    cannyTight = args.cannyTight
    cannyWide = args.cannyWide
    original = args.original
    laplacian = args.laplacian
    sobelX = args.sobelX
    sobelY = args.sobelY
    prewitt = args.prewitt

    if sum([cannyAuto, cannyTight, cannyWide, original, laplacian, sobelX, sobelY, prewitt]) > 3:
        print("Too many pre-processors selected. Please use up to 3 at once.")
    elif sum([cannyAuto, cannyTight, cannyWide, original, laplacian, sobelX, sobelY, prewitt]) < 1:
        print("Use flags to select pre-processors. Check the documentation for more information.")
    else:
        main(inputDir, cannyAuto, cannyWide, cannyTight, original, laplacian, sobelX, sobelY, prewitt)