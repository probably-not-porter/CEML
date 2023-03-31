# Official Code - Composite Edge Detection in Convolutional Neural Networks
## Porter Libby - Senior Capstone Project Spring 2020

Note: all original code is denoted with a tag at the top of the file.

## Usage
While there isn't a GUI yet, the project is meant to work with both command line and notebook interfaces. In a `ipynb` setting, the **Data Structure** can be imported directly and configured. In a terminal interface however, the `createModel.py` file can be used to control the data structure with command line arguements (specified below).

## Command Line Usage - createModel.py
`-i [path]` : **REQUIRED** : Specify a path to a database (parent path with labels as subfolders)

Up to three pre-processing algorithms can be used. they can be selected using the follow flags:

- `--canney_auto`
- `--canney_tight`
- `--canney_wide`
- `--laplacian`
- `--sobel_x`
- `--sobel_y`
- `--prewitt`

There are also some command line arguements for configuring the CNN parameters:
- `--model_type [model]` : Sets the model used in the CNN. Currently the options are `resnet18`, `reset34` (default), and `resnet50`. This is something that could be expanded in future work. 
- `--batch_size [int]` : Sets the batch size for training the CNN. Higher batch size will allow more to be processed in parallel, but it will also increase resource usage. Default is `4` for CPU usage. GPGPU usage will support much higher batch size.
- `--image_size [int]` : Sets the size that images will be adjusted to for the CNN. Default is `224`.

## Examples
```$ python3 createModel.py -i "path" --canny_auto --laplacian --original```</br>
Creates a model using the specified path and two pre-processing algorithms (Canny (automatic) and Laplacian) combined with the original image.

```$ python3 createModel.py -i "path" --canny_auto --model_type resnet18 --batch_size 8 --image_size 112``` </br>
Creates a model using just Canny Edge Detection (automatic) using the resnet18 model, an image size of 112px, and a batch size of 8 images.

## Data Structure
The `DataGlob` structure I created for this project is meant to be an amorphous container for all the information and settings that go into the preprocessing of images (before they are used to construct a model). 

*Public* methods for the `DataGlob` class are outlined below:

- `prepare_database()` - This method takes the settings that are present in the DataGlob and constructs a set of images which are ready to be used to create a model. It doesn't take any params, but it does require that at least one processing algorithm is set to be used. 

- `prepare_control_database()` - Similar to prepare_database(), but does not use any kind of preprocessing. This is basically a wrapper for skipping the pre-processing step, and is mostly useful from a testing and comparison point of view. 

- `show_configuration()` - This method will output the configuration of the DataGlob. This method will be most useful to those who are unfamiliar with the data structure of this project, and need some extra verbosity when it comes to settings.

- `set_configuration( SETTING, VALUE )` - This method allows the user to set the value of a boolean setting in the Glob configuration. The possible settings are outlined below, organized by which part of the process they affect. These values can also be controlled via command line arguements, which are formatted very similarly, and can be seen above in the `Command Line Usage` section.

  - **Preprocessing Settings**
    - "canny_tight" - BOOLEAN
    - "canny_auto" - BOOLEAN
    - "canny_wide" - BOOLEAN
    - "laplacian" - BOOLEAN
    - "sobel_x" - BOOLEAN
    - "sobel_y" - BOOLEAN
    - "prewitt" - BOOLEAN
    - "original" - BOOLEAN
    - "overwrite" - BOOLEAN
  - **Machine Learning Settings**
    - "image_size" - INT
    - "batch_size" - INT
    - "model_type" - STRING : Currently the options are `resnet18`, `reset34` (default), and `resnet50`.
  
    Examples:<br>
      ```ExampleGlob.set_configuration("canny_auto", True)```    
      ```ExampleGlob.set_configuration("model_type", "resnet18")```   
      ```ExampleGlob.set_configuration("image_size", 112)```   

- `create_databunch()` - Creates and stores a databunch object (from FastAI library) using parameters from the DataGlob. The databunch will be made up of the images created by the dataglob in the _out_path variable.

- `show_databunch()` - **(Jupyter or IPython only)** Plots a figure of a random set of four processed samples from the _out_path variable.

- `create_model()` - Creates a model using the configured values and model type, and exports that model to the `/out` folder. This model is also affected by the `overwrite` setting when creating new models in the same directory, and will be replaced if the option is set to `True`.
</br></br>**NOTE**:It is recommended that once a model is created, it be renamed or moved so that it is not replaced by new data being processed by the project.
## Learning
