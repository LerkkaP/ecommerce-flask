"""This module defines routes related to user profiles."""

from flask import Blueprint, render_template, redirect, flash, session, url_for
from website.decorators import login_required

from  website.views.profile import show_profile_data, delete_profile_data

profile = Blueprint("profile", __name__)


@profile.route("/profile", methods=["GET"])
@login_required
def show_profile():
    """
    Display the user's profile page.

    Returns:
        str: Rendered HTML content.
    """
    user_id = session.get("user_id")

    username, orders_data = show_profile_data(user_id)

    return render_template("user/profile.html", username=username, orders=orders_data)


@profile.route("/profile", methods=["POST"])
@login_required
def delete_profile():
    """
    Delete the user's profile.

    Returns:
        str: Redirect URL after deletion.
    """
    user_id = session.get("user_id")

    delete_profile_data(user_id)

    flash("Account deleted!", category="success")

    return redirect(url_for("auth.logout"))
