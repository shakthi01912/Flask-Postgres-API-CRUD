from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import logging
from routes import note_routes
from models.note_model import create_table

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Register Blueprints for modular routing
app.register_blueprint(note_routes.note_bp)

# Directly create the table when the app starts
create_table()

if __name__ == '__main__':
    app.run(debug=True)