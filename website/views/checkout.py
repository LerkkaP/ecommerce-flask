"""
Module for handling checkout-related logic.
"""

from datetime import date
from flask import session
from sqlalchemy.sql import text
from website.db import db


def checkout_items(first_name, last_name, shipping_address, billing_address, phone_number, email, payment_method):
    """
    Checkout items and create orders in the database.

    Keyword arguments:
        first_name (str): User's first name.
        last_name (str): User's last name.
        shipping_address (str): User's shipping address.
        billing_address (str): User's billing address.
        phone_number (str): User's phone number.
        email (str): User's email address.
        payment_method (str): Payment method used for the order.

    Returns:
        None
    """
    user_id = session.get("user_id")
    order_date = date.today()

    if all([
        first_name,
        last_name,
        shipping_address,
        billing_address,
        phone_number,
        email,
        payment_method
    ]):

        cart_query = db.session.execute(text(
            "SELECT watch_id, quantity FROM cart WHERE user_id=:user_id;"), {"user_id": user_id})
        cart_results = cart_query.fetchall()

        db.session.execute(text("DELETE FROM cart WHERE user_id=:user_id;"), {
                           "user_id": user_id})
        db.session.commit()

        for _ in cart_results:
            query = (
                "INSERT INTO orders (user_id, watch_id, first_name, last_name, "
                "shipping_address, billing_address, phone_number, email, "
                "quantity, payment_method, order_date) "
                "VALUES (:user_id, :watch_id, :first_name, :last_name, "
                ":shipping_address, :billing_address, :phone_number, "
                ":email, :quantity, :payment_method, :order_date);"
            )
            db.session.execute(
                text(query),
                {
                    "user_id": user_id,
                    "watch_id": _[0],
                    "first_name": first_name,
                    "last_name": last_name,
                    "shipping_address": shipping_address,
                    "billing_address": billing_address,
                    "phone_number": phone_number,
                    "email": email,
                    "quantity": _[1],
                    "payment_method": payment_method,
                    "order_date": order_date
                }
            )
            db.session.commit()


'''
def get_cart_items(user_id):
    # Retrieve cart items for the user
    pass

def clear_cart(user_id):
    # Remove items from the cart after checkout
    pass

def create_order(user_id, watch_id, first_name, last_name, shipping_address, billing_address, phone_number, email, quantity, payment_method, order_date):
    # Create a new order in the database
    pass

def checkout_items(first_name, last_name, shipping_address, billing_address, phone_number, email, payment_method):
    user_id = session.get("user_id")
    order_date = date.today()

    if all([first_name, last_name, shipping_address, billing_address, phone_number, email, payment_method]):
        cart_items = get_cart_items(user_id)

        if cart_items:
            clear_cart(user_id)

            for item in cart_items:
                watch_id, quantity = item
                create_order(user_id, watch_id, first_name, last_name, shipping_address, billing_address, phone_number, email, quantity, payment_method, order_date)
'''