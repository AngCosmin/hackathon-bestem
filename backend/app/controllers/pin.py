import os
from random import randint

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from imgurpython import ImgurClient

from app.controllers.badge import assign_badge_reported
from app.models.pictures import Pictures
from app.models.pins import Pins
from app.models.users import Users

blueprint = Blueprint('pin', __name__, url_prefix='/pin')
imgur_client = ImgurClient('980b05841441b73', '3e90da14519e42a635835cdd14028c144cef9e5a')


@blueprint.route('/create', methods=['POST'])
@jwt_required
def create():
    user_id = get_jwt_identity()
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
        image = imgur_client.upload_from_path(filename)
        Pictures.create(url=image['link'], pin=pin.id)

    user = Users.get_or_none(Users.id == user_id)
    query = Users.update(places_reported=(user.places_reported + 1)).where(Users.id == user_id)
    query.execute()

    assign_badge_reported(user.id)

    return jsonify({'success': True, 'message': 'Your pin was created'}), 200


@blueprint.route('/details', methods=['GET'])
@jwt_required
def details():
    id = request.args['pin_id']

    pin = Pins.get_or_none(Pins.id == id)
    # user
    if pin.type == 1:
        mydict = {
            'title': pin.title,
            'description': pin.description,
            'created_at': pin.created_at,
            'type': 1,
            'pictures': [],
            'status': pin.status,
        }

        pictures = Pictures.select().where(Pictures.pin == id)

        for picture in pictures:
            mydict['pictures'].append(picture.url)

    # company
    else:
        user_id = pin.user
        user = Users.get_or_none(Users.id == user_id)
        pictures = [user.avatar]
        mydict = {
            'type': 2,
            'name': user.name,
            'email': user.email,
            'info': user.info,
            'phone': user.phone,
            'pictures': pictures
        }

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
@jwt_required
def allPins():
    allPins = []
    for pin in Pins.select():
        dict = {'id': pin.id, 'position': {'lat': pin.lat, 'lng': pin.lng}, 'type': pin.type, 'status': pin.status}
        allPins.append(dict)

    return jsonify({'success': True, 'message': allPins}), 200


@blueprint.route('/mark_as_clean', methods=['POST'])
@jwt_required
def mark_clean():
    user_id = get_jwt_identity()
    pin_id = request.form['pin_id']

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

    query = Pins.update(status=1).where(Pins.id == pin_id)
    query.execute()

    if filename is not None:
        image = imgur_client.upload_from_path(filename)
        Pictures.create(url=image['link'], pin=pin_id)

    return jsonify({'success': True, 'message': 'Your pin was updated'}), 200
