from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.badges import Badges
from app.models.events import Events
from app.models.users_badges import Users_Badges

blueprint = Blueprint('badge', __name__, url_prefix='/badge')


def create(user_id, badge_id):
    Users_Badges.create(user=user_id, badge=badge_id)
    return jsonify({'success': True, 'message': 'Your badge was created'}), 200


def create_specific_badge(type, user_id):
    badge = Badges.get(Badges.id == type)
    create(user_id, badge.id)


@blueprint.route('/invite', methods=['POST'])
@jwt_required
def invite():
    return jsonify({'success': True, 'message': 'Your event was created'}), 200


@blueprint.route('/all', methods=['GET'])
@jwt_required
def all():
    allEvents = []
    for event in Events.select():
        dict = {'title': event.title, 'description': event.description, 'start': event.time_start,
                'end': event.time_end}
        allEvents.append(dict)

    return jsonify({'success': True, 'message': allEvents}), 200


@blueprint.route('/get-user-badges', methods=['GET'])
@jwt_required
def get_user_badges():
    user_id = get_jwt_identity()
    result = []

    badges = Users_Badges.select().where(Users_Badges.user == user_id)

    for badge_id in badges:
        badge = Badges.get(Badges.id == badge_id.badge)
        result.append({
            'name': badge.name,
            'description': badge.description,
            'icon': badge.icon,
            'points': badge.points
        })

    return jsonify({'success': True, 'message': result}), 200
