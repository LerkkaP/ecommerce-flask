from flask import Blueprint, render_template, request, flash, redirect, session
from ..views.auth import login_user, logout_user, register_user

from ..decorators import login_required

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("auth/login.html")
    elif request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        type, message = login_user(username, password)

        if type == "error":
            flash(message, category="error")
            return redirect('/login')
        else:
            flash(message, category="success")
            return redirect('/')

@auth.route('/logout')
@login_required
def logout():

    logout_user()

    return redirect('/')

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        register_user(username, password1, password2)

    return render_template('auth/sign_up.html')
