from flask import request
from sqlalchemy.sql import text
from ..db import db
from datetime import date

def get_all_watches():
    page = int(request.args.get('page', 1))
    items_per_page = 6

    offset = (page - 1) * items_per_page

    total_items_query = db.session.execute(text("SELECT COUNT(*) FROM watches;"))
    total_items = total_items_query.fetchone()[0]

    total_pages = (total_items + items_per_page - 1) // items_per_page

    result = db.session.execute(text("SELECT id, brand, model, price FROM watches ORDER BY brand LIMIT :limit OFFSET :offset;"), {'limit': items_per_page, 'offset': offset})

    watches = result.fetchall()
    
    return watches, page, items_per_page, total_pages

def get_watch_detail(id):
    query = db.session.execute(text("SELECT id, brand, model, price, description FROM watches WHERE id=:watch_id;"), {'watch_id': id})
    details = query.fetchone()

    review_query = db.session.execute(text("SELECT reviews.id as review_id, users.id as user_id, users.username, reviews.review, reviews.rating, reviews.review_date "
                                        "FROM reviews "
                                        "JOIN users ON reviews.user_id = users.id "
                                        "WHERE reviews.watch_id=:watch_id;"), {'watch_id': id})
    
    rating_query = db.session.execute(text("SELECT ROUND(AVG(rating), 0) FROM reviews WHERE watch_id=:watch_id"), {"watch_id": id})

    average_rating = rating_query.fetchone()[0]
    
    reviews = review_query.fetchall()

    return details, reviews, average_rating

def add_review(watch_id, user_id, rating, description):
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
    
    result = db.session.execute(text(query), {"watch_id": watch_id, "user_id": user_id, "review": description, "rating": rating, "review_date": today})
    db.session.commit()

    return result.rowcount > 0


def delete_watch_review(review_id, user_id):
    db.session.execute(text("DELETE FROM reviews WHERE id=:review_id AND user_id=:user_id"), {"review_id": review_id, "user_id": user_id})
    db.session.commit()
        


