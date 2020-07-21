import logging
from flask import Blueprint, request, jsonify, current_app
from datetime import timedelta
from flask_jwt_extended import create_access_token, create_refresh_token
from project.model.model import User
from project.serializer.serializer import UserSchema
from sqlalchemy.exc import SQLAlchemyError

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

bp_user = Blueprint('user', __name__)


@bp_user.route('/signin', methods=['POST'])
def register():
    try:
        us = UserSchema()
        user = us.load(request.json)
        user.gen_hash()
        current_app.db.session.add(user)
        current_app.db.session.commit()
    except SQLAlchemyError as e:
        print(e)
        return jsonify({'error': 'Data related error'}), 422
    except Exception as e:
        return jsonify(e.messages), 422
    else:
        return us.jsonify(user), 201


@bp_user.route('/login', methods=['POST'])
def login():
    try:
        user = UserSchema().load(request.json)
        user_obj = User.query.filter_by(username=user.username).first()
        if user_obj and user_obj.verify_password(request.json['password']):
            acess_token = create_access_token(
                identity=user_obj.id,
                expires_delta=timedelta(days=1)
            )
            refresh_token = create_refresh_token(identity=user_obj.id)

            return jsonify({
                'acess_token': acess_token,
                'message': 'success'
            }), 200
    except SQLAlchemyError as e:
        print(e)
        return jsonify({'error': 'Data related error'}), 422
    except Exception as e:
        return jsonify(e.messages), 422
    else:
        return jsonify({
            'message': 'Wrong credentials'
        }), 401

@bp_user.route('/health-check', methods=['GET'])
def health():
    return {"I'm": "alive"}