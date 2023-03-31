# example from 
# https://github.com/fastai/fastai/blob/master/examples/dogs_cats.ipynb

from fastai.vision import *
from fastai.metrics import accuracy

path = "./dogs-cats"
size = 224
bs = 16

import os
labels = os.listdir("dogs-cats")
print("No. of labels: {}".format(len(labels)))
print("-----------------")

for label in labels:
    print("{}, {} files".format(label, len(os.listdir("dogs-cats/"+label))))

data = ImageDataBunch.from_folder(path, 
    ds_tfms=get_transforms(do_flip=True, flip_vert=True),
    valid_pct=0.2, 
    size=size, 
    bs=bs)

data.normalize(imagenet_stats)

learner = cnn_learner(data, models.resnet18, metrics=[accuracy])
learner.fit_one_cycle(3,max_lr=1e-2)

interp = ClassificationInterpretation.from_learner(learner)
interp.plot_confusion_matrix(figsize=(10,10))
