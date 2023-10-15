from flask import request, session, flash
import re
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash
from ..db import db

def login_user(username, password):
    username = request.form.get("username")
    password = request.form.get("password")
    query = ("SELECT id, password FROM users WHERE username=:username;")
    result = db.session.execute(text(query), {'username': username})
    user = result.fetchone()
    if not user:
        return "error", "Invalid username"
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            return "success", f"Welcome {username}!"
        else:
            return "error", "Invalid password"

def logout_user():
    del session['user_id']

def register_user(username, password1, password2):
    check_username = db.session.execute(text("SELECT EXISTS (SELECT username FROM users WHERE username=:username)"), {"username": username})
    if check_username.fetchone()[0]:
        flash("Username is already taken", category="error")
    else:
        hash_value = generate_password_hash(password1)

        reg = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"

        if len(username) < 4:
            flash("username must be at least 4 characters long", category='error')
        elif password1 != password2:
            flash("Passwords didn't match", category="error")
        elif not re.match(reg, password1):
            flash("Make sure your password fulfills the following requirements: is at least 8 characters long, contains at least one uppercase and lowercase letter, has a digit and a special character.", category="error")
        else:
            query = ("INSERT INTO users (username, password, privileges) VALUES (:username, :password, :privileges);")
            db.session.execute(text(query), {'username': username, 'password': hash_value, 'privileges': 'customer'})
            db.session.commit()
            flash("Account created!", category="success")


