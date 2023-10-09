from flask import redirect, url_for
from flask_admin import BaseView, expose
from sqlalchemy.sql import text

from .. import db

class Users(BaseView):
    @expose('/')
    def index(self):
        query = db.session.execute(text("SELECT id, username, privileges FROM users;"))

        users = query.fetchall()

        users_list = []
        for user in users:
            users_dict = {
                'id': user[0],
                'username': user[1],
                'privileges': user[2],
            }
            users_list.append(users_dict)

        return self.render('admin/users.html', users=users_list)
    
    @expose('/delete/<int:user_id>', methods=['POST'])
    def delete_user(self, user_id):
        db.session.execute(text("DELETE FROM users WHERE id=:user_id"), {"user_id": user_id})
        db.session.commit()

        return redirect(url_for('users.index'))
    
        