from peewee import ForeignKeyField

from app.models.badges import Badges
from app.models.base import BaseModel
from app.models.users import Users


class Users_Badges(BaseModel):
    user = ForeignKeyField(Users, backref='User_Badges')
    badge = ForeignKeyField(Badges, backref='User_Badges')

