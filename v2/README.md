# CEML v2
After returning to this project I've found a shocking number of things in the python world have changed. Instead of just installing the versions I was using before, I have chosen to re-write most of my work to see if I discover any better ways of accomplishing my goals for the project. 

I have also become a bit better at organizing and documenting software, so it may be that this version is a bit less cryptic than the last, and that my work will be of some benefit to someone at some point. To that end, I will be dividing up the steps of the pipeline to make my process more extensible and easier to repair and replicate in different environments, or even with entirely different libraries.

My new design involves three main steps:
1. `process_images.py`. This first step takes a set of images and attempts to pre-process them so that an image classifier can get more traction on minute details that may otherwise be ignored.

2. `create_model.py`. This second step will leverage `torch` and `fastai` to create a CNN image classification model of the data created in step one. The majority of my work will end with this step, as it provides the relevant statistics for proving that the pre-processing algorithm is having any kind of positive effect on image classification.

3. `classify_image.py`. This final step, which is for now a stretch goal, will take a generated model from step 2 (a .pkl file, in my case), and leverage it to classify an input image.

# Usage
## Part 1
Prepare your data. For this step, you will need a set of images to train a model. The images do not have to be the same size, or even the same file format, but they must be divided up into the catagories you would like to teach. 

As an example, one of my testing sets is a binary image set with dogs and cats. In order to set this up, I placed the original data into two folders based in this root directory: `data/dogs_cats/dogs` and `data/dogs_cats/cats`. The processing step will take advantage of this file structure to simplify names and future runs, so make sure it is labeled sensibly.

When I run:

`python3 process_images.py -i "data/dogs_cats" --canny_auto --original --canny_wide`

I will get new folders in the `data` directory, labeled to match the pre-processors I selected in the command line (`data/dogs_cats-cannyauto` and `data/dogs_cats-cannywide`). Since original images are already present, there is no need to move them to a new folder, they are simply left unchanged. The composit version of these images, which will make use of all three versions of the `dogs_cats` dataset, will be labeled `data/dogs_cats-composit`.

Note: When re-running the same data set, the program will not overwrite folders that already exist in order to save processing time. If I decide I want to make a composit with a different three algorithms, ones that do not exist will be generated, while those that have already been run will be re-used from last time. To avoid this, simply delete the folder and the program will generate them again.


# Project Requirements
My current environment for this version is as follows:
- Python 3.9.2 64bit
- Debian 11 (Bullseye)

## `process_images.py`
- numpy==1.22.0
- opencv_python==4.5.5.62
- Pillow==9.0.0
- scipy==1.7.3

