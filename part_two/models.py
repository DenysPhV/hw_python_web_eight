from mongoengine import Document
from mongoengine.fields import DateTimeField, StringField, BooleanField
from connect import connect


class Contacts(Document):
    fullname = StringField()
    born_date = DateTimeField()
    email = StringField()
    send = BooleanField(default=False)

