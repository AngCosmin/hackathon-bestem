from peewee import ForeignKeyField

from app.models.base import BaseModel
from app.models.users import Users


class Users_Friends(BaseModel):
    user = ForeignKeyField(Users, backref='Users_Friends')
    friend = ForeignKeyField(Users, backref='Users_Friends')

