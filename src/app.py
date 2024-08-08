import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from backend.config.css import load_css
from frontend.create_app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)