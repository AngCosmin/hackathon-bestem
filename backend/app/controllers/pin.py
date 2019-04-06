import os
from random import random

from flask import current_app as app
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename

from app.models.pictures import Pictures
from app.models.pins import Pins

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
    f = request.files['file']
    filename = None
    if f is not None:
        value = random(100000000)
        f.save(os.path.join(app.instance_path, 'images', secure_filename(str(user_id) + str(value))))
        filename = app.instance_path + '/images/' + str(user_id) + str(value)
    pin = Pins.create(user_id=user_id, lat=lat, lng=lng, title=title, description=description)
    if filename is not None:
        Pictures.create(url=filename, pin=pin.id)

    return jsonify({'success': True, 'message': 'Your pin was created'}), 401


@blueprint.route('/get_status', methods=['GET'])
def get_status():
    id = request.args['pin_id']

    pin = Pins.get_or_none(Pins.id == id)
    mydict = {'pin' : 'jmekerie'}
    ## get values for pop up

    return jsonify({'success': True, 'message': mydict}), 401


@blueprint.route('/my_pins', methods=['GET'])
@jwt_required
def my_pins():
    user_id = get_jwt_identity()

    my_pins = []

    for pin in Pins.select().where(Pins.user == user_id):
        my_pins.append(pin.created_at)

    return jsonify({'success': True, 'message': my_pins}), 401


@blueprint.route('/all', methods=['GET'])
def allPins():
    allPins = []
    for pin in Pins.select():
        dict = {'id': pin.id, 'position': {'lat': pin.lat, 'lng': pin.lng}, 'type': pin.type}
        allPins.append(dict)

    return jsonify({'success': True, 'message': allPins}), 401



