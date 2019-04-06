import datetime
from peewee import CharField, ForeignKeyField, DateTimeField, TextField
from app.models.base import BaseModel
from app.models.pins import Pins


class Events(BaseModel):
    pin = ForeignKeyField(Pins, backref='Events')
    title = CharField()
    description = TextField()
    time_start = DateTimeField(default=datetime.datetime.now)
    time_end = DateTimeField(default=datetime.datetime.now)
