from flask import Blueprint, render_template, request, redirect, session, flash, url_for

from sqlalchemy.sql import text
from . import db
from datetime import date

watches = Blueprint('watches', __name__)

@watches.route('/')
def all_watches():
    page = int(request.args.get('page', 1))
    items_per_page = 6

    offset = (page - 1) * items_per_page

    total_items_query = db.session.execute(text("SELECT COUNT(*) FROM watches;"))
    total_items = total_items_query.fetchone()[0]

    total_pages = (total_items + items_per_page - 1) // items_per_page

    result = db.session.execute(text("SELECT id, brand, model, price FROM watches ORDER BY brand LIMIT :limit OFFSET :offset;"), {'limit': items_per_page, 'offset': offset})

    watches = result.fetchall()
    return render_template("watches.html", watches=watches, page=page, items_per_page = items_per_page, total_pages=total_pages)

@watches.route('/watch/<int:id>', methods = ['GET', 'POST'])
def watch_detail(id):
    if request.method == "GET":
        watch_id = id
        query = db.session.execute(text("SELECT brand, model, price, description FROM watches WHERE id=:watch_id;"), {'watch_id': watch_id})
        details = query.fetchone()

        review_query = db.session.execute(text("SELECT * FROM reviews WHERE watch_id=:watch_id;"), {'watch_id': watch_id})
        reviews = review_query.fetchall()
        
        return render_template("watch_detail.html", details=details, reviews=reviews)

    if request.method == "POST":
        rating = request.form.get("ratings")
        description = request.form.get("description")
        today = date.today()
        user_id = session.get("user_id")

        query = ("INSERT INTO reviews (watch_id, user_id, review, rating, review_date) values (:watch_id, :user_id, :review, :rating, :review_date);")
        db.session.execute(text(query), {"watch_id": id, "user_id": user_id, "review": description, "rating": rating, "review_date": today})
        db.session.commit()
        flash("Review added!")

        return redirect(url_for('watches.watch_detail', id=id))


        


