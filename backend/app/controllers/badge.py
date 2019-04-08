from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.badges import Badges
from app.models.users import Users
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


def assign_badge_clean(user_id):
    user = Users.get(user_id)
    places_cleaned = user.places_cleaned
    badge = None

    if places_cleaned == 1:
        badge = Badges.get(id=1)
    elif places_cleaned == 2:
        badge = Badges.get(id=4)
    elif places_cleaned == 5:
        badge = Badges.get(id=5)
    elif places_cleaned == 10:
        badge = Badges.get(id=6)

    if badge is not None:
        Users_Badges.create(user=user_id, badge=badge.id)

        points = Users.get(Users.id==user_id).points + badge.points
        query = Users.update(points=points).where(Users.id == user_id)
        query.execute()


def assign_badge_reported(user_id):
    user = Users.get(user_id)
    places_reported = user.places_reported
    badge = None

    if places_reported == 1:
        badge = Badges.get(id=3)
    elif places_reported == 2:
        badge = Badges.get(id=7)
    elif places_reported == 3:
        badge = Badges.get(id=8)
    elif places_reported == 5:
        badge = Badges.get(id=9)
    Users_Badges.create(user=user_id, badge=badge.id)

    if badge is not None:
        Users_Badges.create(user=user_id, badge=badge.id)

        points = Users.get(Users.id==user_id).points + badge.points
        query = Users.update(points=points).where(Users.id == user_id)
        query.execute()
