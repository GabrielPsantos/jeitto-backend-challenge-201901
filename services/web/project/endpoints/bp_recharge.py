from flask import Blueprint, request, current_app, jsonify
from flask_jwt_extended import jwt_required
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import SQLAlchemyError
import logging

from project.serializer.serializer import RechargeSchema
from project.model.model import Recharge

bp_recharge = Blueprint('phoneRecharges', __name__)


@bp_recharge.route("/PhoneRecharges/", methods=['GET'])
@jwt_required
def listOneAll():
    rSchema = RechargeSchema(many=True)
    r_id = request.args.get('id')
    r_phone = request.args.get('phone_number')
    if r_id:
        result = Recharge.query.filter(Recharge.id == r_id)
    elif r_phone:
        result = Recharge.query.filter(Recharge.phone_number == r_phone)
    else:
        result = Recharge.query.all()

    data = rSchema.jsonify(result)
    status = 404 if not data else 200
    return data, status


@bp_recharge.route("/PhoneRecharges/", methods=['POST'])
@jwt_required
def create():
    rSchema = RechargeSchema()
    try:
        payload = rSchema.load(request.json)
        current_app.db.session.add(payload)
        current_app.db.session.commit()
        result = rSchema.jsonify(payload)
    except SQLAlchemyError as e:
        print(e)
        return jsonify({'error': 'Data related error'}), 422
    except Exception as e:
        return jsonify(e.messages), 422
    else:
        return result
