from back.models import db_postgres as db
from back import mongo, grid_fs_seniors
from flask import jsonify

class Seniors(db.Model):
    senior_id = db.Column(db.Integer, primary_key=True)
    senior_fullname = db.Column(db.String(100), nullable=False)
    senior_username = db.Column(db.String(100), nullable=False)
    senior_password = db.Column(db.String(100), nullable=False)
    senior_skills = db.Column(db.String(250), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('Categories.category_id'), nullable=False)
    senior_birthday = db.Column(db.Date, nullable=False)