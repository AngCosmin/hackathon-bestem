from peewee import CharField

from app.models.base import BaseModel


class Roles(BaseModel):
    name = CharField()
