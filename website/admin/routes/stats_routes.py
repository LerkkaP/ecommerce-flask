from flask_admin import AdminIndexView
from flask_admin import BaseView, expose

from ..views.stats import show_stats
from ...decorators import admin_login_required

class Stats(AdminIndexView):
    @expose('/')
    @admin_login_required
    def index(self):
        
        watches, orders, reviews, users = show_stats()

        return self.render('admin/index.html', watches=watches, orders=orders, reviews=reviews, users=users)