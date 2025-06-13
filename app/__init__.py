from flask import Flask
from flask_cors import CORS

from .errors import add_error_handlers


def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app, resources={r'/*': {'origins': '*'}})

    @app.route('/', methods=["GET"])
    def read_root():
        return render_template('index.html')
        
    return app


application: Flask = create_app()
