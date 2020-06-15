import numpy as np
from skimage import feature
from cv2 import cv2
import io
import os
import pickle
from flask import Flask, request

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


spiral_model_path = os.path.join(os.path.join(os.getcwd(), 'model'),
                                 'spiral_model.pickle')

wave_model_path = os.path.join(os.path.join(os.getcwd(), 'model'),
                               'wave_model.pickle')

with open(spiral_model_path, 'rb') as fp:
    spiral_model = pickle.load(fp)

with open(spiral_model_path, 'rb') as fp:
    wave_model = pickle.load(fp)


def quantify_image(image):
    #compute the histogram of oriented gradients feature
    # vector for the input image
    features = feature.hog(image,
                           orientations=9,
                           pixels_per_cell=(10, 10),
                           cells_per_block=(2, 2),
                           transform_sqrt=True,
                           block_norm="L1")
    return features


def preprocess_image(filestr):
    image = cv2.imdecode(np.fromstring(filestr, np.uint8),
                                 cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (200, 200))
    image = cv2.threshold(image, 0, 255,
                          cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    return quantify_image(image)


@app.route('/spiral', methods=['POST'])
def base_spiral():
    if request.method == 'POST':
        if 'InputImg' not in request.files:
            print("No file part")
            return "No File Part Found. Please Try Again."

        file = request.files['InputImg']

        if file.filename == '':
            print('No selected file')
            return "No Selected File. Please Try Again."

        if file and allowed_file(file.filename):
            filestr = request.files['InputImg'].read()

            features = preprocess_image(filestr)

            if spiral_model.predict([features])[0] == 0:
                output = 'Healthy'
            else:
                output = "Parkinson's Disease"

        return output


@app.route('/wave', methods=['POST'])
def base_wave():
    if request.method == 'POST':
        if 'InputImg' not in request.files:
            print("No file part")
            return "No File Part Found. Please Try Again."

        file = request.files['InputImg']

        if file.filename == '':
            print('No selected file')
            return "No Selected File. Please Try Again."

        if file and allowed_file(file.filename):
            filestr = request.files['InputImg'].read()

            features = preprocess_image(filestr)
            
            if wave_model.predict([features])[0] == 0:
                output = 'Healthy'
            else:
                output = "Parkinson's Disease"

        return output

if __name__ == '__main__':
    app.secret_key = 'qwertyuiop1234567890'
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
