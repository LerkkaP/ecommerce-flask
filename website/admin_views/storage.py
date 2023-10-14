from flask import redirect, url_for
from flask import redirect, url_for, request
from flask_admin import BaseView, expose
from sqlalchemy.sql import text

from ..db import db

class Storage(BaseView):
    @expose('/')
    def index(self):
        query = db.session.execute(text("SELECT * FROM watches;"))

        watches = query.fetchall()

        return self.render('admin/watches.html', watches=watches)
    

    @expose('/add_watch', methods=["POST"])
    def add_watch(self):
        if request.method == "POST":
            brand = request.form.get("brand")
            model = request.form.get("model")
            price = request.form.get("price")
            description = request.form.get("description")
            db.session.execute(text("INSERT INTO watches (brand, model, price, description) VALUES (:brand, :model, :price, :description)"), {"brand": brand, "model": model, "price": price, "description": description})
            db.session.commit()

            return redirect(url_for('.index'))
    
    @expose('/delete_watch/<int:watch_id>', methods=["POST"])
    def delete_watch(self, watch_id):
        if request.method == "POST":
            db.session.execute(text("DELETE FROM watches WHERE id=:watch_id"), {"watch_id": watch_id})
            db.session.commit()
            return redirect(url_for('.index'))




            
    