from email.mime.text import MIMEText

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.events import Events
from app.models.users import Users
import smtplib

blueprint = Blueprint('utils', __name__, url_prefix='/utils')


def verify_if_user_should_receive_a_badge(user_id):
    return


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
    message = message + '<strong>Note:</strong> This invitation was intended for <strong><a href="mailto:{}" target="_blank">catrina.mihaela20@gmail.com</a></strong>.<br>'.format(email_to)
    message = message + '<strong>Event Page:</strong> <strong><a href="https://google.com" style="color:#4183c4;text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://github.com/settings/blocked_users?block_user%3DAngCosmin&amp;source=gmail&amp;ust=1554664209321000&amp;usg=AFQjCNFhcEiyGnWd5Kt311X8KnYc0aRuqg">Click here</a>'
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