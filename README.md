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

you also needs to download some more files for the dataset ,
you can find it in the [udacity dog-project github](https://github.com/udacity/dog-project) .
--------------
## 2. Project Motivation

this is a the last project for a udacity Nanodegree it is to make an app on web that can predict a dog breed .
it also can can pridect what of the dog breed a human similar to , or if it didn't find any human or dog face .

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

## 5. Licensing, Authors, Acknowledgements

thanks to udacity for providing the complementry codes .
