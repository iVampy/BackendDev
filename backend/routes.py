"""Application routes."""
from flask import current_app as app, jsonify, request, send_from_directory
from flask_cors import cross_origin
from .models import User, db

@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api', methods=["GET"])
@cross_origin()
def index():
    return {
        "tutorial": "Flask React Heroku"
    }

@app.route("/signup", methods=["POST"])
@cross_origin()
def signup():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    phone = request.json['phone']
    email = request.json['email']
    passwd = request.json['passwd']

    existing_user = User.query.filter_by(email=email).first()
    if existing_user is None:
        user = User(first_name, last_name, phone, email)
        user.set_password(passwd)
        db.session.add(user) # Create new user
        db.session.commit()
        return 'OK'
    else:
        return 'A user already exists with that email address.'

@app.route("/login", methods=['POST'])
@cross_origin()
def login():
    email = request.json['email']
    passwd = request.json['passwd']

    user = User.query.filter_by(email=email).first()
    if user is None:
        return 'Invalid email'
    elif not user.check_password(password=passwd):
        return 'Invalid password'
    else:
        return 'Log in'


@app.route("/register", methods=["POST"])
@cross_origin()
def register():
    subjects = ["Mathematics", "Algebra", "Geometry", "Science", "Biology", "Physics", "Chemistry", "Geography", "History", "Home Economics", "Art", "Business Studies", "Home Economics"]
    # get form data
    grade_choice = request.json['grade_choice']
    year_choice = request.json['year_choice']
    subjects = request.json['subjects']

    # Insert subjects

    # Insert application

    # Send acknowledgment email to the user with PDF containing payment and courser details