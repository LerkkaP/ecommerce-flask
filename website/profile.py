from flask import Blueprint, render_template, redirect, flash

from sqlalchemy.sql import text
from . import db

profile = Blueprint('profile', __name__)


@profile.route('/profile')
def show_profile():
    return render_template("profile.html")
