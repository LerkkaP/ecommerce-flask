from flask import Blueprint, render_template
from sqlalchemy.sql import text
from . import db

views = Blueprint('view', __name__)

@views.route('/')
def watches():
    result = db.session.execute(text("SELECT id, brand, model, price FROM watches;"))
    watches = result.fetchall()
    return render_template("watches.html", watches=watches)

@views.route('/shopping-cart')
def shopping_cart():
    return render_template("cart.html")

@views.route('/watch/<int:id>')
def watch_detail(id):
    watch_id = id
    query = db.session.execute(text("SELECT brand, model, price, description FROM watches WHERE id=:watch_id;"), {'watch_id': watch_id})
    details = query.fetchone()

    details_dict = {
        'brand': details[0],
        'model': details[1],
        'price': details[2],
        'description': details[3]
    }

    print(details_dict)
    return render_template("watch_detail.html", details=details_dict)