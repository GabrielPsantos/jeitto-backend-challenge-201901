from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha256
import datetime

db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class User(db.Model):
    __tablename__ = "users"

    def __init__(self, email, username, password, **kwargs):
        super(User, self).__init__(**kwargs)
        self.email = email
        self.username = username
        self.password = password

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def gen_hash(self):
        self.password = pbkdf2_sha256.hash(self.password)

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.password)


class Company(db.Model):
    __tablename__ = "company"
    company_id = db.Column('company_id', db.String(20), primary_key=True)

    def __init__(self, company_id, **kwargs):
        super(Company, self).__init__(**kwargs)
        self.company_id = company_id


class Product(db.Model):
    __tablename__ = "product"
    product_id = db.Column('product_id', db.String(20), primary_key=True)
    value = db.Column(db.Float(), nullable=False)

    company_id = db.Column(db.String(20), db.ForeignKey('company.company_id'))
    company = db.relationship('Company', backref='products', lazy='select',
                              cascade="all, delete")


class Recharge(db.Model):
    __tablename__ = "recharge"

    id = db.Column('id', db.Integer, primary_key=True)

    company_id = db.Column(db.String(20), db.ForeignKey('company.company_id'))
    company = db.relationship('Company', backref='company_recharges', lazy='select',
                              cascade="all, delete")

    product_id = db.Column(db.String(20), db.ForeignKey('product.product_id'))
    product = db.relationship('Product', backref='product_recharges', lazy='select',
                              cascade="all, delete")

    phone_number = db.Column(db.String(25), nullable=False)
    value = db.Column(db.Float(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
