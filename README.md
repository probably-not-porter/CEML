# SRSD (Subterrainian Rectilinear Shape Detection)

## Installation

1. Make sure you have python3.x.
2. install dependencies listed below.
3. run `python3 srsd.py` to start the GUI.

## Usage
The first input that is expected is your <strong>master data directory</strong>, which will determine what operations are available for the rest of the execution. A typical structure for the master data directory looks like this:

>DIR </br>
>including any input images.
>>DIR / ndvi </br>
>>processed NDVI versions of the images in DIR </br></br>
>>DIR / NIR</br>
>>NIR versions of the images in DIR

* The program will attempt to detect any folders in this structure that are manually included, based on folder name.
  
* Each type of image will be used in the edge detection operations, so each of these modifiers adds a lot to processing time.

Once the folder is set up, you have the option to create additional resources like NDVI if they do not exist, and pick what edge detectors you want to use on the available set of data.

## Dependencies
- tkinter
- matplotlib
- getopt
## References
https://rosettacode.org/wiki/Canny_edge_detector

https://github.com/OlafenwaMoses/ImageAI

https://github.com/adl1995/edge-detectors

https://gitlab.cluster.earlham.edu/field-science/images

https://github.com/Wangyupei/CED

https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html

https://github.com/JalaliLabUCLA/Image-feature-detection-using-Phase-Stretch-Transform

https://github.com/ankitaggarwal011/PyCNN

