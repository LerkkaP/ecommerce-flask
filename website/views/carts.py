"""
Module for handling cart-related logic.
"""

from flask import flash
from sqlalchemy.sql import text
from website.db import db


def add_watch_to_cart(watch_id, user_id):
    """
    Add a watch to the user's cart.

    Keyword arguments:
        watch_id (int): The ID of the watch to be added to the cart.
        user_id (int): The ID of the user.

    Returns:
        None
    """
    count = db.session.execute(
        text("SELECT COUNT(*) FROM cart WHERE watch_id=:watch_id"),
        {"watch_id": watch_id}
    )
    count_result = count.fetchone()[0]
    if count_result == 0:
        query = "INSERT INTO cart (watch_id, user_id, quantity) values (:watch_id, :user_id, 1);"
        db.session.execute(
            text(query), {"watch_id": watch_id, "user_id": user_id})
        db.session.commit()
        flash("Watch added to cart!")

    else:
        db.session.execute(
            text("UPDATE cart SET quantity = quantity + 1 WHERE watch_id=:watch_id"),
            {"watch_id": watch_id}
        )
        db.session.commit()
        flash("Item updated")


def show_cart(user_id):
    """
    Retrieve the user's cart.

    Keyword arguments:
        user_id (int): The ID of the user.

    Returns:
        tuple: A tuple containing a list of items in the cart and
        the total sum of prices.
    """
    query = db.session.execute(text(
        "SELECT c.watch_id, c.quantity, w.brand, w.model, cast(w.price as money), "
        "cast(SUM(w.price * c.quantity) as money) as total_price "
        "FROM cart c JOIN watches w ON c.watch_id = w.id "
        "WHERE c.user_id=:user_id "
        "GROUP BY c.watch_id, c.quantity, w.brand, w.model, w.price;"),
        {"user_id": user_id})

    total_sum_query = db.session.execute(text(
        "SELECT cast(SUM(w.price * c.quantity) as money) as total_sum "
        "FROM cart c JOIN watches w ON c.watch_id = w.id "
        "WHERE c.user_id=:user_id;"),
        {"user_id": user_id})

    items = query.fetchall()
    total_sum = total_sum_query.fetchone()[0]

    return items, total_sum


def delete_from_cart(watch_id):
    """
    Delete a watch from the user's cart.

    Keyword arguments:
        watch_id (int): The ID of the watch to be removed from the cart.

    Returns:
        None
    """
    db.session.execute(text("DELETE FROM cart WHERE watch_id=:watch_id"), {
                       "watch_id": watch_id})
    db.session.commit()


def decrease_item_quantity(watch_id, quantity):
    """
    Decrease the quantity of a watch in the user's cart.

    Keyword arguments:
        watch_id (int): The ID of the watch.
        quantity (int): The current quantity of the watch.

    Returns:
        None
    """
    if int(quantity) == 1:
        db.session.execute(text("DELETE FROM cart WHERE watch_id=:watch_id"), {
                           "watch_id": watch_id})
        db.session.commit()
    else:
        db.session.execute(text(
            "UPDATE cart SET quantity = quantity - 1 WHERE watch_id=:watch_id"),
            {"watch_id": watch_id})
        db.session.commit()


def increase_item_quantity(watch_id):
    """
    Increase the quantity of a watch in the user's cart.

    Keyword arguments:
        watch_id (int): The ID of the watch.

    Returns:
        None
    """
    db.session.execute(text(
        "UPDATE cart SET quantity = quantity + 1 WHERE watch_id=:watch_id"), {"watch_id": watch_id})
    db.session.commit()
