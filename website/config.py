from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = getenv("SECRET_KEY", "dev")
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URL")
    FLASK_ADMIN_SWATCH = 'materia'