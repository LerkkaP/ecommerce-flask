from flask import redirect, url_for, request
from flask_admin import BaseView, expose
from sqlalchemy.sql import text

from .. import db

class Orders(BaseView):
    @expose('/')
    def index(self):
        query = db.session.execute(text("SELECT id, user_id, watch_id, first_name, last_name, shipping_address, billing_address, phone_number, email, quantity, payment_method, order_date FROM orders GROUP BY id ORDER BY order_date;"))

        orders = query.fetchall()

        return self.render('admin/orders.html', orders=orders)
    
    @expose('/delete_order', methods=['POST'])
    def delete_order(self):
        id = request.form.get("order_id")
        user_id = request.form.get("user_id")
        db.session.execute(text("DELETE FROM orders WHERE id=:id AND user_id=:user_id"), {"id": id, "user_id": user_id})
        db.session.commit()

        return redirect(url_for('orders.index'))
 
    