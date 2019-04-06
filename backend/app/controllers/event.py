from flask import Blueprint, request, jsonify
from app.models.events import Events


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





