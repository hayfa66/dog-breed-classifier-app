from keras.layers import GlobalAveragePooling2D , MaxPooling2D
from keras.layers import Dense
from keras.models import Sequential  

def get_model():
    model = Sequential()
    model.add(GlobalAveragePooling2D(input_shape=(7, 7, 2048)))
    model.add(Dense(133, activation='softmax'))
    model.load_weights('saved_models/weights.best.modelresnet50.hdf5')
    
    return model