from flask import redirect, url_for
from flask import redirect, url_for, request
from flask_admin import BaseView, expose

from ..views.storage import show_storage, add_to_storage, delete_from_storage

from ...decorators import admin_login_required


class Storage(BaseView):
    @expose('/')
    @admin_login_required
    def index(self):
        watches = show_storage()

        return self.render('admin/watches.html', watches=watches)
    

    @expose('/add_watch', methods=["POST"])
    @admin_login_required
    def add_watch(self):
        if request.method == "POST":
            brand = request.form.get("brand")
            model = request.form.get("model")
            price = request.form.get("price")
            description = request.form.get("description")

            add_to_storage(brand, model, price, description)

            return redirect(url_for('.index'))
    
    @expose('/delete_watch/<int:watch_id>', methods=["POST"])
    @admin_login_required
    def delete_watch(self, watch_id):
        if request.method == "POST":
            delete_from_storage(watch_id)

            return redirect(url_for('.index'))