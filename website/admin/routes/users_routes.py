from flask import redirect, url_for
from flask_admin import BaseView, expose

from ..views.users import users_page, remove_user

from ...decorators import admin_login_required


class Users(BaseView):
    @expose('/')
    @admin_login_required
    def index(self):
        users = users_page()
        
        return self.render('admin/users.html', users=users)
    
    @expose('/delete_user/<int:user_id>', methods=['POST'])
    @admin_login_required
    def delete_user(self, user_id):
        remove_user(user_id)

        return redirect(url_for('users.index'))
    
        