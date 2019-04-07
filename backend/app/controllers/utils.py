from datetime import datetime
from email.mime.text import MIMEText

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.controllers.badge import assign_badge_clean
from app.models.events import Events
from app.models.pictures import Pictures
from app.models.pins import Pins
from app.models.users import Users
import smtplib

blueprint = Blueprint('utils', __name__, url_prefix='/utils')

@blueprint.route('/get_emails', methods=['GET'])
@jwt_required
def get_emails():
    string = request.form['string']

    users = Users.select().where(Users.email.contains(string))

    result = []
    for user in users:
        result.append({
            'email': user.email,
            'name': user.name
        })

    return jsonify({'success': True, 'message': result}), 200


@blueprint.route('/send_mail', methods=['GET'])
@jwt_required
def send_mail():
    current_user_id = get_jwt_identity()
    user = Users.get_or_none(Users.id == current_user_id)
    email_to = request.form['email_to']

    event_id = request.form['event_id']
    event = Events.get_or_none(Events.id == event_id)

    message = "@" + user.name + " has invited you to take part in a recycling event : " + event.title + ".<br> <br>"
    message = message + '<strong>Note:</strong> This invitation was intended for <strong><a href="mailto:{}" target="_blank">{}</a></strong>.<br>'.format(email_to, email_to)
    message = message + '<strong>Event Page:</strong> <strong><a href="http://localhost:8080/#/event/' + str(event_id) + '" style="color:#4183c4;text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://github.com/settings/blocked_users?block_user%3DAngCosmin&amp;source=gmail&amp;ust=1554664209321000&amp;usg=AFQjCNFhcEiyGnWd5Kt311X8KnYc0aRuqg">Click here</a>'
    email_body = """\
<p class="m_-1403629251686063965email-body-subtext" style="color:#333;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:13px;font-weight:normal;line-height:20px;margin:15px 0 5px;padding:0;text-align:left;word-wrap:normal" align="left">
{}
</p>""".format(message)
    msg = MIMEText(email_body, 'html')
    msg['Subject'] = 'Event Invitation'
    send_mail_helper(email_to, msg.as_string())
    return jsonify({'success': True, 'message': 'Success'}), 200


def send_mail_helper(email_to, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('app.bestem@gmail.com', 'parolaapp')

    server.sendmail('app.bestem@gmail.com', email_to, message)
    server.quit()


@blueprint.route('/pending_users', methods=['GET'])
@jwt_required
def pending_users():
    current_user_id = get_jwt_identity()
    users = Users.select().where(Users.status == 0)
    board = []

    for user in users:
        if user.id != current_user_id:
            board.append({
                'id': user.id,
                'name': user.name,
                'avatar': user.avatar,
            })

    return jsonify({'success': True, 'message': board}), 200


@blueprint.route('/pending_pins', methods=['GET'])
@jwt_required
def pending_pins():
    pins = Pins.select().where(Pins.status == 1)
    result = []
    for pin in pins:
        dict = {
            'id': pin.id,
            'title': pin.title,
            'description': pin.description,
            'pictures': []
        }

        pictures = Pictures.select().where(Pictures.pin == pin.id)
        for picture in pictures:
            dict['pictures'].append(picture.url)
        result.append(dict)

    return jsonify({'success': True, 'message': result}), 200


@blueprint.route('/approve_user_profile', methods=['POST'])
def approve_user_profile():
    user_id = request.form['user_id']
    query = Users.update(status=1).where(Users.id == user_id)
    query.execute()

    return jsonify({'success': True, 'message': 'Successfully updated!'}), 200


@blueprint.route('/approve_pin_cleaned', methods=['POST'])
def approve_pin_cleaned():
    pin_id = request.form['pin_id']
    query = Pins.update(status=1, cleaned_at=datetime.now).where(Pins.id == pin_id)
    query.execute()

    user = Users.get_or_none(Users.id == Pins.get(Pins.id == pin_id).user)
    query = Users.update(points=user.points + 20, places_cleaned=(user.places_cleaned+1))
    query.execute()

    assign_badge_clean(user.id)

    return jsonify({'success': True, 'message': 'Successfully approved!'}), 200

