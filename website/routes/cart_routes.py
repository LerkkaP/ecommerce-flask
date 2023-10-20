from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from ..views.carts import add_watch_to_cart, show_cart, delete_from_cart, decrease_item_quantity, increase_item_quantity

from ..decorators import login_required

carts = Blueprint('carts', __name__)

@carts.route('/addcart', methods=['POST'])
@login_required
def add_cart():
    watch_id = request.form.get('watch_id')
    user_id = session.get("user_id")
    
    if request.method == "POST":
        add_watch_to_cart(watch_id, user_id)

        return redirect(url_for('watches.watch_detail', id=watch_id))
    
@carts.route('/shopping-cart', methods=['GET'])
@login_required
def shopping_cart():
    user_id = session.get("user_id")

    items, total_sum = show_cart(user_id)

    return render_template("checkout/cart.html", items=items, total_sum=total_sum)

@carts.route('/deleteitem/<int:watch_id>', methods=['POST'])
@login_required
def delete_item(watch_id):

    delete_from_cart(watch_id)

    return redirect(url_for('carts.shopping_cart'))

@carts.route('/decrease_quantity',  methods=['POST'])
@login_required
def decrease_quantity():
    watch_id = request.form.get('watch_id')
    quantity = request.form.get('quantity')

    decrease_item_quantity(watch_id, quantity)

    return redirect(url_for('carts.shopping_cart'))


@carts.route('/increase_quantity',  methods=['POST'])
@login_required
def increase_quantity():
    watch_id = request.form.get('watch_id')

    increase_item_quantity(watch_id)

    return redirect(url_for('carts.shopping_cart'))


