from flask import Blueprint

views = Blueprint('view', __name__)

@views.route('/')
def home():
    return '<h1>Hello world </h1>'