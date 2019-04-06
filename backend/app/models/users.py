from peewee import CharField

from app.models.base import BaseModel


class Users(BaseModel):
    email = CharField()
    password = CharField()
