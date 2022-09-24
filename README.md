# dog-breed-classifier-app

## 1. Installation

it works on python3
, and needs this libraries

no necessary version needed i import all of these libraries by the last version .

- opencv-python
- matplotlib
- numpy
- tqdm
- keras
- scikit-learn
- tensorflow-gpu

You also need to download some file called "VGG-16 bottleneck features"
And add it at folder bottleneck_features .

you can find it here in the [udacity dog-project github](https://github.com/udacity/dog-project) .

Then the app should work without more dataset , enviroment... etc


However the dog_app.py would not work ,
until you download the dataset (human and dog images)from the
[udacity dog-project github](https://github.com/udacity/dog-project) .

--------------
## 2. Project Motivation

this is a the last project for a udacity Nanodegree it is to make an app on web that can predict a dog breed .
it also can pridect what of the dog breed a human similar to , or if it didn't find any human or dog face .

*The interface of the web app*

![Screenshot Web1 ](https://github.com/hayfa66/dog-breed-classifier-app/blob/main/webapp.png)


---------

## 3. How to interact with the project

You need to install all the libraries and run the files
In the terminal :-

- run.py

And click on the url that will be given to you in the terminal.

---------

## 4.File Descriptions

dog_app.html : html version of the dog_app notbook
dog_app.ipynb : notebook provided by udacity to be a guide through the project

app folder : 
1. templetes : have the master.html that run the app
2. utils
    1. dog_names.p 
    2. helper.py 
    3. pretrainedmodel.py
    4. extract_bottleneck_features
3. static : necessary javascript code
4. run.py : to run the app

haarcascades folder : contain the model that detect a human face.

Myphoto : photo to test the model.

images : photo used everywhere in the project.

-----
## 5. Project Definition

# Project Overview

This is a project has an app that would use convolutional neural network to predict a dog breed , a human face and its similar look alike from dog breeds or pridict that no human or dog detected .

# Problem Statement

The app accept a photo from a user and predict as following :

1. if it detect a dog it would predict its breed.
2. if it detect a human it would pridict what of dog breed it similar to the most.
3. if it detect no human of dog it would indicate it as an erorr.
4. If the prediction fails it will show an error.

Strategy for solving the problem

- use Human and Dog detectors to correctly identify type of prediction we using .
- use convolutional neural network to classify dog breeds from scratch
- Use a pre-trained convolutional neural network to Classify Dog Breeds .
- use convolutional neural network with Transfer Learning strategy to Classify Dog Breeds
- evaluate which was the best model for classification.
- write an algorithm to detect dog breed or what a human looks like as a dog breed or return an error.
- test the the algorithm.
- load the best model to an app.

from the app a user can upload photo to test the model and the app .


# Metrics
Accuracy of the model was used to evaluate which model of the three was the best by taking the highest value.

# Analysis

## Data Exploration
### Data Description

Dog Files , containg 8351 dog images in total .
Human Files , containg 13233 human images in total .

dog Breeds name , 133 in total .

For training :

There are 6680 dog images.

For validation :

There are 835 dog images.

For testing :

There are 836 dog images.

Human Detector Performance
using a CascadeClassifier provided by udacity accuracy was :

- 100.0% accuracy on the first 100 images in human files , have a detected human face.
- 11.0% accuracy on the first 100 images in dog files , have a detected human face.

Dog Detector Performance
using pre-trained ResNet-50 model to detect dogs in images the accuracy was :

- 0.0% accuracy on the first 100 images in human files , have a detected dog.
- 100.0% accuracy on the first 100 images in dog files , have a detected dog.


Model Performance

- Convolutional neural network from scratch Accuracy was 6.8182%.
- Pre-trained convolutional neural network Accuracy was 40.6699%.
- Convolutional neural network with Transfer Learning strategy Accuracy was 80.1435%.

For the web app i would choose the Convolutional neural network with Transfer Learning strategy , have heighest accuracy .


Data Visualization
-----
Data :
human 

<img src="https://github.com/hayfa66/dog-breed-classifier-app/blob/main/images/Aaron_Tippin_0001.jpg" height="200">

Curly-coated retriever

<img src="https://github.com/hayfa66/dog-breed-classifier-app/blob/main/images/Curly-coated_retriever_03896.jpg" height="200">

Welsh springer spaniel dog breed

<img src="https://github.com/hayfa66/dog-breed-classifier-app/blob/main/images/Welsh_springer_spaniel_08203.jpg" height="200">

Testing algorithm photos : 

- human 
This human looks like an Beagle.
<img src="https://github.com/hayfa66/dog-breed-classifier-app/blob/main/MyPhotos/photo1.png" height="200">
This human looks like an Silky terrier.
<img src="https://github.com/hayfa66/dog-breed-classifier-app/blob/main/MyPhotos/photo6.png" height="200">

- dogs
This Dog breed is American staffordshire terrier.
<img src="https://github.com/hayfa66/dog-breed-classifier-app/blob/main/MyPhotos/photo2.png" height="200">
This Dog breed is Pomeranian.
<img src="https://github.com/hayfa66/dog-breed-classifier-app/blob/main/MyPhotos/photo5.png" height="200">

- Bears
No human or dog found
<img src="https://github.com/hayfa66/dog-breed-classifier-app/blob/main/MyPhotos/photo3.png" height="200">
No human or dog found
<img src="https://github.com/hayfa66/dog-breed-classifier-app/blob/main/MyPhotos/photo4.png" height="200">
-----

# 6. Conclusion
## Reflection

Summary: -

- using face_detector() and dog_detector() function
and with the notebook provided by udacity i did the following :
- implement all necessary function :
- - dog_breed() .
- - Human_or_dog() function .
- - using Resnet50 model with transfer learning strategy .
- and copy paste it in the helper.py .
- implement run.py to run app using helper.py .
- writing messages as response to every predicton situation.
- and used script.js to transfer the result predicton to the web app .

web app predictions : 

<img src="https://github.com/hayfa66/dog-breed-classifier-app/blob/main/webapp.png" height="700">
<img src="https://github.com/hayfa66/dog-breed-classifier-app/blob/main/webapp2.png" height="700">
<img src="https://github.com/hayfa66/dog-breed-classifier-app/blob/main/webapp3.png" height="700">

# Two particular aspect with difficulty or interesting:
- understanding how architecture impact the CNN model was hard .
- the result from the predictions was interesting . 

# Improvement

- Face human detector somtimes predict that there is a human face while there is not , maybe improving the face detector .
- Improve the dog breed predicton on human maybe by training a new model specific for this task .

## 7. Licensing, Authors, Acknowledgements

thanks to udacity for providing the complementry codes .
