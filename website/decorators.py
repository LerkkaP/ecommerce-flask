"""
Module with login decorators.
"""

from functools import wraps
from flask import redirect, session, render_template
from sqlalchemy import text
from .db import db

def login_required(f):
    """
    Decorator to check if the user is logged in.
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        user_id = session.get("user_id")
        if not user_id:
            return render_template("messages/denied.html")
        return f(*args, **kwargs)
    return wrap

def admin_login_required(f):
    """
    Decorator to check if the user is an admin and logged in.
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        user_id = session.get("user_id")
        if user_id is not None:
            query = "SELECT privileges FROM users WHERE id=:id"
            result = db.session.execute(text(query), {"id": user_id})
            privileges = result.fetchone()

            if not (privileges and privileges[0] == "admin"):
                return render_template("messages/denied.html")
        else:
            return redirect("/login")
        return f(*args, **kwargs)
    return wrap
