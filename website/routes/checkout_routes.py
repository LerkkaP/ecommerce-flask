from flask import Blueprint, render_template, redirect, flash, request
from ..views.checkout import checkout_items

from ..decorators import login_required

checkout = Blueprint('checkout', __name__)

@checkout.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout_page():
    if request.method == 'GET':
        return render_template("checkout/checkout.html")
    elif request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        shipping_address = request.form.get('shipping_address')
        billing_address = request.form.get('billing_address')
        phone_number = request.form.get('phone_number')
        email = request.form.get('email')
        payment_method = request.form.get('payment')

        checkout_items(first_name, last_name, shipping_address, billing_address, phone_number, email, payment_method)

        return render_template("messages/thanks_page.html")
