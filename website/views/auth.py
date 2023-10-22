"""
Module for handling authentication-related logic.
"""

import re
from flask import session, flash
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash
from website.db import db


def login_user(username, password):
    """
    Log in a user.

    Keyword arguments:
        username (str): The username.
        password (str): The user's password.

    Returns:
        tuple: A tuple containing the result and a message.
    """
    query = "SELECT id, password FROM users WHERE username=:username;"
    result = db.session.execute(text(query), {"username": username})
    user = result.fetchone()
    if not user:
        # Generic error message for security reasons
        return "error", "Invalid username or password"

    if check_password_hash(user.password, password):
        session["user_id"] = user.id
        return "success", f"Welcome {username}!"

    return "error", "Invalid username or password"


def logout_user():
    """Log out a user."""
    del session["user_id"]


def register_user(username, password1, password2):
    """
    Register a new user.

    Keyword arguments:
        username (str): The username.
        password1 (str): The user's password.
        password2 (str): The repeated password.

    Returns:
        None
    """
    check_username = db.session.execute(
        text("SELECT EXISTS (SELECT username FROM users WHERE username=:username)"),
        {"username": username}
    )
    if check_username.fetchone()[0]:
        flash("Username is already taken", category="error")
    else:
        hash_value = generate_password_hash(password1)

        reg = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"

        if len(username) < 4:
            flash("username must be at least 4 characters long", category="error")
        elif password1 != password2:
            flash("Passwords didn't match", category="error")
        elif not re.match(reg, password1):
            flash(
                "Password requirements: 8+ characters, "
                "1 uppercase, 1 lowercase, 1 digit, 1 special character.",
                category="error"
            )
        else:
            query = (
                "INSERT INTO users (username, password, privileges) "
                "VALUES (:username, :password, :privileges);"
            )

            db.session.execute(
                text(query),
                {"username": username, "password": hash_value,
                    "privileges": "customer"}
            )
            db.session.commit()
            flash("Account created!", category="success")
