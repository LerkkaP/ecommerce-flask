from flask import Blueprint, render_template, request
from sqlalchemy.sql import text
from . import db

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

@views.route('/shopping-cart')
def shopping_cart():
    return render_template("cart.html")

@views.route('/watch/<int:id>')
def watch_detail(id):
    watch_id = id
    query = db.session.execute(text("SELECT brand, model, price, description FROM watches WHERE id=:watch_id;"), {'watch_id': watch_id})
    details = query.fetchone()

    details_dict = {
        'brand': details[0],
        'model': details[1],
        'price': details[2],
        'description': details[3]
    }

    print(details_dict)
    return render_template("watch_detail.html", details=details_dict)