from flask import Blueprint, render_template, request, redirect, session, flash, url_for

from sqlalchemy.sql import text
from . import db

carts = Blueprint('carts', __name__)

@carts.route('/addcart', methods=['POST'])
def add_cart():
    watch_id = request.form.get('watch_id')
    quantity = request.form.get('quantity')
    user_id = session.get("user_id")
    
    if request.method == "POST":
        query = ("INSERT INTO cart (watch_id, user_id, quantity) values (:watch_id, :user_id, :quantity);")
        db.session.execute(text(query), {"watch_id": watch_id, "user_id": user_id, "quantity": quantity})
        db.session.commit()
        flash("Watch added to cart!")

        return redirect(url_for('view.watch_detail', id=watch_id))

@carts.route('/shopping-cart', methods=['GET'])
def shopping_cart():
    user_id = session.get("user_id")
    query = db.session.execute(text(
        "SELECT c.watch_id, c.quantity, w.brand, w.model, w.price " 
        "FROM cart c JOIN watches w ON c.watch_id = w.id " 
        "WHERE c.user_id=:user_id;"),
        {"user_id": user_id})
    items = query.fetchall()
    
    return render_template("cart.html", items=items)



