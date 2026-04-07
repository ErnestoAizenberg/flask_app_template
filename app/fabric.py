"""Application Fabric"""

__all__ == ['create_app']

from flask import Flask
from flask_cors import CORS

from .errors import add_error_handlers
from . import views

def register_handlers(app: Flask) -> None:
    """Register handlers"""
    app.add_url_rule('/', 'read_root', views.read_root)


def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app, resources={r'/*': {'origins': '*'}})
    register_handlers(app) 
    return app

if __name__ == '__main__':
    application: Flask = create_app()