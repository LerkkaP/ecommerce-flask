from flask import redirect, url_for
from flask_admin import BaseView, expose

from ..views.users import users_page, remove_user

class Users(BaseView):
    @expose('/')
    def index(self):
        users = users_page()
        
        return self.render('admin/users.html', users=users)
    
    @expose('/delete_user/<int:user_id>', methods=['POST'])
    def delete_user(self, user_id):
        remove_user(user_id)

        return redirect(url_for('users.index'))
    
        