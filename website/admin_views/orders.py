from flask_admin import BaseView, expose
from sqlalchemy.sql import text

from .. import db

class Orders(BaseView):
    @expose('/')
    def index(self):
        query = db.session.execute(text("SELECT watch_id, first_name, last_name, shipping_address, billing_address, phone_number, email, quantity, payment_method, order_date FROM orders GROUP BY id ORDER BY order_date;"))

        orders = query.fetchall()

        orders_list = []
        for order in orders:
            orders_dict = {
                'watch_id': order[0],
                'first_name': order[1],
                'last_name': order[2],
                'shipping_address': order[3],
                'billing_address': order[4],
                'phone_number': order[5],
                'email': order[6],
                'quantity': order[7],
                'payment_method': order[8],
                'order_date': order[9]
            }
            orders_list.append(orders_dict)

        return self.render('admin/orders.html', orders=orders_list)
    