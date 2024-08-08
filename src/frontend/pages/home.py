from flask import Blueprint

home = Blueprint('home', __name__)

@home.route('/')
def home_func():
    return "<h1>Home</h1>"