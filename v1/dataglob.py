"""
|----------------------------------------------|
| CS488 -  Senior Capstone Project             |
| Porter Libby                                 |
| Spring 2020                                  |
|----------------------------------------------|
"""

import argparse, glob, cv2, time, os, sys, shutil

from PIL import Image
from fastai.vision import *
from fastai.imports import *
from matplotlib import pyplot as plt
import numpy as np
from scipy import ndimage as ndi
from IPython.display import clear_output
from datetime import datetime


# ---------------- CUSTOMIZABLE ERROR MESSAGES ---------------------
OVERWRITE_ERROR = "This action will overwrite an existing Glob output. Use 'set_configuration('overwrite',True)' to override this warning, and erase existing data"
CONFIGURATION_ERROR = "Something went wrong with the configuration you tried. Check the documentation for the set_configuration() function."

class DataGlob:
    """ data structure to manage a single input set of images and 
        all the processed/compressed versions of those images."""

    def __init__(self, inputpath, outputpath):
        # INITIALIZE PATHS
        self._input_path = inputpath            # this is the path the glob pulls images from
        self._out_path = outputpath + "/out"    # root path for image output
        self._tmp_path = outputpath + "/tmp"    # tmp dir for things that will be created and deleted quickly (saves space)
        self._model_path = None

        # PROCESSING CONFIG                     # these track what settings to use when prepareDatabase is used
        self._use_canny_auto = False
        self._use_canny_wide = False
        self._use_canny_tight = False
        self._use_laplacian = False
        self._use_sobel_x = False
        self._use_sobel_y = False
        self._use_prewitt = False
        self._use_original = False
        
        self._overwrite = False

        # MACHINE LEARNING CONFIG
        self._databunch = None

        self._model_type = "resnet34"

        self._image_size = 224
        self._batch_size = 4

    
    # ----------------- Public Methods -----------------
    def create_model(self):
        model_type = None

        if self._model_type == "resnet34":
            model_type = models.resnet34
        elif self._model_type == "resnet18":
            model_type = models.resnet18
        elif self._model_type == "resnet50":
            model_type = models.resnet50

        learner = cnn_learner(self._databunch, model_type, metrics=[accuracy, error_rate])
        learner.fit_one_cycle(5)
        #learner.recorder.plot_lr()
        #learner.recorder.plot()
        learner.export()
        #interp = ClassificationInterpretation.from_learner(learner)
        #interp.plot_confusion_matrix(figsize=(3,3))
        
    def create_databunch(self):
        self._databunch = ImageDataBunch.from_folder(self._out_path, 
            ds_tfms=get_transforms(do_flip=True, flip_vert=True),
            valid_pct=0.5, 
            size=self._image_size, 
            bs=self._batch_size)

    def show_databunch(self, r=3, f=(7,6)):
        self._databunch.show_batch(rows=r, figsize=f)
        
    def prepare_control_database(self):
        """ Wrapper for moving a database without modifying it """
        self._write_output("Formatting Existing Data for control...")
        if os.path.exists(self._out_path) and os.path.isdir(self._out_path):    # check if out_path exists
            if self._overwrite:
                shutil.rmtree(self._out_path)
            else:
                raise Exception(OVERWRITE_ERROR)
        os.mkdir(self._out_path)

        if os.path.exists(self._tmp_path) and os.path.isdir(self._tmp_path):    # check if tmp_path exists
            shutil.rmtree(self._tmp_path)
        os.mkdir(self._tmp_path)
        
        subfolders = [ f.path for f in os.scandir(self._input_path) if f.is_dir() ]
        for label in subfolders:
            
            dirpath = os.path.join(self._out_path, label.split('/')[-1])
            if os.path.exists(dirpath) and os.path.isdir(dirpath):      # check if sub-dir exists
                shutil.rmtree(dirpath)
            os.mkdir(dirpath)
            
            for jpgfile in glob.iglob(os.path.join(label, "*.jpg")):
                shutil.copy(jpgfile, dirpath)
                
            for jpegfile in glob.iglob(os.path.join(label, "*.jpeg")):
                shutil.copy(jpegfile, dirpath)
                
        if os.path.exists(self._tmp_path) and os.path.isdir(self._tmp_path):    # check if tmp_path exists
            shutil.rmtree(self._tmp_path)
        self._write_output("Done.")
        
    def prepare_database(self):
        """ Wrapper for processing a full database """

        settings = self._get_configuration()
        if os.path.exists(self._out_path) and os.path.isdir(self._out_path):    # check if out_path exists
            if self._overwrite:
                shutil.rmtree(self._out_path)
            else:
                raise Exception(OVERWRITE_ERROR)
        os.mkdir(self._out_path)

        if os.path.exists(self._tmp_path) and os.path.isdir(self._tmp_path):    # check if tmp_path exists
            shutil.rmtree(self._tmp_path)
        os.mkdir(self._tmp_path)
        
        subfolders = [ f.path for f in os.scandir(self._input_path) if f.is_dir() ]
        for label in subfolders:
            
            imgs = []
            for file in os.listdir(label):
                if file.endswith(".jpg") or file.endswith(".jpeg"):
                    imgs.append(os.path.join(label, file))
                    
            dirpath = os.path.join(self._out_path, label.split('/')[-1])
            
            if os.path.exists(dirpath) and os.path.isdir(dirpath):      # check if sub-dir exists
                shutil.rmtree(dirpath)
            os.mkdir(dirpath)
            
            self._create_multiple_images(imgs, self._out_path + "/"+label.split('/')[-1]+"/", settings)
            
        if os.path.exists(self._tmp_path) and os.path.isdir(self._tmp_path):    # check if tmp_path exists
            shutil.rmtree(self._tmp_path)
            
    def show_configuration(self):
        """ Output current configuration to terminal screen """

        print("GLOB CONFIG: ")
        print("-- Pre-processing Config --")
        print("    Canny Tight: " + str(self._use_canny_tight))
        print("    Canny Auto: " + str(self._use_canny_auto))
        print("    Canny Wide: " + str(self._use_canny_wide))
        print("    Laplacian: " + str(self._use_laplacian))
        print("    Sobel X: " + str(self._use_sobel_x))
        print("    Sobel Y: " + str(self._use_sobel_y))
        print("    Prewitt: " + str(self._use_prewitt))
        print("    Original: " + str(self._use_original))
        print("-- Machine Learning Config --")
        print("    Image Size: " + str(self._image_size))
        print("    Batch Size: " + str(self._batch_size))
        print("    Model Type: " + str(self._model_type))
        
    def set_configuration(self, setting, value):
        """ Set a specific setting to a specific value """

        if setting == "canny_tight":
            if type(value) is bool: self._use_canny_tight = value
            else: raise TypeError
        elif setting == "canny_auto":
            if type(value) is bool: self._use_canny_auto = value
            else: raise TypeError
        elif setting == "canny_wide":
            if type(value) is bool: self._use_canny_wide = value
            else: raise TypeError
        elif setting == "laplacian":
            if type(value) is bool: self._use_laplacian = value
            else: raise TypeError
        elif setting == "sobel_x":
            if type(value) is bool: self._use_sobel_x = value
            else: raise TypeError
        elif setting == "sobel_y":
            if type(value) is bool: self._use_sobel_y = value
            else: raise TypeError
        elif setting == "prewitt":
            if type(value) is bool: self._use_prewitt = value
            else: raise TypeError
        elif setting == "original":
            if type(value) is bool: self._use_original = value
            else: raise TypeError
        elif setting == "model_type":
            if value == "resnet18" or value == "resnet34" or value == "resnet50":
                self._model_type = value
            else:
                raise TypeError
        elif setting == "image_size":
            if type(value) is int: self._image_size = value
            else: raise TypeError
        elif setting == "batch_size":
            if type(value) is int: self._batch_size = value
            else: raise TypeError
        else:
            print('setting not found.')

    # ----------------- Private Methods -----------------
    def _get_configuration(self):
        """ Internal accessor for configuration as array """

        settings = [
            self._use_canny_tight,
            self._use_canny_auto,
            self._use_canny_wide,
            self._use_laplacian,
            self._use_sobel_x,
            self._use_sobel_y,
            self._use_prewitt,
            self._use_original
        ]
        if True not in settings:
            raise Exception("Configuration has no processors selected. Please enable at least one preprocessor")
        return settings
    
    def _image_preprocess(self, img_path):
        """ Takes a directory path, returns gray+gaussian versions of image. """

        image = cv2.imread(img_path) 
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)

        return gray
        #return image
    
    def _isnotebook(self):
        try:
            shell = get_ipython().__class__.__name__
            return True  # Other type (?)
        except NameError:
            return False      # Probably standard Python interpreter
    
    def _write_output(self, text):
        if self._isnotebook():
            pass
        else:
            os.system('clear')  # For Linux/OS X
            print(text)

    # ----------------- Processing Algorithms -----------------
    def _canny_auto(self, in_path, sigma=0.33):
        """ Take a directory path, writes result to another path """

        img = self._image_preprocess(in_path)
        v = np.median(img)
        lower = int(max(0, (1.0 - sigma) * v))
        upper = int(min(255, (1.0 + sigma) * v))
        cannyauto = cv2.Canny(img, lower, upper)
        cv2.imwrite(self._tmp_path + '/canny_auto.jpg', cannyauto)
        return self._tmp_path + '/canny_auto.jpg'

    def _canny_wide(self, in_path):
        """ Take a directory path, writes result to another path """

        img = self._image_preprocess(in_path)
        cannywide = cv2.Canny(img, 10, 200)
        cv2.imwrite(self._tmp_path + '/canny_wide.jpg', cannywide)
        return self._tmp_path + '/canny_wide.jpg'

    def _canny_tight(self, in_path):
        """ Take a directory path, writes result to another path """

        img = self._image_preprocess(in_path)
        cannytight = cv2.Canny(img, 225, 250)
        cv2.imwrite(self._tmp_path + '/canny_tight.jpg', cannytight)
        return self._tmp_path + '/canny_tight.jpg'
    
    def _laplacian(self, in_path):
        """ Take a directory path, writes result to another path """

        img = self._image_preprocess(in_path)
        lap = cv2.Laplacian(img,cv2.CV_64F)
        cv2.imwrite(self._tmp_path + '/laplacian.jpg', lap)
        return self._tmp_path + '/laplacian.jpg'

    def _sobel_x(self, in_path):
        """ Take a directory path, writes result to another path """

        img = self._image_preprocess(in_path)
        sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
        cv2.imwrite(self._tmp_path + '/sobel_x.jpg', sobelx)
        return self._tmp_path + '/sobel_x.jpg'

    def _sobel_y(self, in_path):
        """ Take a directory path, writes result to another path """

        img = self._image_preprocess(in_path)
        sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y
        cv2.imwrite(self._tmp_path + '/sobel_y.jpg', sobely)
        return self._tmp_path + '/sobel_y.jpg'
    
    def _original(self, in_path):
        """ Take a directory path, writes result to another path """
        img = self._image_preprocess(in_path)
        cv2.imwrite(self._tmp_path + '/original.jpg', img)
        return self._tmp_path + '/original.jpg'
    
    def _prewitt(self, in_path):
        """ Take a directory path, writes result to another path """
        img = self._image_preprocess(in_path)
        p = ndi.prewitt(img) 
        cv2.imwrite(self._tmp_path + '/prewitt.jpg', p)
        return self._tmp_path + '/prewitt.jpg'
    
    def _create_multiple_images(self, path_ls,out_path, settings):
        """ Wrapper for creating multiple images """

        img_layers = []
        img = None
        for x in range(len(path_ls)):
            outstr = "Processing label '" + path_ls[0].split("/")[-2] + "': "
            outstr += str( round(x * 100 / len(path_ls),2) ) + "% "
            outstr += "(" + str(x) + "/" + str(len(path_ls)) + ")"
            
            self._write_output(  outstr  ) # print progress
            img_layers = []
            img = None

            if settings[0] == True:
                img_layers.append(self._canny_tight(path_ls[x]))
                
            if settings[1] == True:
                img_layers.append(self._canny_auto(path_ls[x]))
                
            if settings[2] == True:
                img_layers.append(self._canny_wide(path_ls[x]))
                
            if settings[3] == True:
                img_layers.append(self._laplacian(path_ls[x]))
                
            if settings[4] == True:
                img_layers.append(self._sobel_x(path_ls[x]))
                
            if settings[5] == True:
                img_layers.append(self._sobel_y(path_ls[x]))

            if settings[6] == True:
                img_layers.append(self._prewitt(path_ls[x]))

            if settings[7] == True:
                img_layers.append(self._original(path_ls[x]))
                
            if len(img_layers) == 1:
                img = PIL.Image.open(img_layers[0])  # single channel image
                
                img.save(out_path+str(x)+'.jpg')

            elif len(img_layers) == 2:
                img = self._create_multichannel_image([ # multi channel image
                    img_layers[0],
                    img_layers[1],
                    img_layers[1]
                ])
                img.save(out_path+str(x)+'.jpg')

            else:
                img = self._create_multichannel_image([ # multi channel image
                    img_layers[0],
                    img_layers[1],
                    img_layers[2]
                ])
                img.save(out_path+str(x)+'.jpg')
        self._write_output(  ""  ) # clear

    def _create_multichannel_image(self, fpArr):
        """ Open multiple images and return a single multi channel image """

        mat = None
        nChannels = len(fpArr)
        for i,fp in enumerate(fpArr):
            img = PIL.Image.open(fp)
            chan = pil2tensor(img, np.float32).float().div_(255)
            if(mat is None):
                mat = torch.zeros((nChannels,chan.shape[1],chan.shape[2]))
            mat[i,:,:]=chan
        return Image(mat)
