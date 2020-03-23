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


# testing
glob1 = DataGlob(os.getcwd() + "/training/plant-id",os.getcwd() +"/out")
glob1.prepareDatabase([1,1,1,0,0,0,0])
