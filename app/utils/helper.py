from keras.preprocessing import image
import numpy as np
from .extract_bottleneck_features import *
import cv2 
from tensorflow.keras.applications.resnet50 import preprocess_input,  ResNet50
import pickle
from utils.trainedmodel import get_model

dog_names = pickle.load(open("app/utils/dog_names.p", "rb"))

ResNet50_model = ResNet50(weights='imagenet')

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')

model = get_model()

# returns "True" if face is detected in image stored at img_path
def face_detector(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    return len(faces) > 0


def path_to_tensor(img_path):
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)

def ResNet50_predict_labels(img_path):
    # returns prediction vector for image located at img_path
    img = preprocess_input(path_to_tensor(img_path))
    return np.argmax(ResNet50_model.predict(img))

def dog_detector(img_path):
    prediction = ResNet50_predict_labels(img_path)
    return ((prediction <= 268) & (prediction >= 151))

def dog_breed(img_path):
    
    bottleneck_feature = extract_Resnet50(path_to_tensor(img_path))
    pred_vector = model.predict(bottleneck_feature)
    max = np.argmax(pred_vector)
    dog_name = dog_names[max].replace("_"," ")
    return dog_name
