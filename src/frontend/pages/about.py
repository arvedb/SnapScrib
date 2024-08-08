from flask import Blueprint

about = Blueprint('about', __name__)

@about.route('/')
def about_func():
    return "<h1>About</h1>"