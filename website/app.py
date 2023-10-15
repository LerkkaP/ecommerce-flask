from flask import Flask, request, session, redirect, render_template
from flask_admin import Admin
from os import getenv
from dotenv import load_dotenv
from sqlalchemy.sql import text
from .db import db

load_dotenv()  

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
    app.config['FLASK_ADMIN_SWATCH'] = 'materia'
    app.secret_key = getenv("SECRET_KEY")

    db.init_app(app)

    from .routes.watch_routes import watches
    from .routes.auth_routes import auth
    from .routes.cart_routes import carts
    from .routes.profile_routes import profile
    from .routes.checkout_routes import checkout

    from .admin.routes.orders_routes import Orders
    from .admin.routes.users_routes import Users
    from .admin.routes.storage_routes import Storage
    from .admin.routes.stats_routes import Stats
    
    app.register_blueprint(watches, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(carts, url_prefix='/')
    app.register_blueprint(profile, url_prefix='/')
    app.register_blueprint(checkout, url_prefix='/')

    @app.before_request
    def check_admin_access():
        if request.path.startswith('/admin'):
            user_id = session.get('user_id')
            if user_id is not None:
                query = "SELECT privileges FROM users WHERE id=:id"
                result = db.session.execute(text(query), {'id': user_id})
                privileges = result.fetchone()

                if not (privileges and privileges[0] == 'admin'):
                    return render_template("messages/denied.html")
            else:
                return redirect('/login')
    
    admin = Admin(app, name='ecommerceFlask', template_mode='bootstrap4', index_view=Stats())
    admin.add_view(Orders(name='Orders', endpoint='orders'))
    admin.add_view(Users(name='Users', endpoint='users'))
    admin.add_view(Storage(name='Storage', endpoint='storage'))

    return app

