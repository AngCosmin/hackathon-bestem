from email.mime.text import MIMEText

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.events import Events
from app.models.users import Users
import smtplib

blueprint = Blueprint('utils', __name__, url_prefix='/utils')


@blueprint.route('/get_emails', methods=['GET'])
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
    email_from = user.email
    email_to = request.form['email_to']

    event_id = request.form['event_id']
    event = Events.get_or_none(Events.id == event_id)

    message = "@" + user.name + " has invited you to take part in a recycling event : " + event.title + ".\n"
    message = message + "You can accept or decline this invitation.\n"
    message = message + 'Event link: <a href= "{}" >click here</a>'.format("https://google.com")
    email_body = """<pre>
        {}
    </pre>""".format(message)

    msg = MIMEText(email_body, 'html')
    send_mail_helper(email_to, email_from, msg.as_string())
    return jsonify({'success': True, 'message': 'Success'}), 200


def send_mail_helper(email_to, email_from, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('app.bestem@gmail.com', 'parolaapp')

    server.sendmail('app.bestem@gmail.com', email_to, message)
    server.quit()