from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.pictures import Pictures
from app.models.users import Users
from app.models.users_friends import Users_Friends

blueprint = Blueprint('account', __name__, url_prefix='/account')


@blueprint.route('/', methods=['GET'])
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
@jwt_required
def friends():
    current_user_id = get_jwt_identity()
    friends = []
    for val in Users_Friends.select().where(Users_Friends.user == current_user_id):
        user = Users.get_or_none(Users.id == val.user)
        friends.append({
            'name': user.name,
            'avatar': user.avatar
        })

    return jsonify({'success': True, 'message': friends}), 200