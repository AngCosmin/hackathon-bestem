from flask import Blueprint, request, jsonify
from app.models.events import Events

import datetime


blueprint = Blueprint('event', __name__, url_prefix='/event')


@blueprint.route('/create', methods=['POST'])
def create():
    pin_id = request.form['pid_id']
    time_start = request.form['time_start']
    time_end = request.form['time_end']
    description = request.form['description']
    title = request.form['title']

    Events.create(pin=pin_id, time_start=time_start, time_end=time_end, description=description, title=title)

    return jsonify({'success': True, 'message': 'Your event was created'}), 200



@blueprint.route('/invite', methods=['POST'])
def invite():


    return jsonify({'success': True, 'message': 'Your event was created'}), 200



@blueprint.route('/all', methods=['GET'])
def all():
    allEvents = []
    for event in Events.select():
        dict = {'title': event.title, 'description': event.description, 'start': event.time_start, 'end': event.time_end}
        allEvents.append(dict)

    return jsonify({'success': True, 'message': allEvents}), 200



