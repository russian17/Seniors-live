from back.models import db_postgres as db
from flask import jsonify

class Guests(db.Model):
    guest_id = db.Column(db.Integer, primary_key=True)
    younger_id = db.Column(db.Integer, db.ForeignKey('Youngers.younger_id'), nullable=False)
    senior_id = db.Column(db.Integer, db.ForeignKey('Seniors.senior_id'), nullable=False)
    meeting_id = db.Column(db.Integer, db.ForeignKey('Meetings.meeting_id'), nullable=False)