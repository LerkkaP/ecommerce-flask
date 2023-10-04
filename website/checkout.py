from flask import Blueprint, render_template, redirect, flash, session

from sqlalchemy.sql import text
from . import db

checkout = Blueprint('checkout', __name__)


@checkout.route('/checkout')
def checkout_items():
    user_id = session.get("user_id")
    search = db.session.execute(text("SELECT * FROM cart WHERE user_id=:user_id;"), {"user_id": user_id})
    search_results = search.fetchall()
        

    return render_template("checkout.html")
