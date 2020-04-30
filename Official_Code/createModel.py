"""
|----------------------------------------------|
| CS488 -  Senior Capstone Project             |
| Porter Libby                                 |
| Spring 2020                                  |
|----------------------------------------------|
"""
import os, argparse, time

# import data structure
from dataglob import DataGlob # Data structure

def main(url, cannyAuto = False, cannyWide = False, cannyTight = False, original = False, laplacian = False, sobelX = False, sobelY = False, prewitt = False, modelType = None, batchSize = None, imageSize = None):
    glob1 = DataGlob(os.getcwd() + url,os.getcwd())
    glob1._overwrite = True

    if cannyAuto:
        glob1.set_configuration("canny_auto", True)
    if cannyTight:
        glob1.set_configuration("canny_tight", True)
    if cannyWide:
        glob1.set_configuration("canny_wide", True)
    if original:
        glob1.set_configuration("original", True)
    if laplacian:
        glob1.set_configuration("laplacian", True)
    if sobelX:
        glob1.set_configuration("sobel_x", True)
    if sobelY:
        glob1.set_configuration("sobel_y", True)
    if prewitt:
        glob1.set_configuration("prewitt", True)
    if modelType:
        glob1.set_configuration("model_type", modelType)
    if batchSize:
        glob1.set_configuration("batch_size", int(batchSize))
    if imageSize:
        glob1.set_configuration("image_size", int(imageSize))

    #glob1.show_configuration()
    glob1.prepare_database()
    glob1.create_databunch()
    glob1.create_model()
    print("Done! Trained model has been exported to out/export.pkl")

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

    parser.add_argument('--model_type', help='Select CNN Model type', dest="modelType")
    parser.add_argument('--batch_size', help='Select a batch size for CNN', dest="batchSize")
    parser.add_argument('--image_size', help='Select an image size for CNN', dest="imageSize")

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

    modelType = args.modelType
    batchSize = args.batchSize
    imageSize = args.imageSize

    if sum([cannyAuto, cannyTight, cannyWide, original, laplacian, sobelX, sobelY, prewitt]) > 3:
        print("Too many pre-processors selected. Please use up to 3 at once.")
    elif sum([cannyAuto, cannyTight, cannyWide, original, laplacian, sobelX, sobelY, prewitt]) < 1:
        print("Use flags to select pre-processors. Check the documentation for more information.")
    else:
        main(inputDir, cannyAuto, cannyWide, cannyTight, original, laplacian, sobelX, sobelY, prewitt, modelType, batchSize, imageSize)