import argparse, matplotlib, fastbook
from fastai2 import *
from fastai2.vision import *
from fastbook import *
from datetime import datetime
import matplotlib.pyplot as plt
matplotlib.use('Agg')
fastbook.setup_book()

def clear_pyplot_memory():
    plt.clf()
    plt.cla()
    plt.close()

def main(input_dir, model, cycles):
    # variables
    image_size = 224
    batch_size = 4


    # Set up output holder
    output_list = ["start time", "end time", ""]

    # Get Start Time
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y_%H:%M:%S")
    os.mkdir('output_' + timestampStr)
    output_list[0] = "Start Time: " + timestampStr

    # count files to be processed
    subfolders= [f.path.split("/")[-1] for f in os.scandir(input_dir) if f.is_dir()]
    for sub in subfolders:
        path, dirs, files = next(os.walk(input_dir + "/" + sub))
        file_count = len(files)
        output_list.append("Label: " + sub + " (" + str(file_count) + " images)")
    output_list.append("")
    
    # Default values + write to output
    if cycles == None: cycles = 5 #default
    if model == None: model = "resnet18"
    output_list.append("Cycles: " + str(cycles))
    output_list.append("Model: " + model)

    # set model
    m = None
    if model == 'resnet18': m = models.resnet18
    elif model == 'resnet34': m = models.resnet34
    elif model == 'resnet50': m = models.resnet50
    else: print("ERROR: Model not recognized.")

    # Setup for fastai
    class DataLoaders(GetAttr):
        def __init__(self, *loaders): self.loaders = loaders
        def __getitem__(self, i): return self.loaders[i]
        train,valid = add_props(lambda i,self: self[i])

    block = DataBlock(
        blocks=(ImageBlock, CategoryBlock), 
        get_items=get_image_files, 
        splitter=RandomSplitter(valid_pct=0.2, seed=42),
        get_y=parent_label,
        item_tfms=Resize(128)
    )

    # Create CNN Learner
    dls = block.dataloaders(input_dir)
    learn = cnn_learner(dls, m, metrics=error_rate)

    # Create fig 1 - SAMPLE BATCH
    print("--> Create sample batch image...")
    dls.show_batch(nrows=4, ncols=3, show=True)
    plt.savefig('output_' + timestampStr + '/sample_batch.png')
    clear_pyplot_memory()
    print("--> Done!")

    # Create fig 2 - learning rate
    print("--> Create learning rate plot image...")
    learn.lr_find(show_plot=True)
    plt.savefig('output_' + timestampStr + '/learning_rate.png')
    clear_pyplot_memory()
    print("--> Done!")

    # LEARN MODEL
    for x in range(int(cycles)):
        # fit cycles
        print("--> Training model cycle=" + str(x))
        learn.fit_one_cycle(1)
        print("--> Done!")
    
    # Create fig 3 - plot loss
    print("--> Create loss plot image...")
    learn.recorder.plot_loss()
    plt.savefig('output_' + timestampStr + '/loss.png')
    clear_pyplot_memory()
    print("--> Done!")

    # Create Fig 4 - Confusion Matrix
    print("--> Create confusion matrix image...")
    interp = ClassificationInterpretation.from_learner(learn)
    interp.plot_confusion_matrix()
    plt.savefig('output_' + timestampStr + '/conf_matrix.png')
    clear_pyplot_memory()
    print("--> Done!")

    # Save model
    print("--> Saving Model...")
    learn.export('output_' + timestampStr + '/model.pkl')

    # Write output file
    dateTimeObj = datetime.now()
    timestampStr2 = dateTimeObj.strftime("%d-%b-%Y_%H:%M:%S")
    output_list[1] = "End Time: " + timestampStr2
    
    with open('output_' + timestampStr + '/meta.md', 'w') as f:
        for item in output_list:
            f.write("%s\n" % item)

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