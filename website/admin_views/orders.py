from flask import redirect, url_for
from flask_admin import BaseView, expose
from sqlalchemy.sql import text

from .. import db

class Orders(BaseView):
    @expose('/')
    def index(self):
        query = db.session.execute(text("SELECT user_id, watch_id, first_name, last_name, shipping_address, billing_address, phone_number, email, quantity, payment_method, order_date FROM orders GROUP BY id ORDER BY order_date;"))

        orders = query.fetchall()

        orders_list = []
        for order in orders:
            orders_dict = {
                'user_id': order[0],
                'watch_id': order[1],
                'first_name': order[2],
                'last_name': order[3],
                'shipping_address': order[4],
                'billing_address': order[5],
                'phone_number': order[6],
                'email': order[7],
                'quantity': order[8],
                'payment_method': order[9],
                'order_date': order[10]
            }
            orders_list.append(orders_dict)

        return self.render('admin/orders.html', orders=orders_list)
    
    @expose('/delete_order/<int:user_id>', methods=['POST'])
    def delete_order(self, user_id):
        db.session.execute(text("DELETE FROM orders WHERE user_id=:user_id"), {"user_id": user_id})
        db.session.commit()

        return redirect(url_for('orders.index'))
 
    