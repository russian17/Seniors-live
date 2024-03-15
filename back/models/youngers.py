from back.models import db_postgres as db
from back import mongo, grid_fs_youngers
from flask import jsonify


class Youngers(db.Model):
    younger_id = db.Column(db.Integer, primary_key=True)
    younger_fullname = db.Column(db.String(100), nullable=False)
    younger_username = db.Column(db.String(100), nullable=False)
    younger_password = db.Column(db.String(100), nullable=False)
    younger_birthday = db.Column(db.Date, nullable=False)