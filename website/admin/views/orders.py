from sqlalchemy.sql import text
from ...db import db

def show_orders():
    query = db.session.execute(text("SELECT id, user_id, watch_id, first_name, last_name, shipping_address, billing_address, phone_number, email, quantity, payment_method, order_date FROM orders GROUP BY id ORDER BY order_date;"))

    orders = query.fetchall()

    return orders

def remove_order(id, user_id):
    db.session.execute(text("DELETE FROM orders WHERE id=:id AND user_id=:user_id"), {"id": id, "user_id": user_id})
    db.session.commit()
