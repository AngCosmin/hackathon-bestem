from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

blueprint = Blueprint('account', __name__, url_prefix='/account')


@blueprint.route('/')
@jwt_required
def index():
    current_user_id = get_jwt_identity()
    return jsonify(logged_in_as=current_user_id), 200


