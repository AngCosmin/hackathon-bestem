from peewee import CharField, ForeignKeyField

from app.models.base import BaseModel
from app.models.pins import Pins


class Pictures(BaseModel):
    url = CharField()
    pin = ForeignKeyField(Pins, backref='Pictures')
