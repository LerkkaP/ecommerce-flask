"""
Module for handling user-related routes in the admin panel.
"""

from flask import redirect, url_for
from flask_admin import BaseView, expose

from website.decorators import admin_login_required
from website.admin.views.users import users_page, remove_user



class Users(BaseView):
    @expose("/")
    @admin_login_required
    def index(self):
        """
        Display a list of users.

        Returns:
            str: Rendered HTML content.
        """
        users = users_page()

        return self.render("admin/users.html", users=users)

    @expose("/delete_user/<int:user_id>", methods=["POST"])
    @admin_login_required
    def delete_user(self, user_id):
        """
        Delete a user.

        Keyword arguments:
            user_id (int): The ID of the user to be deleted.

        Returns:
            str: Redirect URL.
        """
        remove_user(user_id)

        return redirect(url_for("users.index"))
