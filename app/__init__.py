"""Initialize Flask app"""
from flask import Flask
from pathlib import Path

def create_app():
    """Create and configure Flask app"""
    # Get the templates folder path (one level up from app directory)
    template_dir = Path(__file__).parent.parent / 'templates'
    app = Flask(__name__, template_folder=str(template_dir))
    
    # Import config
    from .config import Config
    app.config.from_object(Config)
    
    # Register blueprints
    from .routes import bp
    app.register_blueprint(bp)
    
    return app
