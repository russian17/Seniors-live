from flask import Blueprint, jsonify, request
from datetime import datetime
import bcrypt
from back.models import db_postgres as db
from back.models.seniors import Seniors
from back import app, grid_fs_seniors

# Create a Blueprint for the senior-related routes
seniors_routes = Blueprint("seniors_routes", __name__)

@seniors_routes.route('/senior_register', methods=['POST'])
def register():
    if request.method == 'POST':
        # Extract form fields from the request parameters
        senior_username = request.form.get('senior_username')
        senior_password = request.form.get('senior_password')
        senior_fullname = request.form.get('senior_fullname')
        senior_skills = request.form.get('senior_skills')
        category_id = request.form.get('category_id')
        senior_birthday = request.form.get('senior_birthday')

        existing_senior = Seniors.query.filter_by(senior_username=senior_username).first()

        if existing_senior:
            return jsonify({'message': 'Senior username already exists'}), 400

        # Hashing the password
        pwhash = bcrypt.hashpw(senior_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        new_senior = Seniors(
            senior_fullname=senior_fullname,
            senior_username=senior_username,
            senior_password=pwhash,
            senior_skills=senior_skills,
            category_id=category_id,
            senior_birthday=datetime.strptime(senior_birthday, '%Y-%m-%d').date()
        )

        db.session.add(new_senior)
        db.session.commit()

        return jsonify({'message': 'Senior registered successfully'}), 201

    return jsonify({'message': 'This is the senior registration page'}), 200


@seniors_routes.route('/senior_login', methods=['POST'])
def login():
    if request.method == 'POST':
        senior_username = request.form.get('senior_username')
        senior_password = request.form.get('senior_password')

        existing_senior = Seniors.query.filter_by(senior_username=senior_username).first()
        if not existing_senior:
            return jsonify({'message': 'Senior does not exist'}), 400

        if bcrypt.checkpw(senior_password.encode('utf-8'), existing_senior.senior_password.encode('utf-8')):
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'message': 'Password is incorrect'}), 400

    return jsonify({'message': 'This is the senior login page'}), 200

