from flask import Flask, request, redirect, url_for, render_template, flash, jsonify
from os.path import join, dirname, realpath

UPLOADS_DIR = "uploads"
STATIC_PATH = join(dirname(realpath(__file__)), 'static')
UPLOADS_PATH = join(STATIC_PATH, UPLOADS_DIR)

from flask import Blueprint
bp = Blueprint("", __name__, url_prefix="/")

@bp.route('/')
def index():
    return render_template("top.html")

@bp.route('/health')
def health():
    return 'Health Check OK!!'

@bp.route('/comment', methods=['POST'])
def comment():
    return render_template("comment.html")

@bp.route('/sns', methods=['GET', 'POST'])
def sns():
    return render_template("sns.html")
