from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from app.models.pins import Pins
from app.models.roles import Roles
from app.models.users import Users

blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@blueprint.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']

    user = Users.get_or_none(Users.email == email, Users.password == password)

    if user:
        access_token = create_access_token(identity=user.id)
        return jsonify({'success': True, 'token': access_token, 'role': user.role_id}), 200

    return jsonify({'success': False, 'message': 'Bad username or password'}), 401


@blueprint.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']
    role = request.form['role']
    name = request.form['name']
    phone = None
    info = None
    lat = None
    lng = None
    role = Roles.get(Roles.id == role)
    if role == 2:
        phone = request.form['phone']
        info = request.form['info']
        lat = request.form['lat']
        lng = request.form['lng']

    user = Users.create(email=email, password=password, role=role, name=name, phone=phone, info=info)

    if role == 2:
        Pins.create(user_id=user.id, lat=lat, lng=lng, type=2)

    return jsonify({'success': True, 'message': 'User registered!'}), 200


@blueprint.route('/logout')
def logout():
    return 'Logout'
