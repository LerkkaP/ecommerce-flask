from flask_admin import BaseView, expose

from sqlalchemy.sql import text

class Orders(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/orders.html')