from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from operator import itemgetter

from app.models.events import Events
from app.models.users import Users
from app.models.users_events import Users_Events
from app.models.users_friends import Users_Friends

blueprint = Blueprint('account', __name__, url_prefix='/account')


@blueprint.route('/details', methods=['GET'])
@jwt_required
def index():
    current_user_id = get_jwt_identity()
    user = Users.get_or_none(Users.id == current_user_id)
    details_dict = {
        'picture': user.avatar,
        'name': user.name,
        'points': user.points,
        'cleaned': user.places_cleaned,
        'reported': user.places_reported,
        'nr_friends': 0
    }

    no_friends = len(Users_Friends.select().where(Users_Friends.friend == current_user_id))
    details_dict['nr_friends'] = no_friends

    return jsonify({'success': True, 'message': details_dict}), 200


@blueprint.route('/friends', methods=['GET'])
# @jwt_required
def friends():
    current_user_id = 1#get_jwt_identity()
    vals = {}
    friends = []
    suggestions = []
    for val in Users_Friends.select().where(Users_Friends.user == current_user_id):
        user = Users.get_or_none(Users.id == val.friend)
        friends.append({
            'name': user.name,
            'avatar': user.avatar
        })

    for user_event in Users_Events.select().where(Users_Events.user == current_user_id):
        user_events_new = Users_Events.select().where(Users_Events.event == user_event.event)
        for val in user_events_new:
            user = Users.get_or_none(Users.id== val.user)
            if user.id is not current_user_id:
                suggestions.append({
                    'name': user.name,
                    'avatar': user.avatar
                })

    for i in friends:
        try:
            suggestions.remove(i)
        except ValueError:
            pass
    result = {
        'friends': friends,
        'suggestions': suggestions
    }

    return jsonify({'success': True, 'message': result}), 200


@blueprint.route('/leaderboard', methods=['GET'])
@jwt_required
def leaderboard():
    users = Users.select().where(Users.role == 1)
    board = []
    for user in users:
        board.append({
            'name': user.name,
            'avatar': user.avatar,
            'points': user.points
        })

    newboard = sorted(board, key=itemgetter('points'), reverse=True)

    return jsonify({'success': True, 'message': newboard}), 200


@blueprint.route('/follow', methods=['POST'])
@jwt_required
def follow():
    friend_id = request.form[0]
    user_id = get_jwt_identity()

    Users_Friends.create(user=user_id, friend=friend_id)

    return jsonify({'success': True, 'message': 'follow'}), 200
