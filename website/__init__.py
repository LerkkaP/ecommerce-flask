from flask import Flask, request, session, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from os import getenv
from dotenv import load_dotenv
from sqlalchemy.sql import text

load_dotenv()  

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
    app.config['FLASK_ADMIN_SWATCH'] = 'materia'
    app.secret_key = getenv("SECRET_KEY")

    db.init_app(app)

    from .watches import watches
    from .auth import auth
    from .carts import carts
    from .profile import profile
    from .checkout import checkout

    from .admin_views.orders import Orders
    from .admin_views.users import Users
    from .admin_views.storage import Storage
    from .admin_views.stats import Stats

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
                    return render_template("denied.html")
            else:
                return redirect('/login')
    
    admin = Admin(app, name='ecommerceFlask', template_mode='bootstrap4', index_view=Stats())
    admin.add_view(Orders(name='Orders', endpoint='orders'))
    admin.add_view(Users(name='Users', endpoint='users'))
    admin.add_view(Storage(name='Storage', endpoint='storage'))


    return app

