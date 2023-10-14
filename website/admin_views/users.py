from flask import redirect, url_for
from flask_admin import BaseView, expose
from sqlalchemy.sql import text

from ..db import db

class Users(BaseView):
    @expose('/')
    def index(self):
        query = db.session.execute(text("SELECT id, username, privileges FROM users;"))

        users = query.fetchall()
        
        return self.render('admin/users.html', users=users)
    
    @expose('/delete_user/<int:user_id>', methods=['POST'])
    def delete_user(self, user_id):
        db.session.execute(text("DELETE FROM users WHERE id=:user_id"), {"user_id": user_id})
        db.session.commit()

        return redirect(url_for('users.index'))
    
        