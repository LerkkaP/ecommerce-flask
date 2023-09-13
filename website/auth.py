from flask import Blueprint, render_template, request, flash, redirect
import re
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash
from . import db


auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('base.html')

@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        hash_value = generate_password_hash(password1)

        reg = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
        
        # if check_password_hash(username, password1) == check_password_hash(username, password2)

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

    '''
      password validation:

      - at least 8 chars logn
      - at leaast one uppercase character (A-Z)
      - A number (0-9) and/or symbol (such as !, #, or %)
    '''


    return render_template('sign_up.html')