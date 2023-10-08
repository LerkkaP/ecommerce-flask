from flask_admin import BaseView, expose
from sqlalchemy.sql import text

from .. import db

class Users(BaseView):
    @expose('/')
    def index(self):
        query = db.session.execute(text("SELECT username, privileges FROM users;"))

        users = query.fetchall()

        users_list = []
        for user in users:
            users_dict = {
                'username': user[0],
                'privileges': user[1],
            }
            users_list.append(users_dict)

        return self.render('admin/users.html', users=users_list)