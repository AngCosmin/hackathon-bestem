import datetime
from peewee import CharField, ForeignKeyField, BooleanField, DoubleField, DateTimeField, TextField, IntegerField
from app.models.base import BaseModel
from app.models.users import Users


class Pins(BaseModel):
    user = ForeignKeyField(Users, backref='Pins')
    lat = DoubleField()
    lng = DoubleField()
    cleaned = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)
    description = TextField()
    title = CharField()
    type = IntegerField()
