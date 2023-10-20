# Archive and Results Journal

## Apr27_2023
- **Models**: All resnet, all squeezenet, all densenet
- **Dataset**: x-ray set from Kaggle
- **Preprossing**: None / control 

Some basic tests, nothing special. Used a resize transform value of 128, might need to increase that. 
Plots seem to show a trend of much higher valid loss than training loss, implying that it may be overfitting on the amount of data being processed. Increasing the resize transform may provide more substrate for the CNN. 100 epoch rounds.

## May7_2023
- **Models**: All resnet, all squeezenet, all densenet (except densenet161, failed for some reason)
- **Dataset**: x-ray set from Kaggle
- **Preprossing**: None / control 

Tests larger resize transform (224). Significant improvement in resnet and densenet, no improvement from squeezenet. It's curious that one of the densenet models failed with only 1 epoch recorded, not sure why that happened. Next test should include a second dataset as additional information. It looks like increasing the resize function will continue to improve results, at least up to a certain level. 20 epoch rounds.

## May9_2023
- **Models**: All resnet, all squeezenet, all densenet 
- **Dataset**: dogs-cats from Kaggle
- **Preprossing**: None / control 
Same settings as previous test I think. Got lost between docs. Used 20 epoch rounds for all.

## Aug5_2023
- **Models**: All resnet, all densenet 
- **Dataset**: dogs-cats from Kaggle
- **Preprossing**: Sobel_X + Sobel_Y + Original
Same settings as before, just added preprocessor. Will start to cycle through the whole group.


