from flask import Blueprint, request, current_app, jsonify
from flask_jwt_extended import jwt_required
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import SQLAlchemyError
import logging

from project.serializer.serializer import CompanySchema, ProductSchema
from project.model.model import Company, Product

bp_company_products = Blueprint('companyProducts', __name__)


@bp_company_products.route("/CompanyProducts/", methods=['GET'])
@jwt_required
def listOneAll():
    cSchema = CompanySchema(many=True)
    c_id = request.args.get('company_id')
    if c_id:
        result = Company.query.filter(Company.company_id == c_id)
    else:
        result = Company.query.all()

    data = cSchema.jsonify(result)
    status = 404 if not data else 200
    return data, status


@bp_company_products.route("/CompanyProducts/", methods=['POST'])
@jwt_required
def create():
    cSchema = CompanySchema()
    try:
        payload = cSchema.load(request.json)
        current_app.db.session.add(payload)
        current_app.db.session.commit()
        result = cSchema.jsonify(payload)
    except SQLAlchemyError as e:
        current_app.db.session.rollback()
        return jsonify({'error': 'Data related error'}), 422
    except Exception as e:
        return jsonify(e.messages), 422
    else:
        return result


@bp_company_products.route("/CompanyProducts/", methods=['PUT'])
@jwt_required
def update():
    cSchema = CompanySchema()
    try:
        payload = cSchema.load(request.json)
        id = payload.company_id
        query = Company.query.get(id)
        current_app.db.session.merge(payload)
        current_app.db.session.commit()
        result = cSchema.jsonify(payload)
    except Exception as e:
        return jsonify(e.messages), 422
    else:
        return result


@bp_company_products.route("/CompanyProducts/", methods=['DELETE'])
@jwt_required
def delete():
    c_id = request.args.get('company_id')
    if not c_id:
        return jsonify({'error': 'Missing Field "company_id"'}), 401
    c_obj = Company.query.filter(Company.company_id == c_id).first()
    if not c_obj:
        return jsonify({}), 404
    else:
        current_app.db.session.delete(c_obj)
        current_app.db.session.commit()
        return jsonify({}), 204
