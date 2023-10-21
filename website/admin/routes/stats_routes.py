"""
Module for displaying statistics in the admin panel.
"""

from flask_admin import AdminIndexView, expose

from website.decorators import admin_login_required
from website.admin.views.stats import show_stats



class Stats(AdminIndexView):
    @expose("/")
    @admin_login_required
    def index(self):
        """
        Render the admin index page with statistics.

        Returns:
            str: Rendered HTML content.
        """

        watches, orders, reviews, users = show_stats()

        return self.render("admin/index.html",
                   watches=watches,
                   orders=orders,
                   reviews=reviews,
                   users=users)
