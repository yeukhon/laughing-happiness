import datetime
from flask import url_for
from app import db


class User(db.Document):
    email = db.EmailField(required=True)
