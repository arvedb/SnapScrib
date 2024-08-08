from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()
FLASK_KEY = os.getenv('FLASK_KEY')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = FLASK_KEY

    return app