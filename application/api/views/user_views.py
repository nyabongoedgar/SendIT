""" This module defines user routes """
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, jsonify, request 
import datetime, re
from application.api.models.user import User
from application import app


from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

user_object = User()

app.config['JWT_SECRET_KEY'] = '\x01\n=:\x87\xe1\x02\xca\x81\x8b\x0c\xe4Y=\x87\xb7\xa8\x89.<\x95\x90\xbb\x06'

jwt = JWTManager(app)

user_blueprint  = Blueprint('User',__name__, url_prefix='/api/v2/')

@user_blueprint.route('/auth/signup', methods = ['POST']) 
def register_user():
    """ This function registers a user by using his username,password and email """
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = data.get('password') 
    user = user_object.user(username)
    if not password or password.isspace():
        return jsonify({'message': 'Password field can not be left empty.'}), 400
    if not username or username.isspace():
        return jsonify({'message': 'Username field can not be empty.'}), 400
    if not email or email.isspace():
        return jsonify({'message': 'Email field can not be empty.'}), 400
    elif not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", email):
        return jsonify({'message': 'Enter a valid email address.'}), 400  
    if user is not None:
        return jsonify({'message':'Username already exists'}),400 
    hashed_password = generate_password_hash(password, method='sha256')
    user_object.register_user(username,email,hashed_password)
    return jsonify({'message':'User registered successfully'}),201

@user_blueprint.route("/auth/login", methods=['POST'])
def login():
    """ This function signs in  user by using his username and password """ 
    data = request.get_json() 
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message':'No data has been sent'}),400
    user = user_object.user(data.get('username'))
    if not user:
        return jsonify({'message':'Verification of credentials failed !'}),401
    if check_password_hash(user['password'],data['password']):
        token = create_access_token(identity=user['user_id'])
        return jsonify({'token':token}), 200        
    return jsonify({'message':'password does not match !'}),401

@user_blueprint.route('/promote/<username>',methods=['PUT'])
def promote_user(username):
    """ This function promotes a user to admin """
    user = user_object.user(username)
    if user is None:
        return jsonify({'message':'user promotion failed'}),400
    result_set =user_object.promoter(username)
    if result_set is not None:
        return jsonify({'message':username + ' promoted to admin'}),200