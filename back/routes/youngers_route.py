from flask import Blueprint, jsonify, request
from datetime import datetime
import bcrypt
from back.models import db_postgres as db
from back.models.youngers import Youngers
from back import app, grid_fs_youngers

# Create a Blueprint for the routes associated with younger users
youngers_routes = Blueprint("youngers_routes", __name__)

@youngers_routes.route('/younger_register', methods=['POST'])
def register():
    if request.method == 'POST':
        # Extracting form fields from the request
        younger_username = request.form.get('younger_username')
        younger_password = request.form.get('younger_password')
        younger_fullname = request.form.get('younger_fullname')
        younger_birthday = request.form.get('younger_birthday')

        existing_younger = Youngers.query.filter_by(younger_username=younger_username).first()

        if existing_younger:
            return jsonify({'message': 'Username already exists'}), 400

        # Hashing the password
        pwhash = bcrypt.hashpw(younger_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        new_younger = Youngers(
            younger_fullname=younger_fullname,
            younger_username=younger_username,
            younger_password=pwhash,
            younger_birthday=datetime.strptime(younger_birthday, '%Y-%m-%d').date()
        )

        db.session.add(new_younger)
        db.session.commit()

        return jsonify({'message': 'Younger registered successfully'}), 201

    return jsonify({'message': 'This is the younger registration page'}), 200

@youngers_routes.route('/younger_login', methods=['POST'])
def login():
    if request.method == 'POST':
        younger_username = request.form.get('younger_username')
        younger_password = request.form.get('younger_password')

        existing_younger = Youngers.query.filter_by(younger_username=younger_username).first()
        if not existing_younger:
            return jsonify({'message': 'User does not exist'}), 400

        if bcrypt.checkpw(younger_password.encode('utf-8'), existing_younger.younger_password.encode('utf-8')):
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'message': 'Password is incorrect'}), 400

    return jsonify({'message': 'This is the login page for younger users'}), 200

# Don't forget to register this Blueprint in your Flask app's setup
