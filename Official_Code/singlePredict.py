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
from fastai import *
from torchvision import transforms
from matplotlib import pyplot as plt
import numpy as np

def predict(image, model, topk=5):
    learn = load_learner(model)

    img = open_image(image)

    pred_class, pred_idx, outputs = learn.predict(img)
    print(pred_class)
    print(pred_idx)
    print(outputs)


model = "out"
image = "../training/plant-id/docks/3113_12449_30098.jpg"

predict(image, model)