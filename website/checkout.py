from flask import Blueprint, render_template, redirect, flash, session, request

from sqlalchemy.sql import text
from . import db
from datetime import date

checkout = Blueprint('checkout', __name__)

@checkout.route('/checkout', methods=['GET'])
def display_checkout_form():
    return render_template("checkout.html")

@checkout.route('/checkout', methods=['POST'])
def checkout_items():
    if request.method == 'POST':
        user_id = session.get("user_id")
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        shipping_address = request.form.get('shipping_address')
        billing_address = request.form.get('billing_address')
        phone_number = request.form.get('phone_number')
        email = request.form.get('email')
        payment_method = request.form.get('payment')
        order_date = date.today()

        cart_query = db.session.execute(text("SELECT watch_id, quantity FROM cart WHERE user_id=:user_id;"), {"user_id": user_id})
        cart_results = cart_query.fetchall()
        for _ in cart_results:
            query = ("INSERT INTO orders (user_id, watch_id, first_name, last_name, shipping_address, billing_address, phone_number, email, quantity, payment_method, order_date) VALUES (:user_id, :watch_id, :first_name, :last_name, :shipping_address, :billing_address, :phone_number, :email, :quantity, :payment_method, :order_date);") 
            db.session.execute(text(query), {"user_id": user_id, "watch_id": _[0], "first_name": first_name, "last_name": last_name, "shipping_address": shipping_address, "billing_address": billing_address, "phone_number": phone_number, "email": email, "quantity": _[1], "payment_method": payment_method, "order_date": order_date})
            db.session.commit()

    return render_template("thanks_page.html")