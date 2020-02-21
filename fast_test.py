# example from 
# https://github.com/fastai/fastai/blob/master/examples/dogs_cats.ipynb

from fastai.vision import *



path = untar_data(URLs.PLANET_SAMPLE)
data = ImageDataBunch.from_folder(path, ds_tfms=get_transforms(), size=224).normalize(imagenet_stats)
learn = cnn_learner(data, models.resnet34, metrics=accuracy)
learn.fit_one_cycle(1)