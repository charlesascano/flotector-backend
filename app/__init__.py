import os
from flask import Flask
from supabase import create_client
from dotenv import load_dotenv

def create_app():
    load_dotenv()  # Load .env

    app = Flask(__name__)

    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    app.supabase = create_client(supabase_url, supabase_key)

    with app.app_context():
        from .routes import bp  # Import the Blueprint, not just the view
        app.register_blueprint(bp)  # Register Blueprint properly

    return app

