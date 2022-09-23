from keras.layers import GlobalAveragePooling2D , MaxPooling2D
from keras.layers import Dense
from keras.models import Sequential  

def get_model():
    '''
    returns the model with the transfered learning
    to predict a dog breed
    input : None
    return : Model
    '''
    # sequential model
    model = Sequential()
    #photo would be with shape (7, 7, 2048)
    model.add(GlobalAveragePooling2D(input_shape=(7, 7, 2048)))
    model.add(Dense(133, activation='softmax'))
    # load the weights
    model.load_weights('saved_models/weights.best.modelresnet50.hdf5')
    
    return model