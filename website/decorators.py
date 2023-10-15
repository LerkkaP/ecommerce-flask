from functools import wraps
from flask import request, redirect, url_for, session, render_template
from sqlalchemy import text
from .db import db

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        user_id = session.get("user_id")
        if not user_id:
            return render_template("messages/denied.html")
        return f(*args, **kwargs)
    return wrap

def admin_login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        user_id = session.get('user_id')
        if user_id is not None:
            query = "SELECT privileges FROM users WHERE id=:id"
            result = db.session.execute(text(query), {'id': user_id})
            privileges = result.fetchone()

            if not (privileges and privileges[0] == 'admin'):
                return render_template("messages/denied.html")
        else:
            return redirect('/login')
        return f(*args, **kwargs)
    return wrap

