from sqlalchemy.sql import text
from ...db import db

def show_stats():

    watch_query = db.session.execute(text("SELECT COUNT(*) FROM watches;"))
    watches = watch_query.fetchone()[0]

    order_query = db.session.execute(text("SELECT COUNT(*) FROM orders;"))
    orders = order_query.fetchone()[0]

    review_query = db.session.execute(text("SELECT COUNT(*) FROM reviews;"))
    reviews = review_query.fetchone()[0]

    user_query = db.session.execute(text("SELECT COUNT(*) FROM users;"))
    users = user_query.fetchone()[0]

    return watches, orders, reviews, users