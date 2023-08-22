from flask import Flask, render_template, send_from_directory
from flask_ckfinder3 import CKFinder
from os.path import dirname, join

app = Flask(__name__)

upload_dir = join(dirname(__file__), 'uploads')

app.config.update(
    dict(
        CKFINDER_LICENSE_NAME='',
        CKFINDER_LICENSE_KEY='*K?M-*1**-Q**B-*Q**-*B**-1*5*-2**J',
        CKFINDER_QUICKUPLOAD_DIR=upload_dir,
        CKFINDER_QUICKUPLOAD_ENDPOINT='uploads',
        CKFINDER_UPLOADMAXSIZE=1024 * 1024,
        CKFINDER_UPLOADCHECKIMAGES=True,
        CKFINDER_IMAGES_SIZES=dict(small='480x320', medium='600x480', large='800x600'),
        CKFINDER_RESOURCE_TYPES=[
             dict(name='Uploaded files',
                  endpoint='uploads',
                  allowedExtensions='gif,jpeg,jpg,png',
                  directory=upload_dir)
        ]))

CKFinder(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/uploads/<path:filename>')
def uploads(filename):
    return send_from_directory(upload_dir, filename)
