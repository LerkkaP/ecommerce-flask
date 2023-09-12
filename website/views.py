from flask import Blueprint, render_template
from sqlalchemy.sql import text
from . import db

views = Blueprint('view', __name__)

@views.route('/')
def watches():
    result = db.session.execute(text("SELECT brand, model, price FROM watches;"))
    watches = result.fetchall()
    return render_template("watches.html", watches=watches)

@views.route('/shopping-cart')
def shopping_cart():
    return render_template("cart.html")