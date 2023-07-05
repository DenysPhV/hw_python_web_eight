from mongoengine import Document, CASCADE
from mongoengine.fields import ReferenceField, DateTimeField, ListField, StringField

from connect import connect
connect(db='hw_eight_db')


class Authors(Document):
    fullname = StringField()
    born_date = DateTimeField()
    born_location = StringField()
    description = StringField()


class Quotes(Document):
    tags = ListField(StringField())
    author = ReferenceField(Authors, reverse_delete_rule=CASCADE)
    quote = StringField()
