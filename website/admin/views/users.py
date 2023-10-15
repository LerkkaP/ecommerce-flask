from sqlalchemy.sql import text

from ...db import db

def users_page():
    query = db.session.execute(text("SELECT id, username, privileges FROM users;"))

    users = query.fetchall()

    return users

def remove_user(user_id):
    db.session.execute(text("DELETE FROM users WHERE id=:user_id"), {"user_id": user_id})
    db.session.commit()