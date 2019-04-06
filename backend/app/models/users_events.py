from peewee import ForeignKeyField, IntegerField

from app.models.base import BaseModel
from app.models.events import Events
from app.models.users import Users


class Users_Events(BaseModel):
    user = ForeignKeyField(Users, backref='Users_Events')
    event = ForeignKeyField(Events, backref='Users_Events')
    invited_by_id = IntegerField()
    status = IntegerField()
