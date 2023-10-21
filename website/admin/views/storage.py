"""
Module for handling storage-related logic for admin panel.
"""

from sqlalchemy.sql import text

from website.db import db


def show_storage():
    """
    Retrieve information about all watches.

    Returns:
        list: A list of watch records.
    """
    query = db.session.execute(
        text("SELECT id, brand, model, cast(price as money), description FROM watches;"))

    watches = query.fetchall()

    return watches


def add_to_storage(brand, model, price, description):
    """
    Add a new watch to the storage.

    Keyword arguments:
        brand (str): The brand of the watch.
        model (str): The model of the watch.
        price (float): The price of the watch.
        description (str): The description of the watch.

    Returns:
        None
    """
    db.session.execute(
        text("INSERT INTO watches (brand, model, price, description) "
            "VALUES (:brand, :model, :price, :description)"),
        {"brand": brand, "model": model, "price": price, "description": description}
    )
    db.session.commit()


def delete_from_storage(watch_id):
    """
    Delete a watch from the storage.

    Keyword arguments:
        watch_id (int): The ID of the watch to be deleted.

    Returns:
        None
    """
    db.session.execute(text("DELETE FROM watches WHERE id=:watch_id"), {
                       "watch_id": watch_id})
    db.session.commit()
