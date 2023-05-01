# Archive and Results Journal

## Apr23_2023
- **Models**: All resnet, all squeezenet, all densenet
- **Dataset**: x-ray set from Kaggle
- **Preprossing**: None / control 


Some basic tests, nothing special. Used a resize transform value of 128, might need to increase that. 
Plots seem to show a trend of much higher valid loss than training loss, implying that it may be overfitting on the amount of data being processed. Increasing the resize transform may provide more substrate for the CNN.