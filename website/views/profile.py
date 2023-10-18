from sqlalchemy.sql import text
from ..db import db

def show_profile_data(user_id):
    user_query = db.session.execute(text("SELECT username FROM users WHERE id=:user_id"), {"user_id": user_id})
    username = user_query.fetchone()[0]

    order_query = db.session.execute(text("SELECT DISTINCT watch_id, brand, model, price, quantity, order_date FROM orders JOIN watches ON orders.watch_id = watches.id WHERE orders.user_id = :user_id"), {"user_id": user_id})
    orders_data = order_query.fetchall()

    return username, orders_data

def delete_profile_data(user_id):
    db.session.execute(text("DELETE FROM users WHERE id=:user_id"), {"user_id": user_id})
    db.session.commit() 
