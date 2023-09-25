from flask import Blueprint, render_template, request, redirect, session, flash, url_for

from sqlalchemy.sql import text
from . import db
from datetime import date

views = Blueprint('view', __name__)

@views.route('/')
def watches():
    page = int(request.args.get('page', 1))
    items_per_page = 6

    offset = (page - 1) * items_per_page

    total_items_query = db.session.execute(text("SELECT COUNT(*) FROM watches;"))
    total_items = total_items_query.fetchone()[0]

    total_pages = (total_items + items_per_page - 1) // items_per_page

    result = db.session.execute(text("SELECT id, brand, model, price FROM watches LIMIT :limit OFFSET :offset;"), {'limit': items_per_page, 'offset': offset})

    watches = result.fetchall()
    return render_template("watches.html", watches=watches, page=page,     items_per_page = items_per_page, total_pages=total_pages
)

@views.route('/watch/<int:id>', methods = ['GET', 'POST'])
def watch_detail(id):
    if request.method == "GET":
        watch_id = id
        query = db.session.execute(text("SELECT brand, model, price, description FROM watches WHERE id=:watch_id;"), {'watch_id': watch_id})
        details = query.fetchone()

        details_dict = {
            'brand': details[0],
            'model': details[1],
            'price': details[2],
            'description': details[3],
            'watch_id': id
        }

        review_query = db.session.execute(text("SELECT * FROM reviews WHERE watch_id=:watch_id;"), {'watch_id': watch_id})
        reviews = review_query.fetchall()
        

        reviews_list = []
        for review in reviews:
            reviews_dict = {
                'watch_id': review[1],
                'user_id': review[2],
                'review': review[3],
                'rating': review[4],
                'review_date': review[5]
            }
            reviews_list.append(reviews_dict)
        
        return render_template("watch_detail.html", details=details_dict, reviews=reviews_list)


    if request.method == "POST":
        rating = request.form.get("ratings")
        description = request.form.get("description")
        today = date.today()
        user_id = session.get("user_id")

        query = ("INSERT INTO reviews (watch_id, user_id, review, rating, review_date) values (:watch_id, :user_id, :review, :rating, :review_date);")
        db.session.execute(text(query), {"watch_id": id, "user_id": user_id, "review": description, "rating": rating, "review_date": today})
        db.session.commit()
        flash("Review added!")

        return redirect(url_for('view.watch_detail', id=id))


        


