from flask import redirect, url_for, request
from flask_admin import BaseView, expose
from ..views.orders import show_orders, remove_order

class Orders(BaseView):
    @expose('/')
    def index(self):
        orders = show_orders()
        
        return self.render('admin/orders.html', orders=orders)
    
    @expose('/delete_order', methods=['POST'])
    def delete_order(self):
        id = request.form.get("order_id")
        user_id = request.form.get("user_id")

        remove_order(id, user_id)

        return redirect(url_for('orders.index'))
 