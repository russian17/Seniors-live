from back.models import db_postgres as db
from flask import jsonify

class Meetings(db.Model):
    meeting_id = db.Column(db.Integer, primary_key=True)
    senior_id = db.Column(db.Integer, db.ForeignKey('Seniors.senior_id'), nullable=False)