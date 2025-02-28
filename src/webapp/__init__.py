from flask import Flask
from .config import Config
from .tool_options_blueprint import tool_options_bp
from .routes import  register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Set a secret key for session management
    app.secret_key = app.config['SECRET_KEY']

    with app.app_context():
        register_routes(app)
        app.register_blueprint(tool_options_bp, url_prefix='/tool_options')
    return app