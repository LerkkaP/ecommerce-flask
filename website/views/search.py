from sqlalchemy.sql import text
from ..db import db

def search_watches(query):
    sql = "SELECT id, brand, model, cast(price as money) FROM watches WHERE LOWER(brand) LIKE LOWER(:query) OR LOWER(model) LIKE LOWER(:query) ORDER BY price"
    result = db.session.execute(text(sql), {"query":"%"+query+"%"})
    return result.fetchall()


