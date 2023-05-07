# Archive and Results Journal

## Apr27_2023
- **Models**: All resnet, all squeezenet, all densenet
- **Dataset**: x-ray set from Kaggle
- **Preprossing**: None / control 

Some basic tests, nothing special. Used a resize transform value of 128, might need to increase that. 
Plots seem to show a trend of much higher valid loss than training loss, implying that it may be overfitting on the amount of data being processed. Increasing the resize transform may provide more substrate for the CNN.

## May7_2023
- **Models**: All resnet, all squeezenet, all densenet (except densenet161, failed for some reason)
- **Dataset**: x-ray set from Kaggle
- **Preprossing**: None / control 

Tests larger resize transform (224). Significant improvement in resnet and densenet, no improvement from squeezenet. It's curious that one of the densenet models failed with only 1 epoch recorded, not sure why that happened. Next test should include a second dataset as additional information. It looks like increasing the resize function will continue to improve results, at least up to a certain level. 