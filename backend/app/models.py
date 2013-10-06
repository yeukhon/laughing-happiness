import datetime
from flask import url_for
from app import db


class User(db.Document):
    email = db.EmailField(required=True)

class Job(db.Document):
    user_id = db.ReferenceField(User, required=True)
    job_service = db.StringField(required=True)
    job_action = db.StringField(required=True)
    data = db.DictField()

