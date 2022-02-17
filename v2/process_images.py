import argparse, cv2, os

from PIL import Image
from fastcore.basics import true
import numpy as np
from scipy import ndimage as ndi

def main(url, cannyAuto = False, cannyWide = False, cannyTight = False, original = False, laplacian = False, sobelX = False, sobelY = False, prewitt = False, comp = False):

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
        print("--> Processing Canny Auto...")
        types.append("-cannyauto")
        if os.path.exists(url +"-cannyauto/") and os.path.isdir(url +"-cannyauto/"):    # check if tmp_path exists
            print("--> Path already exists!  (" + url +"-cannyauto/"+ ")")
        else:
            os.mkdir(url +"-cannyauto/")
            for key in image_urls:
                cat_total = len(image_urls[key])
                count = 0
                os.mkdir(url +"-cannyauto/" + key)
                for image in image_urls[key]:
                    count = count + 1
                    img = cv2.imread(url +"/"+ key +"/"+ image)
                    v = np.median(img)
                    lower = int(max(0, (1.0 - sigma) * v))
                    upper = int(min(255, (1.0 + sigma) * v))
                    cannyauto = cv2.Canny(img, lower, upper)
                    cv2.imwrite(url +"-cannyauto/"+ key +"/"+ image, cannyauto)
        print("--> Done.")

    if cannyWide:
        print("--> Processing Canny Wide...")
        types.append("-cannywide")
        if os.path.exists(url +"-cannywide/") and os.path.isdir(url +"-cannywide/"):    # check if tmp_path exists
            print("--> Path already exists!  (" + url +"-cannywide/"+ ")")
        else:
            os.mkdir(url +"-cannywide/")
            for key in image_urls:
                cat_total = len(image_urls[key])
                count = 0
                os.mkdir(url +"-cannywide/" + key)
                for image in image_urls[key]:
                    count = count + 1
                    img = cv2.imread(url +"/"+ key +"/"+ image)
                    cannywide = cv2.Canny(img, 10, 200)
                    cv2.imwrite(url +"-cannywide/"+ key +"/"+ image, cannywide)
        print("--> Done.")

    if cannyTight:
        print("--> Processing Canny Tight")
        types.append("-cannytight")
        if os.path.exists(url +"-cannytight/") and os.path.isdir(url +"-cannytight/"):    # check if tmp_path exists
            print("--> Path already exists!  (" + url +"-cannytight/"+ ")")
        else:
            os.mkdir(url +"-cannytight/")
            for key in image_urls:
                cat_total = len(image_urls[key])
                count = 0
                os.mkdir(url +"-cannytight/" + key)
                for image in image_urls[key]:
                    count = count + 1
                    img = cv2.imread(url +"/"+ key +"/"+ image)
                    cannytight = cv2.Canny(img, 225, 250)
                    cv2.imwrite(url +"-cannytight/"+ key +"/"+ image, cannytight)
        print("--> Done.")

    if laplacian:
        print("--> Processing Laplacian")
        types.append("-laplacian")
        if os.path.exists(url +"-laplacian/") and os.path.isdir(url +"-laplacian/"):    # check if tmp_path exists
            print("--> Path already exists!  (" + url +"-laplacian/"+ ")")
        else:
            os.mkdir(url +"-laplacian/")
            for key in image_urls:
                cat_total = len(image_urls[key])
                count = 0
                os.mkdir(url +"-laplacian/" + key)
                for image in image_urls[key]:
                    count = count + 1
                    img = cv2.imread(url +"/"+ key +"/"+ image)
                    lap = cv2.Laplacian(img,cv2.CV_64F)
                    cv2.imwrite(url +"-laplacian/"+ key +"/"+ image, lap)
        print("--> Done.")

    if sobelX:
        print("--> Processing Sobel (x-axis)")
        types.append("-sobel_x")
        if os.path.exists(url +"-sobel_x/") and os.path.isdir(url +"-sobel_x/"):    # check if tmp_path exists
            print("--> Path already exists!  (" + url +"-sobel_x/"+ ")")
        else:
            os.mkdir(url +"-sobel_x/")
            for key in image_urls:
                cat_total = len(image_urls[key])
                count = 0
                os.mkdir(url +"-sobel_x/" + key)
                for image in image_urls[key]:
                    count = count + 1
                    img = cv2.imread(url +"/"+ key +"/"+ image)
                    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
                    cv2.imwrite(url +"-sobel_x/"+ key +"/"+ image, sobelx)
        print("--> Done.")

    if sobelY:
        print("--> processing Sobel (y-axis)")
        types.append("-sobel_y")
        if os.path.exists(url +"-sobel_y/") and os.path.isdir(url +"-sobel_y/"):    # check if tmp_path exists
            print("--> Path already exists!  (" + url +"-sobel_y/"+ ")")
        else:
            os.mkdir(url +"-sobel_y/")
            for key in image_urls:
                cat_total = len(image_urls[key])
                count = 0
                os.mkdir(url +"-sobel_y/" + key)
                for image in image_urls[key]:
                    count = count + 1
                    img = cv2.imread(url +"/"+ key +"/"+ image)
                    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
                    cv2.imwrite(url +"-sobel_y/"+ key +"/"+ image, sobely)
        print("--> Done.")

    if prewitt:
        print("--> processing Prewitt")
        types.append("-prewitt")
        if os.path.exists(url +"-prewitt/") and os.path.isdir(url +"-prewitt/"):    # check if tmp_path exists
            print("--> Path already exists!  (" + url +"-prewitt/"+ ")")
        else:
            os.mkdir(url +"-prewitt/")
            for key in image_urls:
                cat_total = len(image_urls[key])
                count = 0
                os.mkdir(url +"-prewitt/" + key)
                for image in image_urls[key]:
                    count = count + 1
                    img = cv2.imread(url +"/"+ key +"/"+ image)
                    p = ndi.prewitt(img) 
                    cv2.imwrite(url +"-prewitt/"+ key +"/"+ image, p)
        print("--> Done.")
    
    # create composit of the selected types
    if comp == True:
        _create_multichannel_image(types, image_urls, url)

