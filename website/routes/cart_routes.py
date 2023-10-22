"""
Module for handling cart-related routes and logic.
"""

from flask import Blueprint, render_template, request, redirect, session, url_for, flash

from website.decorators import login_required
from website.views.carts import (
    add_watch_to_cart, show_cart, delete_from_cart,
    decrease_item_quantity, increase_item_quantity
)

carts = Blueprint("carts", __name__)


@carts.route("/addcart", methods=["POST"])
@login_required
def add_cart():
    """
    Add a watch to the user's cart.

    Returns:
        str: Redirect URL.
    """
    watch_id = request.form.get("watch_id")
    user_id = session.get("user_id")

    if not watch_id:
        flash("Invalid watch ID.", category="error")
        return redirect(url_for("watches.watch_detail", watch_id=watch_id))

    if request.method == "POST":
        add_watch_to_cart(watch_id, user_id)

        return redirect(url_for("watches.watch_detail", watch_id=watch_id))

    return None

@carts.route("/shopping-cart", methods=["GET"])
@login_required
def shopping_cart():
    """
    Display the user's shopping cart.

    Returns:
        str: Rendered HTML content.
    """
    user_id = session.get("user_id")

    items, total_sum = show_cart(user_id)

    return render_template("checkout/cart.html", items=items, total_sum=total_sum)


@carts.route("/deleteitem/<int:watch_id>", methods=["POST"])
@login_required
def delete_item(watch_id):
    """
    Delete an item from the user's cart.

    Keyword arguments:
        watch_id (int): The ID of the watch to be deleted.
    
    Returns:
        str: Redirect URL.
    """

    delete_from_cart(watch_id)

    return redirect(url_for("carts.shopping_cart"))


@carts.route("/decrease_quantity",  methods=["POST"])
@login_required
def decrease_quantity():
    """
    Decrease the quantity of an item in the user's cart.

    Returns:
        str: Redirect URL.
    """
    watch_id = request.form.get("watch_id")
    quantity = request.form.get("quantity")

    decrease_item_quantity(watch_id, quantity)

    return redirect(url_for("carts.shopping_cart"))


@carts.route("/increase_quantity",  methods=["POST"])
@login_required
def increase_quantity():
    """
    Increase the quantity of an item in the user's cart.

    Returns:
        str: Redirect URL.
    """
    watch_id = request.form.get("watch_id")

    increase_item_quantity(watch_id)

    return redirect(url_for("carts.shopping_cart"))
