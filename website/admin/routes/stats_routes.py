from flask_admin import AdminIndexView
from flask import redirect, url_for
from flask_admin import BaseView, expose

from ..views.stats import show_stats

class Stats(AdminIndexView):
    @expose('/')
    def index(self):
        
        watches, orders, reviews, users = show_stats()

        return self.render('admin/index.html', watches=watches, orders=orders, reviews=reviews, users=users)