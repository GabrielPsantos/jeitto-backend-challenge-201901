from marshmallow import fields, post_load
from flask_marshmallow import Marshmallow
from project.model.model import User, Company, Product, Recharge

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class UserSchema(ma.Schema):
    class Meta:
        model = User

    email = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)


class ProductSchema(ma.Schema):
    class Meta:
        model = Product

    product_id = fields.Str(required=True)
    value = fields.Float(required=True)

    @post_load
    def make_product(self, data, **kwargs):
        return Product(**data)


class CompanySchema(ma.Schema):
    class Meta:
        model = Company

    company_id = fields.Str(required=True)
    products = ma.Nested(ProductSchema, required=True, many=True)

    @post_load
    def make_company(self, data, **kwargs):
        return Company(**data)


class RechargeSchema(ma.Schema):
    class Meta:
        model = Recharge
        load_instance = False

    id = fields.Str(dump_only=True)
    company_id = fields.Str(required=True)
    product_id = fields.Str(required=True)
    phone_number = fields.Str(required=True)
    value = fields.Float(required=True)

    @post_load
    def make_recharge(self, data, **kwargs):
        return Recharge(**data)
