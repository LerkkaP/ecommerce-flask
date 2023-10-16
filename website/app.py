from flask_wtf.csrf import CSRFProtect
from flask import Flask
from flask_admin import Admin

from .config import Config
from .db import db

from .routes.watch_routes import watches
from .routes.auth_routes import auth
from .routes.cart_routes import carts
from .routes.profile_routes import profile
from .routes.checkout_routes import checkout

from .admin.routes.orders_routes import Orders
from .admin.routes.users_routes import Users
from .admin.routes.storage_routes import Storage
from .admin.routes.stats_routes import Stats

csrf = CSRFProtect()

def register_blueprints(app):
    app.register_blueprint(watches, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(carts, url_prefix='/')
    app.register_blueprint(profile, url_prefix='/')
    app.register_blueprint(checkout, url_prefix='/')
    
def register_admin_blueprints(app):
    admin = Admin(app, name='ecommerceFlask', template_mode='bootstrap4', index_view=Stats())
    admin.add_view(Orders(name='Orders', endpoint='orders'))
    admin.add_view(Users(name='Users', endpoint='users'))
    admin.add_view(Storage(name='Storage', endpoint='storage'))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    csrf.init_app(app)
    db.init_app(app)

    register_blueprints(app)
    register_admin_blueprints(app)

    return app
