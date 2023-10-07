from flask import Blueprint, render_template, redirect, flash, session, url_for

from sqlalchemy.sql import text
from . import db

profile = Blueprint('profile', __name__)

@profile.route('/profile', methods=["GET"])
def show_profile():
    return render_template("profile.html")

@profile.route('/profile', methods=["POST"])
def delete_profile():
    user_id = session.get('user_id')
    db.session.execute(text("DELETE FROM users WHERE id=:user_id"), {"user_id": user_id})
    db.session.commit() 

    flash("Account deleted!", category="success")
    return redirect(url_for('auth.logout'))
