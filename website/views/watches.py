"""
Module for implementing watch-related logic
"""

from datetime import date
from flask import request
from sqlalchemy.sql import text
from website.db import db


def get_all_watches():
    """
    Retrieve a paginated list of watches.

    Returns:
        A tuple containing a list of watches, current page number, items per page, and total pages.
    """
    page = int(request.args.get("page", 1))
    items_per_page = 6

    offset = (page - 1) * items_per_page

    total_items_query = db.session.execute(
        text("SELECT COUNT(*) FROM watches;"))
    total_items = total_items_query.fetchone()[0]

    total_pages = (total_items + items_per_page - 1) // items_per_page

    result = db.session.execute(
        text(
            "SELECT id, brand, model, cast(price as money) "
            "FROM watches ORDER BY brand LIMIT :limit OFFSET :offset;"
        ),
        {"limit": items_per_page, "offset": offset}
    )

    watches = result.fetchall()

    return watches, page, items_per_page, total_pages


def get_watch_detail(watch_id):
    """
    Get detailed information about a specific watch.

    Keyword arguments:
        id (int): The ID of the watch.

    Returns:
        tuple: A tuple containing details about the watch, its reviews, 
        average rating, and review count.
    """
    query = db.session.execute(text(
        "SELECT id, brand, model, cast(price as money), description "
        "FROM watches WHERE id=:watch_id;"
    ), {"watch_id": watch_id})
    details = query.fetchone()

    review_query = db.session.execute(text(
        "SELECT reviews.id as review_id, users.id as user_id, users.username, "
        "reviews.review, reviews.rating, reviews.review_date "
        "FROM reviews "
        "JOIN users ON reviews.user_id = users.id "
        "WHERE reviews.watch_id=:watch_id;"
    ), {"watch_id": watch_id})

    rating_query = db.session.execute(text(
        "SELECT ROUND(AVG(rating), 0) "
        "FROM reviews "
        "WHERE watch_id=:watch_id"), {"watch_id": watch_id})

    count_query = db.session.execute(
        text("SELECT COUNT(*) FROM reviews WHERE watch_id=:watch_id;"), {"watch_id": watch_id})
    review_count = count_query.fetchone()[0]

    average_rating = rating_query.fetchone()[0]

    reviews = review_query.fetchall()

    return details, reviews, average_rating, review_count


def add_review(watch_id, user_id, rating, description):
    """
    Add a review for a specific watch.

    Keyword arguments:
        watch_id (int): The ID of the watch.
        user_id (int): The ID of the user submitting the review.
        rating (int): The rating given to the watch.
        description (str): The review description.

    Returns:
        True if the review was added successfully, False otherwise.
    """
    today = date.today()

    query = """
    INSERT INTO reviews (watch_id, user_id, review, rating, review_date)
    SELECT :watch_id, :user_id, :review, :rating, :review_date
    WHERE NOT EXISTS (
        SELECT 1 FROM reviews 
        WHERE user_id = :user_id 
        AND watch_id = :watch_id
    )
    """

    result = db.session.execute(
        text(query),
        {
            "watch_id": watch_id,
            "user_id": user_id,
            "review": description,
            "rating": rating,
            "review_date": today
        }
    )
    db.session.commit()

    return result.rowcount > 0


def delete_watch_review(review_id, user_id):
    """
    Delete a user's review for a specific watch.

    Keyword arguments:
        review_id (int): The ID of the review to be deleted.
        user_id (int): The ID of the user who submitted the review.
    """
    db.session.execute(text("DELETE FROM reviews WHERE id=:review_id AND user_id=:user_id"), {
                       "review_id": review_id, "user_id": user_id})
    db.session.commit()
