from django.db import models

from mongoengine import *
from bson.objectid import ObjectId

class Presentation(Document):
    _id = ObjectIdField(required=True, default=ObjectId, primary_key=True)
    id = StringField(required=True)
    title = StringField(required=True)
    thumbnail = StringField(required=True)
    creator = DictField(required=True)
    createdAt = StringField(required=True)
