from datetime import datetime

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from app.models.events import Events
import dateutil.parser
from app.models.pins import Pins

blueprint = Blueprint('event', __name__, url_prefix='/event')


@blueprint.route('/create', methods=['POST'])
@jwt_required
def create():
    pin_id = request.form['pin_id']
    time_start = dateutil.parser.parse(request.form['time_start'])
    time_end = dateutil.parser.parse(request.form['time_end'])
    description = request.form['description']
    title = request.form['title']

    Events.create(pin=pin_id, time_start=time_start, time_end=time_end, description=description, title=title)

    return jsonify({'success': True, 'message': 'Your event was created'}), 200


@blueprint.route('/invite', methods=['POST'])
@jwt_required
def invite():

    return jsonify({'success': True, 'message': 'Your event was created'}), 200


@blueprint.route('/all', methods=['GET'])
@jwt_required
def all():
    allEvents = []
    for event in Events.select():
        dict = {'id': event.id, 'title': event.title, 'description': event.description, 'start': str(event.time_start),
                'end': str(event.time_end)}
        allEvents.append(dict)

    return jsonify({'success': True, 'message': allEvents}), 200
