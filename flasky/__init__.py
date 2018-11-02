from flask import Flask

from flasky.config import DevelopmentConfig
from flasky.product.product_view import products_bp
from flasky.auth.views import auth_bp
from flasky.database.postgres import db
from flasky.sale.sale_view import sales_bp
from flasky.cart.cart_view import cart_bp


def create_app(config_name=None):

    app = Flask(__name__)
    # configure app
    if config_name is not None:
        app.config.from_object(config_name)
    else:
        app.config.from_object(DevelopmentConfig)
        # database setup
        db.connect('')
        db.create_db_tables()
    # register blueprints
    app.register_blueprint(products_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(sales_bp)
    app.register_blueprint(cart_bp)

    return app
