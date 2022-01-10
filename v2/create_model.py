import argparse
from fastai2 import *
from fastai2.vision import *
import fastbook
fastbook.setup_book()
from fastbook import *

import pandas as pd 
import numpy as np 

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def clear_pyplot_memory():
    plt.clf()
    plt.cla()
    plt.close()

def main(input_dir, model, cycles):
    if cycles == None: cycles = 5 #default
    if model == None: model = "resnet18"

    output_name_mod = input_dir + "/model_" + model + "_" + str(cycles)
    # variables
    image_size = 224
    batch_size = 4

    # set model
    m = None
    if model == 'resnet18': m = models.resnet18
    elif model == 'resnet34': m = models.resnet34
    elif model == 'resnet50': m = models.resnet50
    else: print("ERROR: Model not recognized.")

    class DataLoaders(GetAttr):
        def __init__(self, *loaders): self.loaders = loaders
        def __getitem__(self, i): return self.loaders[i]
        train,valid = add_props(lambda i,self: self[i])

    block = DataBlock(
        blocks=(ImageBlock, CategoryBlock), 
        get_items=get_image_files, 
        splitter=RandomSplitter(valid_pct=0.2, seed=42),
        get_y=parent_label,
        item_tfms=Resize(128))

    dls = block.dataloaders(input_dir)
    learn = cnn_learner(dls, m, metrics=error_rate)

    
    # Create fig 1 - SAMPLE BATCH
    print("--> Create sample batch image...")
    dls.show_batch(nrows=4, ncols=3, show=True)
    plt.savefig(output_name_mod + '_sample_batch.png')
    clear_pyplot_memory()
    print("--> Done!")

    # Create fig 3
    print("--> Create learning rate plot image...")
    learn.lr_find(show_plot=True)
    plt.savefig(output_name_mod+ '_lr_plot.png')
    clear_pyplot_memory()
    print("--> Done!")

    # fit cycles
    print("--> Training model for 'c' cycles...")
    learn.fit_one_cycle(int(cycles))
    print("--> Done!")

    # Create fig 2
    print("--> Create loss plot image...")
    learn.recorder.plot_loss()
    plt.savefig(output_name_mod + '_loss_plot.png')
    clear_pyplot_memory()
    print("--> Done!")

    # Save model
    print("--> Saving Model...")
    learn.export(output_name_mod+ '_model.pkl')
    print("--> Done!")

if __name__ == '__main__':
    # Specify Command line args
    parser = argparse.ArgumentParser(description="CEML - Create Model")
    parser.add_argument('-i', '--input', help='Enter the directory of your dataset', required=True, dest="inDir")
    parser.add_argument('-m', '--model', help='Enter a type of model to use', required=False, dest="model")
    parser.add_argument('-c', '--cycles', help='Enter an iteger for number of cycles', required=False, dest="cycles")
    args = parser.parse_args()

    # Assign Command line args
    inputDir = args.inDir
    model = args.model
    cycles = args.cycles

    main(inputDir, model, cycles)