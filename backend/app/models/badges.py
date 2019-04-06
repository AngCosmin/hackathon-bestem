from peewee import CharField, ForeignKeyField

from app.models.base import BaseModel


class Badges(BaseModel):
    name = CharField()
    description = CharField()
    icon = CharField()
