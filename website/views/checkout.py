from flask import session
from sqlalchemy.sql import text
from ..db import db
from datetime import date

def checkout_items(first_name, last_name, shipping_address, billing_address, phone_number, email, payment_method):
    user_id = session.get("user_id")
    order_date = date.today()

    if first_name and last_name and shipping_address and billing_address and phone_number and email and payment_method:

        cart_query = db.session.execute(text("SELECT watch_id, quantity FROM cart WHERE user_id=:user_id;"), {"user_id": user_id})
        cart_results = cart_query.fetchall()

        db.session.execute(text("DELETE FROM cart WHERE user_id=:user_id;"), {"user_id": user_id})
        db.session.commit()

        for _ in cart_results:
            query = ("INSERT INTO orders (user_id, watch_id, first_name, last_name, shipping_address, billing_address, phone_number, email, quantity, payment_method, order_date) VALUES (:user_id, :watch_id, :first_name, :last_name, :shipping_address, :billing_address, :phone_number, :email, :quantity, :payment_method, :order_date);") 
            db.session.execute(text(query), {"user_id": user_id, "watch_id": _[0], "first_name": first_name, "last_name": last_name, "shipping_address": shipping_address, "billing_address": billing_address, "phone_number": phone_number, "email": email, "quantity": _[1], "payment_method": payment_method, "order_date": order_date})
            db.session.commit()
    