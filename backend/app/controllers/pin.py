import os
from random import randint

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.pictures import Pictures
from app.models.pins import Pins
from app.models.users import Users

blueprint = Blueprint('pin', __name__, url_prefix='/pin')


@blueprint.route('/create', methods=['POST'])
# @jwt_required
def create():
    # user_id = get_jwt_identity()
    user_id = 1
    lat = request.form['lat']
    lng = request.form['lng']
    title = request.form['title']
    description = request.form['description']
    f = None
    if len(request.files) > 0:
        f = request.files['file']
    filename = None
    if f is not None:
        value = randint(1, 100000000)
        path = 'instance/images'
        name = '{}-{}'.format(user_id, value)
        extension = f.filename.split('.')[1]
        filename = '{}/{}.{}'.format(path, name, extension)
        f.save(os.path.join(filename))

    pin = Pins.create(user_id=user_id, lat=lat, lng=lng, title=title, description=description, type=1)
    if filename is not None:
        Pictures.create(url=filename, pin=pin.id)

    return jsonify({'success': True, 'message': 'Your pin was created'}), 200



@blueprint.route('/details', methods=['GET'])
def details():
    id = request.args['pin_id']

    pin = Pins.get_or_none(Pins.id == id)
    #user
    if pin.type == 1:
        mydict = {'title': pin.title, 'description': pin.description,
                  'created_at': pin.created_at, 'type': 1}
    # company
    else:
        user_id = pin.user
        user = Users.get_or_none(Users.id == user_id)
        mydict = {'type': 2, 'email': user.email, 'info': user.info, 'phone': user.phone}

    return jsonify({'success': True, 'message': mydict}), 200



@blueprint.route('/my_pins', methods=['GET'])
@jwt_required
def my_pins():
    user_id = get_jwt_identity()

    my_pins = []

    for pin in Pins.select().where(Pins.user == user_id):
        my_pins.append(pin.created_at)

    return jsonify({'success': True, 'message': my_pins}), 200



@blueprint.route('/all', methods=['GET'])
def allPins():
    allPins = []
    for pin in Pins.select():
        dict = {'id': pin.id, 'position': {'lat': pin.lat, 'lng': pin.lng}, 'type': pin.type}
        allPins.append(dict)

    return jsonify({'success': True, 'message': allPins}), 200






