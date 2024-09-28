import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    DB_HOST = os.getenv('DB_HOST')
    DB_DATABASE = os.getenv('DB_DATABASE')
    DB_PORT = os.getenv('DB_PORT')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')