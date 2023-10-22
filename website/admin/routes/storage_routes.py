"""
Module for managing the storage of watches in the admin panel.
"""

from flask import redirect, url_for, request
from flask_admin import BaseView, expose

from website.decorators import admin_login_required
from website.admin.views.storage import show_storage, add_to_storage, delete_from_storage


class Storage(BaseView):
    @expose("/")
    @admin_login_required
    def index(self):
        """
        Display the list of watches in the storage.

        Returns:
            str: Rendered HTML content.
        """
        watches = show_storage()

        return self.render("admin/watches.html", watches=watches)

    @expose("/add_watch", methods=["POST"])
    @admin_login_required
    def add_watch(self):
        """
        Add a watch to the storage.

        Returns:
            str: Redirect URL.
        """
        if request.method == "POST":
            brand = request.form.get("brand")
            model = request.form.get("model")
            price = request.form.get("price")
            description = request.form.get("description")

            add_to_storage(brand, model, price, description)

            return redirect(url_for(".index"))

        return None

    @expose("/delete_watch/<int:watch_id>", methods=["POST"])
    @admin_login_required
    def delete_watch(self, watch_id):
        """
        Delete a watch from the storage.

        Returns:
            str: Redirect URL.
        """
        if request.method == "POST":
            delete_from_storage(watch_id)

            return redirect(url_for(".index"))

        return None
