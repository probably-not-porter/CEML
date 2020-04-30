"""
|----------------------------------------------|
| CS488 -  Senior Capstone Project             |
| Porter Libby                                 |
| Spring 2020                                  |
|----------------------------------------------|
"""
# This file changes frequently. It's just the method I have been using to queue large amounts of work to be run overnight or over the course of a day or so.

import os

# import custom code
from dataglob import DataGlob # Data structure

sample_url = "/training/plant-id-100"

def full_pipe(url):
    glob1 = DataGlob(os.getcwd() + url,os.getcwd())
    glob1._overwrite = True

    print("CONTROL")
    glob1.show_configuration()
    glob1.prepare_control_database()
    glob1.create_databunch()
    glob1.create_model()



    # adjust some knobs
    glob1.set_configuration("prewitt", True)
    glob1.set_configuration("sobel_y", True)
    glob1.set_configuration("original", True)
    
    print('prewitt+sobely AND ORIGINAL')
    glob1.show_configuration()
    glob1.prepare_database()
    glob1.create_databunch()
    glob1.create_model()

    glob1 = DataGlob(os.getcwd() + url,os.getcwd())
    glob1._overwrite = True

    # adjust some knobs
    glob1.set_configuration("prewitt", True)
    glob1.set_configuration("sobel_y", True)
    glob1.set_configuration("canny_tight", True)
    
    print('prewitt+sobely AND canny_tight')
    glob1.show_configuration()
    glob1.prepare_database()
    glob1.create_databunch()
    glob1.create_model()

    glob1 = DataGlob(os.getcwd() + url,os.getcwd())
    glob1._overwrite = True

    # adjust some knobs
    glob1.set_configuration("prewitt", True)
    glob1.set_configuration("sobel_y", True)
    glob1.set_configuration("canny_auto", True)
    
    print('prewitt+sobely AND canny_auto')
    glob1.show_configuration()
    glob1.prepare_database()
    glob1.create_databunch()
    glob1.create_model()

    

    glob1 = DataGlob(os.getcwd() + url,os.getcwd())
    glob1._overwrite = True

    # adjust some knobs
    glob1.set_configuration("canny_wide", True)
    glob1.set_configuration("prewitt", True)
    glob1.set_configuration("sobel_y", True)
    
    print('prewitt+sobely AND canny_wide')
    glob1.show_configuration()
    glob1.prepare_database()
    glob1.create_databunch()
    glob1.create_model()



    glob1 = DataGlob(os.getcwd() + url,os.getcwd())
    glob1._overwrite = True

    # adjust some knobs
    glob1.set_configuration("laplacian", True)
    glob1.set_configuration("prewitt", True)
    glob1.set_configuration("sobel_y", True)
    
    print('prewitt+sobely AND laplacian')
    glob1.show_configuration()
    glob1.prepare_database()
    glob1.create_databunch()
    glob1.create_model()




    glob1 = DataGlob(os.getcwd() + url,os.getcwd())
    glob1._overwrite = True

    # adjust some knobs
    glob1.set_configuration("sobel_x", True)
    glob1.set_configuration("prewitt", True)
    glob1.set_configuration("sobel_y", True)
    
    print('prewitt+sobely AND sobel_x')
    glob1.show_configuration()
    glob1.prepare_database()
    glob1.create_databunch()
    glob1.create_model()