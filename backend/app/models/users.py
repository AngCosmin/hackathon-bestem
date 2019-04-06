from peewee import CharField, ForeignKeyField

from app.models.base import BaseModel
from app.models.roles import Roles


class Users(BaseModel):
    email = CharField()
    password = CharField()
    role = ForeignKeyField(Roles, backref='Role')
    name = CharField()
