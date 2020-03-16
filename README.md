# dpCNN

This repo exists of scripts that will prepare the training, validation and test
data to train a convolutional neural network using [@DIGITS](https://developer.nvidia.com/digits).

The dataset contains 5 different species of birds (emu, house sparrow, peacock, blue jay, european goldfinch). 

The purpose of the project is to evaluate the performance of a neuralnetwork e.g. AlexNet depending on certain parameters such as the size of the trainign set, the split of the dataset, the amount of epochs while training, etc*. 
The goal is for the neuralnetwork to predict the right class. 


## Status 
status = still in progress 

## Download Dataset 
cd into the scrips*.
```
cd scripts 
```
run the main_download.py with the amount of images you want in each class (the project has 5 different bird species) e.g. 
```
python main_download.py 100 
```
