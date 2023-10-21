"""
Module for implementing search logic for watches.
"""

from sqlalchemy.sql import text
from website.db import db

def search_watches(query):
    """
    Search watches based on a query.

    Keyword arguments:
        query (str): The search query.

    Returns:
        list: A list of watches matching the search query.
    """
    sql = (
        "SELECT id, brand, model, cast(price as money) "
        "FROM watches "
        "WHERE LOWER(brand) LIKE LOWER(:query) OR LOWER(model) LIKE LOWER(:query) "
        "ORDER BY price"
    )
    result = db.session.execute(text(sql), {"query":"%"+query+"%"})
    return result.fetchall()
