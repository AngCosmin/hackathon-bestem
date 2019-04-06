from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from app.models.users import Users

blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@blueprint.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user = Users.get_or_none(Users.email == email, Users.password == password)

    if user:
        access_token = create_access_token(identity=user.id)
        return jsonify({'success': True, 'token': access_token}), 200

    return jsonify({'success': False, 'message': 'Bad username or password'}), 401


@blueprint.route('/logout')
def logout():
    return 'Logout'
