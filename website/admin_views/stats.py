from flask_admin import AdminIndexView
from flask import redirect, url_for
from flask_admin import BaseView, expose
from sqlalchemy.sql import text

from .. import db

class Stats(AdminIndexView):
    @expose('/')
    def index(self):
        watch_query = db.session.execute(text("SELECT COUNT(*) FROM watches;"))
        watches = watch_query.fetchone()[0]

        order_query = db.session.execute(text("SELECT COUNT(*) FROM orders;"))
        orders = order_query.fetchone()[0]

        review_query = db.session.execute(text("SELECT COUNT(*) FROM reviews;"))
        reviews = review_query.fetchone()[0]

        user_query = db.session.execute(text("SELECT COUNT(*) FROM users;"))
        users = user_query.fetchone()[0]

        return self.render('admin/index.html', watches=watches, orders=orders, reviews=reviews, users=users)
