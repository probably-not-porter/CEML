# Composite Edge Detection in Convulutional Neural Networks

Note: all original code is denoted with a tag at the top of the file.

## Algorithms

## Data Structure
The `DataGlob` structure I created for this project is meant to be an amorphous container for all the information and settings that go into the preprocessing of images (before they are used to construct a model). 

Public methods for the `DataGlob` class are outlined below:

`prepare_database()` - This method takes the settings that are present in the DataGlob and constructs a set of images which are ready to be used to create a model. It doesn't take any params, but it does require that at least one processing algorithm is set to be used. 

`print_configuration()` - This method will output the configuration of the DataGlob. This method will be most useful to those who are unfamiliar with the data structure of this project, and need some extra verbosity when it comes to settings.

## Learning

## Data