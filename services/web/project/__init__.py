import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import (
    Flask,
    jsonify,
    send_from_directory,
    request,
    redirect,
    url_for
)

from flask_cors import CORS
from flask_jwt_extended import JWTManager
from .model.model import configure as config_db
from .serializer.serializer import configure as config_ma
from .endpoints.bp_company_products import bp_company_products
from .endpoints.bp_recharge import bp_recharge
from .endpoints.bp_user import bp_user
from .model.model import User, Company, Product, Recharge

def create_app():
    app = Flask(__name__)
    app.config.from_object("project.config.Config")
    CORS(app)
    config_db(app)
    config_ma(app)
    JWTManager(app)
    Migrate(app, app.db)

    app.register_blueprint(bp_user)
    app.register_blueprint(bp_company_products)
    app.register_blueprint(bp_recharge)
    
    @app.shell_context_processor
    def inject_models():
        return {
            'User': User,
            'Company': Company,
            'Product': Product,
            'Recharge': Recharge
        }


    return app
