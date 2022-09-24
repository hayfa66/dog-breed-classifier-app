from flask import render_template
from flask import Flask, request,jsonify
from werkzeug.utils import secure_filename
import os
from glob import glob
from utils.helper import *



UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def human_or_dog(img_path):
    '''
    function to evaluate a photo if it has a dog or a human or neither
    input : img path
    output : string contain name of the breed
    '''
    if dog_detector(img_path):
        # call function that has a model that can predict
        dog_name = dog_breed(img_path)
        return "This Dog breed is "+dog_name+"."
    if face_detector(img_path):
         # call function that has a model that can predict
        dog_name = dog_breed(img_path)
        return "This human looks like a "+dog_name+" breed."
    return "No human or dog found"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('master.html')


# route for prediction

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)
            img_file_path = os.path.join("app/uploads/", filename)
            file.save(os.path.join("app/uploads/", filename))
            # predict function
            prediction = human_or_dog(img_file_path)
            # delete uploaded file
            os.remove(img_file_path)
            return jsonify(prediction)
        # return True

    return ""
if __name__ == '__main__':
    '''
        main run part
    '''
    server = '0.0.0.0'
    port = '5000'
    app.run(host = server,  port = port, debug = True)    
