from flask import Blueprint

from app.models.users import Users

blueprint = Blueprint('home', __name__)


@blueprint.route('/')
def index():
    user = Users.get(Users.id == 3)
    return user.email


