from flask_admin import BaseView, expose

from sqlalchemy.sql import text

class Users(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/users.html')