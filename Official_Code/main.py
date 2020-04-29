"""
|----------------------------------------------|
| CS488 -  Senior Capstone Project             |
| Porter Libby                                 |
| Spring 2020                                  |
|----------------------------------------------|
"""
import os

# import custom code
from dataglob import DataGlob # Data structure

url = "/training/chest-xray-small"


glob1 = DataGlob(os.getcwd() + url,os.getcwd())
glob1._overwrite = True

# adjust some knobs
#glob1.set_configuration("original", True)
#glob1.set_configuration("canny_auto", True)
#glob1.set_configuration("prewitt", True)

glob1.prepare_control_database()
glob1.create_databunch()
glob1.show_databunch()
