"""
Module for handling profile-related logic.
"""

from sqlalchemy.sql import text
from website.db import db


def show_profile_data(user_id):
    """
    Retrieve profile data for a given user.

    Keyword arguments:
        user_id (int): The ID of the user.

    Returns:
        tuple: A tuple containing the username and a list of order data.
    """
    user_query = db.session.execute(
        text("SELECT username FROM users WHERE id=:user_id"), {"user_id": user_id})
    username = user_query.fetchone()[0]

    order_query = db.session.execute(text(
        "SELECT watch_id, brand, model, cast(price as money), quantity, order_date "
        "FROM orders "
        "JOIN watches ON orders.watch_id = watches.id "
        "WHERE orders.user_id = :user_id "
        "ORDER BY order_date"), {"user_id": user_id})
    orders_data = order_query.fetchall()

    return username, orders_data


def delete_profile_data(user_id):
    """
    Delete a user's profile.

    Keyword arguments:
        user_id (int): The ID of the user.
    """
    db.session.execute(text("DELETE FROM users WHERE id=:user_id"), {
                       "user_id": user_id})
    db.session.commit()
