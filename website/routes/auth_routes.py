"""
Module for handling authentication-related routes.
"""

from flask import Blueprint, render_template, request, flash, redirect

from website.decorators import login_required
from  website.views.auth import login_user, logout_user, register_user


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    """
    Log in a user.

    Returns:
        str: Redirect URL.
    """
    if request.method == "GET":
        return render_template("auth/login.html")
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        login_result, message = login_user(username, password)

        if login_result == "error":
            flash(message, category="error")
            return redirect("/login")

        flash(message, category="success")
        return redirect("/")


@auth.route("/logout")
@login_required
def logout():
    """
    Log out a user.

    Returns:
        str: Redirect URL.
    """

    logout_user()

    return redirect("/")


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    """
    Register a new user.

    Returns:
        str: Rendered HTML content.
    """
    if request.method == "POST":
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        register_user(username, password1, password2)

    return render_template("auth/sign_up.html")
