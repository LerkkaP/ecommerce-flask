"""
Module for handling user-related logic for admin panel.
"""

from sqlalchemy.sql import text

from website.db import db


def users_page():
    """
    Retrieve information about all users.

    Returns:
        list: A list of user records.
    """
    query = db.session.execute(
        text("SELECT id, username, privileges FROM users;"))

    users = query.fetchall()

    return users


def remove_user(user_id):
    """
    Remove a user from the database.

    Keyword arguments:
        user_id (int): The ID of the user to be removed.

    Returns:
        None
    """

    db.session.execute(text("DELETE FROM users WHERE id=:user_id"), {
                       "user_id": user_id})
    db.session.commit()
