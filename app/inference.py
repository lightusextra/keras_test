from flask import Flask, request, jsonify
import os
from os.path import join, dirname, realpath

UPLOADS_DIR = "uploads"
STATIC_PATH = join(dirname(realpath(__file__)), 'static')
UPLOADS_PATH = join(STATIC_PATH, UPLOADS_DIR)

class_names = ['1_建物から庭', '2_外の庭', '5_お菓子', '6_洋館内部', '7_建物屋敷', '9_その他']

IMG_WIDTH, IMG_HEIGHT = 224, 224
TARGET_SIZE = (IMG_WIDTH, IMG_HEIGHT)
#
model_keras = 'my_model'

from flask import Blueprint
bp = Blueprint("inference", __name__, url_prefix="/inference")

@bp.route('/keras', methods=['POST'])
def inference_keras():
    file = request.files['file']
    path = os.path.join(UPLOADS_PATH, file.filename)
    file.save(path)
    from keras.preprocessing import image as preprocessing
    img = preprocessing.load_img(path, target_size=TARGET_SIZE)
    img = preprocessing.img_to_array(img)
    import numpy as np
    x = np.expand_dims(img, axis=0)
    #from PIL import Image
    #img = Image.open(path).convert('RGB')
    import os
    path = os.path.join(STATIC_PATH, "model")
    path = os.path.join(path, model_keras)
    #path = os.path.join("/app", model_keras)
    #print('model')
    #path = os.path.join("./app/static/model/", model_keras)
    if (os.path.exists(path)):
        print(path)
    import h5py
    print(h5py.__version__)
    import tensorflow as tf
    print(tf.__version__)
    #from tensorflow import keras
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    try:
        model = tf.keras.models.load_model(path, compile=False)
    except Exception as e:
        print(e)
    from keras.applications.vgg16 import preprocess_input
    #predict = model.predict(preprocess_input(img))
    predict = model.predict(x)
    for p in predict:
        class_index = p.argmax()
        probality = p.max()
        return jsonify({"result":"OK", "file":class_names[class_index], "probality":str(probality)})
