"""
Module for handling statistics related to watches, orders, reviews, and users.
"""

from sqlalchemy.sql import text
from website.db import db


def show_stats():
    """
    Retrieve statistics for watches, orders, reviews, and users.

    Returns:
        tuple: A tuple containing the counts of watches, orders, reviews, and users.
    """

    watch_query = db.session.execute(text("SELECT COUNT(*) FROM watches;"))
    watches = watch_query.fetchone()[0]

    order_query = db.session.execute(text("SELECT COUNT(*) FROM orders;"))
    orders = order_query.fetchone()[0]

    review_query = db.session.execute(text("SELECT COUNT(*) FROM reviews;"))
    reviews = review_query.fetchone()[0]

    user_query = db.session.execute(text("SELECT COUNT(*) FROM users;"))
    users = user_query.fetchone()[0]

    return watches, orders, reviews, users
