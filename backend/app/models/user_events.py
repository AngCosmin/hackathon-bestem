import datetime
from peewee import ForeignKeyField
from app.models.base import BaseModel
from app.models.events import Events
from app.models.users import Users


class User_Events(BaseModel):
    user = ForeignKeyField(Users, backref='User_Events')
    event = ForeignKeyField(Events, backref='User_Events')
