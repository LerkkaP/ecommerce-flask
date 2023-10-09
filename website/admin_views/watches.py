from flask import redirect, url_for
from flask_admin import BaseView, expose
from sqlalchemy.sql import text

from .. import db

class Watches(BaseView):
    @expose('/')
    def index(self):
        query = db.session.execute(text("SELECT * FROM watches;"))

        watches = query.fetchall()

        watch_list = []
        for watch in watches:
            watches_dict = {
                'id': watch[0],
                'brand': watch[1],
                'model': watch[2],
                'price': watch[3],
                'description': watch[4]
            }
            watch_list.append(watches_dict)

        return self.render('admin/watches.html', watches=watch_list)
    