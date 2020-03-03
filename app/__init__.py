from flask import Flask
import os

app = Flask(__name__,static_folder='static')
IMAGE_FOLDER = 'image'
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER
STATIC_FOLDER = 'static'
app.config['STATIC_FOLDER'] = STATIC_FOLDER
from app import views

