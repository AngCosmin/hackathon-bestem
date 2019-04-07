from datetime import datetime

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.events import Events
import dateutil.parser

from app.models.users import Users
from app.models.users_events import Users_Events


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


@blueprint.route('/going', methods=['POST'])
@jwt_required
def going():
    user_id = get_jwt_identity()
    event_id = request.form['event_id']
    Users_Events.create(user=user_id, event=event_id)
    return jsonify({'success': True, 'message': 'Created successfully'}), 200


@blueprint.route('/get', methods=['POST'])
@jwt_required
def get():
    user_id = get_jwt_identity()
    event_id = request.form['event_id']
    event = Events.get_or_none(Events.id == event_id)

    users_events = Users_Events.select().where(event == event_id)
    users_list = []
    for aux in users_events:
        user = Users.get_or_none(Users.id == aux.user)
        dict = {
            'name': user.name,
            'avatar': user.avatar,
            'id': user.id
        }
        users_list.append(dict)

    result = {
        'title': event.title,
        'description': event.description,
        'time_start': event.time_start,
        'time_end': event.time_end,
        'users': users_list
    }

    return jsonify({'success': True, 'message': result}), 200


@blueprint.route('/my_events', methods=['GET'])
@jwt_required
def my_events():
    user_id = get_jwt_identity()
    users_events = Users_Events.select().where(user=user_id)

    my_events =[]
    for user_event in users_events:
        event = Events.get(Events.id == user_event.event)
        dict = {
            'title': event.title,
            'time_start': event.time_start,
            'time_end': event.time_end
        }
        my_events.append(dict)

    return jsonify({'success': True, 'message': my_events}), 200
