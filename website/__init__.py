from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

from dotenv import load_dotenv

load_dotenv()  

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'
    app.config["SQLALCHEMY_DATABASE_URI"] =  getenv("DATABASE_URL")
    app.secret_key = getenv("SECRET_KEY")

    db.init_app(app)

    from .views import views
    from .auth import auth
    from .carts import carts

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(carts, url_prefix='/')

    return app

