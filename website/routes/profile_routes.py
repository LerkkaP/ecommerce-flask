from flask import Blueprint, render_template, redirect, flash, session, url_for
from ..views.profile import show_profile_data, delete_profile_data
profile = Blueprint('profile', __name__)

@profile.route('/profile', methods=["GET"])
def show_profile():
    user_id = session.get("user_id")
    if not user_id:
        return render_template("denied.html")
    else:
        username, orders_data = show_profile_data(user_id)

        return render_template("user/profile.html", username=username, orders=orders_data)

@profile.route('/profile', methods=["POST"])
def delete_profile():
    user_id = session.get('user_id')
    if not user_id:
        return render_template("denied.html")
    else:
        delete_profile_data(user_id)

        flash("Account deleted!", category="success")
        
        return redirect(url_for('auth.logout'))