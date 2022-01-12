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
model_keras = 'cats_dogs_model.h5'

from flask import Blueprint
bp = Blueprint("inference", __name__, url_prefix="/inference")

import tensorflow as tf

graph = tf.compat.v1.get_default_graph()

@bp.route('/keras', methods=['POST'])
def inference_keras():
    global graph
    with graph.as_default():
        path = os.path.join(STATIC_PATH, "model")
        path = os.path.join(path, model_keras)
        if (os.path.exists(path)):
            print(path)
        from keras.models import load_model
        model = load_model(path)
        file = request.files['file']
        path = os.path.join(UPLOADS_PATH, file.filename)
        file.save(path)
        from keras.preprocessing import image as preprocessing
        img = preprocessing.load_img(path, target_size=TARGET_SIZE)
        img = preprocessing.img_to_array(img)
        import numpy as np
        x = np.expand_dims(img, axis=0)
        try:
            predict = model.predict(x)
            print(predict[0])
        except Exception as e:
            print(e)
        for p in predict:
            class_index = p.argmax()
            probality = p.max()
        return jsonify({"result":"OK", "file":class_names[class_index], "probality":str(probality)})
