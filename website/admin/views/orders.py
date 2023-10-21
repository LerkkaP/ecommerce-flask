"""
Module for handling orders in the admin panel.
"""

from sqlalchemy.sql import text
from website.db import db


def show_orders():
    """
    Retrieve a list of orders.

    Returns:
        list: A list of order details.
    """
    query = db.session.execute(text(
        "SELECT id, user_id, watch_id, first_name, last_name, shipping_address, "
        "billing_address, phone_number, email, quantity, payment_method, order_date "
        "FROM orders GROUP BY id ORDER BY order_date;"
    ))

    orders = query.fetchall()

    return orders


def remove_order(order_id, user_id):
    """
    Remove an order.

    Keyword arguments:
        id (int): The ID of the order to be removed.
        user_id (int): The ID of the user associated with the order.
    """
    db.session.execute(text("DELETE FROM orders WHERE id=:id AND user_id=:user_id"), {
                       "id": order_id, "user_id": user_id})
    db.session.commit()