def _create_multichannel_image(types, image_urls, url):
    """ Open multiple images and return a single multi channel image """
    print("Creating Multichannel Composit...")
    label_ext = ""
    for x in types:
        label_ext += x


    if os.path.exists(url + label_ext +"-composit/") and os.path.isdir(url + label_ext +"-composit/"):    # check if tmp_path exists
        print("--> Path already exists!  (" + url + label_ext +"-composit/"+ ")")

    else:
        os.mkdir(url + label_ext + "-composit/")
        for key in image_urls:
            os.mkdir(url + label_ext + "-composit/" + key)
            for image in image_urls[key]:

                a = cv2.imread(url + types[0] + "/" + key + "/" + image, 0)
                b = cv2.imread(url + types[1] + "/" + key + "/" + image, 0)
                c = cv2.imread(url + types[2] + "/" + key + "/" + image, 0)

                needed_multi_channel_img = np.zeros((a.shape[0], a.shape[1], 3))
                needed_multi_channel_img2 = np.zeros((b.shape[0], b.shape[1], 3))
                needed_multi_channel_img3 = np.zeros((c.shape[0], c.shape[1], 3))

                needed_multi_channel_img [:,:,0] = a
                needed_multi_channel_img [:,:,1] = b
                needed_multi_channel_img [:,:,2] = c

                needed_multi_channel_img2 [:,:,0] = b
                needed_multi_channel_img2 [:,:,1] = c
                needed_multi_channel_img2 [:,:,2] = a

                needed_multi_channel_img3 [:,:,0] = c
                needed_multi_channel_img3 [:,:,1] = a
                needed_multi_channel_img3 [:,:,2] = b
                
                cv2.imwrite(url + label_ext +"-composit/"+ key +"/abc_"+ image, needed_multi_channel_img)
                cv2.imwrite(url + label_ext +"-composit/"+ key +"/bca_"+ image, needed_multi_channel_img2)
                cv2.imwrite(url + label_ext +"-composit/"+ key +"/cab_"+ image, needed_multi_channel_img3)

    print("--> Done.")
if __name__ == '__main__':
    # Specify Command line args
    parser = argparse.ArgumentParser(description="CEML - Process Images")
    parser.add_argument('-i', '--input', help='Enter the directory of your dataset', required=True, dest="inDir")
    parser.add_argument('--pre', help='Run all preprocessors, but no composit.', action='store_true', dest="pre")
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

    if (args.pre == True):
        cannyAuto = True
        cannyTight = True
        cannyWide = True
        original = True
        laplacian = True
        sobelX = True
        sobelY = True
        prewitt = True
        main(inputDir, cannyAuto, cannyWide, cannyTight, original, laplacian, sobelX, sobelY, prewitt, False)
    else:
        if sum([cannyAuto, cannyTight, cannyWide, original, laplacian, sobelX, sobelY, prewitt]) > 3:
            print("Too many pre-processors selected. Please use up to 3 at once.")
        elif sum([cannyAuto, cannyTight, cannyWide, original, laplacian, sobelX, sobelY, prewitt]) < 1:
            print("Use flags to select pre-processors. Check the documentation for more information.")
        else:
            main(inputDir, cannyAuto, cannyWide, cannyTight, original, laplacian, sobelX, sobelY, prewitt, True)