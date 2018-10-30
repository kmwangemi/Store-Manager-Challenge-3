from flask import Flask

import os
from instance.config import app_config
from app.api.V2.views.product_view import product
from app.api.V2.views.sale_view import sale
from app.api.V2.views.user_view import user
from db_con import DbSetup

def create_app(config_name="development"):
    '''configuring the Flask App'''
    app = Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])

    with app.app_context():
        db = DbSetup()
        db.create_tables()


    app.register_blueprint(product)
    app.register_blueprint(sale)
    app.register_blueprint(user)
  
    return app