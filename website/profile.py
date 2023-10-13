from flask import Blueprint, render_template, redirect, flash, session, url_for

from sqlalchemy.sql import text
from . import db

profile = Blueprint('profile', __name__)

@profile.route('/profile', methods=["GET"])
def show_profile():
    user_id = session.get("user_id")

    user_query = db.session.execute(text("SELECT username FROM users WHERE id=:user_id"), {"user_id": user_id})
    username = user_query.fetchone()[0]

    order_query = db.session.execute(text("SELECT DISTINCT brand, model, price FROM orders JOIN watches ON orders.watch_id = watches.id WHERE orders.user_id = :user_id"), {"user_id": user_id})
    orders_data = order_query.fetchall()

    '''
    orders_list = []
    for order in orders_data:
        orders_dict = {
            'brand': order[0],
            'model': order[1],
            'price': order[2]
        }
        orders_list.append(orders_dict)
    '''

    return render_template("profile.html", username=username, orders=orders_data)

@profile.route('/profile', methods=["POST"])
def delete_profile():
    user_id = session.get('user_id')
    db.session.execute(text("DELETE FROM users WHERE id=:user_id"), {"user_id": user_id})
    db.session.commit() 

    flash("Account deleted!", category="success")
    return redirect(url_for('auth.logout'))