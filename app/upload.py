from flask import Flask, request, redirect, url_for, render_template, flash, jsonify
import os
from os.path import join, dirname, realpath

#画像サイズ
image_size = 160

UPLOADS_DIR = "uploads"
STATIC_PATH = join(dirname(realpath(__file__)), 'static')
UPLOADS_PATH = join(STATIC_PATH, UPLOADS_DIR)

from flask import Blueprint
bp = Blueprint("upload", __name__, url_prefix="/upload")

@bp.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        path = os.path.join(UPLOADS_PATH, file.filename)
        file.save(path)
        return jsonify({"result": "OK", "file": url_for('static', filename=UPLOADS_DIR + "/" +file.filename)})
    return render_template("upload/upload.html")

@bp.route('/list', methods=['GET', 'POST'])
def uploadlist():
    filelist = _get_img_names(UPLOADS_PATH)

    return render_template("upload/list.html", filelist=filelist)

import glob
import re
def _get_img_names(img_dir):
    img_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]
    img_paths = sorted([os.path.basename(p) for p 
        in glob.glob(os.path.join(img_dir, '**'), recursive=True) if os.path.isfile(p) if re.search('/*\.(jpg|jpeg|png|gif|bmp)', str(p))])
    return img_paths
