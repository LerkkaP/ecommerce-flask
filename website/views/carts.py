from flask import flash
from sqlalchemy.sql import text
from ..db import db

def add_watch_to_cart(watch_id, user_id):
    count = db.session.execute(text("SELECT COUNT(*) FROM cart WHERE watch_id=:watch_id"), {'watch_id': watch_id})
    count_result = count.fetchone()[0]
    if count_result == 0:
        query = ("INSERT INTO cart (watch_id, user_id, quantity) values (:watch_id, :user_id, 1);")
        db.session.execute(text(query), {"watch_id": watch_id, "user_id": user_id})
        db.session.commit()
        flash("Watch added to cart!")

    else:
        db.session.execute(text("UPDATE cart SET quantity = quantity + 1 WHERE watch_id=:watch_id"), {'watch_id': watch_id})
        db.session.commit()
        flash("Item updated")

def show_cart(user_id):
    query = db.session.execute(text(
    "SELECT c.watch_id, c.quantity, w.brand, w.model, w.price " 
    "FROM cart c JOIN watches w ON c.watch_id = w.id " 
    "WHERE c.user_id=:user_id;"),
    {"user_id": user_id})
    items = query.fetchall()

    summa = 0
    if len(items) > 0:
        for item in items:
            summa += item.price * item.quantity

    return items, summa

def delete_from_cart(watch_id):
    db.session.execute(text("DELETE FROM cart WHERE watch_id=:watch_id"), {"watch_id": watch_id})
    db.session.commit()

def decrease_item_quantity(watch_id, quantity):
    if int(quantity) == 1:
        db.session.execute(text("DELETE FROM cart WHERE watch_id=:watch_id"), {'watch_id': watch_id})
        db.session.commit()
    else:
        db.session.execute(text("UPDATE cart SET quantity = quantity - 1 WHERE watch_id=:watch_id"), {'watch_id': watch_id})
        db.session.commit()

def increase_item_quantity(watch_id):
    db.session.execute(text("UPDATE cart SET quantity = quantity + 1 WHERE watch_id=:watch_id"), {"watch_id": watch_id})
    db.session.commit()



