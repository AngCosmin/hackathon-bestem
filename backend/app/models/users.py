from peewee import CharField, ForeignKeyField, TextField, IntegerField

from app.models.base import BaseModel
from app.models.roles import Roles


class Users(BaseModel):
    email = CharField()
    password = CharField()
    role = ForeignKeyField(Roles, backref='Role')
    name = CharField()
    phone = CharField()
    info = TextField()
    avatar = CharField()
    points = IntegerField(default=0)
    places_reported = IntegerField(default=0)
    places_cleaned = IntegerField(default=0)
