# SRSD (Subterrainian Rectilinear Shape Detection)
Subterranean Rectilinear Shape Detector

run srsd.py with python3 to see current GUI. Allows the user to create ndvi version of an image folder (TAKES A LONG TIME)
expects to be given a folder with images, and will create the following structure:

>DIR </br>
>including any input images.
>>DIR / ndvi </br>
>>processed NDVI versions of the images in DIR </br></br>
>>DIR / NIR</br>
>>NIR versions of the images in DIR
* the program will attempt to detect any folders in this structure that are manually included, based on file name. 
* each type of image will be used in the edge detection operations, so each of these modifiers adds a lot to processing time.

# References
https://rosettacode.org/wiki/Canny_edge_detector

https://github.com/OlafenwaMoses/ImageAI

https://github.com/adl1995/edge-detectors

https://gitlab.cluster.earlham.edu/field-science/images

https://github.com/Wangyupei/CED

https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html

https://github.com/JalaliLabUCLA/Image-feature-detection-using-Phase-Stretch-Transform

https://github.com/ankitaggarwal011/PyCNN

