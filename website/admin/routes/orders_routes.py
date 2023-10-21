"""
Module for handling orders in the admin panel.
"""

from flask import redirect, url_for, request
from flask_admin import BaseView, expose

from website.decorators import admin_login_required
from website.admin.views.orders import show_orders, remove_order



class Orders(BaseView):
    @expose("/")
    @admin_login_required
    def index(self):
        """
        Render the admin orders page.

        Returns:
            str: Rendered HTML content.
        """
        orders = show_orders()

        return self.render("admin/orders.html", orders=orders)

    @expose("/delete_order", methods=["POST"])
    @admin_login_required
    def delete_order(self):
        """
        Delete an order.

        Returns:
            str: Redirect URL.
        """
        order_id = request.form.get("order_id")
        user_id = request.form.get("user_id")

        remove_order(order_id, user_id)

        return redirect(url_for("orders.index"))
