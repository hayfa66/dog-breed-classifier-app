import numpy as np
from .extract_bottleneck_features import *
import cv2 
from tensorflow.keras.applications.resnet50 import preprocess_input,  ResNet50
import pickle
from utils.trainedmodel import get_model
from keras.utils import image_utils as image

# loading dog breeds form a file
dog_names = pickle.load(open("app/utils/dog_names.p", "rb"))

# model to detect if there is a dog 
ResNet50_model = ResNet50(weights='imagenet')

# model to detect if there is a human face
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')

# upload the main model that would predict the dog breed
model = get_model()

# returns "True" if face is detected in image stored at img_path
def face_detector(img_path):
    '''
    returns "True" if face is detected in image stored at img_path
    input : image path
    return : boolean
    '''
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    return len(faces) > 0


def path_to_tensor(img_path):
    '''
    input : image path
    return : expanded image
    '''
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)

def ResNet50_predict_labels(img_path):
    '''
    returns prediction vector for image located at img_path
    input : image path
    return : prediction vector
    '''
    img = preprocess_input(path_to_tensor(img_path))
    return np.argmax(ResNet50_model.predict(img))

def dog_detector(img_path):
    '''
    returns "True" if dog is detected in image stored at img_path
    input : image path
    return : boolean
    '''
    prediction = ResNet50_predict_labels(img_path)
    return ((prediction <= 268) & (prediction >= 151))

def dog_breed(img_path):
    '''
    returns name of the breed predicted 
    input : image path
    return : string
    '''
    # extract features from the photo
    bottleneck_feature = extract_Resnet50(path_to_tensor(img_path))
    # predict 
    pred_vector = model.predict(bottleneck_feature)
    max = np.argmax(pred_vector)
    # remove _ from the string
    dog_name = dog_names[max].replace("_"," ")
    return dog_name
