# example from 
# https://github.com/fastai/fastai/blob/master/examples/dogs_cats.ipynb

from fastai.vision import *
import fastai

path = untar_data(URLs.PETS)
print(path)
data = ImageDataBunch.from_folder(path, train="images", valid="annotations", size=26)
learn = cnn_learner(data, models.resnet18, metrics=accuracy)
learn.fit(1)