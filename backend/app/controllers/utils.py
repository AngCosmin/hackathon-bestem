from flask import Blueprint, request, jsonify
from app.models.events import Events
from app.models.users import Users

blueprint = Blueprint('utils', __name__, url_prefix='/utils')


@blueprint.route('/get_emails', methods=['GET'])
def get_emails():
    string = 'ioana'#request.form['string']

    users = Users.select().where(Users.email.contains(string))

    result = []
    for user in users:
        result.append({
            'email': user.email,
            'name': user.name
        })

    return jsonify({'success': True, 'message': result}), 200
