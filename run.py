from flask import Flask
from os.path import join, dirname, realpath
from app.upload import bp as upload
from app.inference import bp as inference
from app.application import bp as application

UPLOADS_DIR = "uploads"
STATIC_PATH = join(dirname(realpath(__file__)), 'static')
UPLOADS_PATH = join(STATIC_PATH, UPLOADS_DIR)

app = Flask(__name__, static_folder='app/static')
app.config['UPLOAD_FOLDER'] = UPLOADS_PATH
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")

app.register_blueprint(application)
app.register_blueprint(upload, url_prefix="/upload")
app.register_blueprint(inference, url_prefix="/inference")

app.config.from_mapping(
    # a default secret that should be overridden by instance config
    SECRET_KEY="dev",
    # store the database in the instance folder
    #DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

if __name__ == "__main__":
    import tensorflow as tf
    STATIC_PATH = join(dirname(realpath(__file__)), 'static')
    import os
    path = os.path.join(STATIC_PATH, "model")
    model_keras = 'my_model2'
    path = os.path.join(path, model_keras)
    model = tf.keras.models.load_model(path, compile=False)
    app.run(host='0.0.0.0', port=5000)