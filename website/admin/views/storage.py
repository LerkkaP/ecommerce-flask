from sqlalchemy.sql import text

from ...db import db

def show_storage():
    query = db.session.execute(text("SELECT * FROM watches;"))

    watches = query.fetchall()

    return watches

def add_to_storage(brand, model, price, description):
    db.session.execute(text("INSERT INTO watches (brand, model, price, description) VALUES (:brand, :model, :price, :description)"), {"brand": brand, "model": model, "price": price, "description": description})
    db.session.commit()

def delete_from_storage(watch_id):
    db.session.execute(text("DELETE FROM watches WHERE id=:watch_id"), {"watch_id": watch_id})
    db.session.commit()



            
    