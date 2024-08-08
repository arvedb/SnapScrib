from flask import Flask 

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshjdhjs'

    from .pages.home import home
    from .pages.about import about

    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(about, url_prefix='/about/')

    return app