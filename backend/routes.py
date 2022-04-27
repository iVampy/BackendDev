"""Application routes."""
from flask import current_app as app, jsonify, request, send_from_directory, make_response
from flask_login import login_user, login_required, logout_user, current_user
from flask_cors import cross_origin
from .models import User, UserSchema, Subjects, Biodata, Applications


# instantiate schema objects for todolist and todolists
user_schema = UserSchema(many=False)
users_schema = UserSchema(many=True)

# error handeling
@app.errorhandler(400)
def handle_400_error(_error):
    """Return a http 400 error to client"""
    return make_response(jsonify({'error': 'Misunderstood, Bad Request response'}), 400)

@app.errorhandler(401)
def handle_401_error(_error):
    """Return a http 401 error to client"""
    return make_response(jsonify({'error': 'Unauthorised'}), 401)

@app.errorhandler(404)
def handle_404_error(_error):
    """Return a http 404 error to client"""
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    return make_response(jsonify({'error': 'Server error'}), 500)

# just testing
@app.route('/api', methods=["GET"])
@cross_origin()
def index():
    return {
        "test": "Roaa"
    }

# just testing
@app.route('/test', methods=["GET"])
@cross_origin()
#@login_required
def indextest():
    print(current_user.email)
    print(current_user.id)
    return {
        "test": current_user.email
    }

@app.route("/signup", methods=["POST"])
@cross_origin()
def signup():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    phone = request.json['phone']
    email = request.json['email']
    passwd = request.json['passwd']
        
    user_exists = User.query.filter_by(email=email).first()
    if user_exists is None:
        
        new_user = User(first_name, last_name, phone, email)
        new_user.set_password(passwd)
        new_user.save() # Create new user

        return {"success": True,
            "userID": new_user.id,
            "msg": "The user was successfully registered"}, 200 
    else:
        return {"success": False,
                "msg": "Email already taken"}, 400

@app.route("/login", methods=['POST'])
@cross_origin()
def login():
    email = request.json['email']
    passwd = request.json['passwd']
    user_exists = User.query.filter_by(email=email).first()

    if user_exists is None:
        return {"success": False,
                "msg": "This email does not exist."}, 400
    elif not user_exists.check_password(password=passwd):
        return {"success": False,
                "msg": "Wrong credentials."}, 400
    else:
        login_user(user_exists)
        return {"success": True,
            #"token": token,
            "msg": "Login successfully"}, 200

@app.route('/logout')
@cross_origin()
@login_required
def logout():
    logout_user()
    return {"success": True,
                #"token": token,
                "msg": "Logout successfully"}, 200

@app.route("/register", methods=["POST"])
@cross_origin()
def register():
    subjects = ["Mathematics", "Algebra", "Geometry", "Science", "Biology", "Physics", "Chemistry", "Geography", "History", "Home Economics", "Art", "Business Studies", "Home Economics"]
    # get form data
    grade_choice = request.json['grade_choice']
    year_choice = request.json['year_choice']
    subjects = request.json['subjects']
    paid_status = 1
    user_id = current_user.id


    # Insert subjects
    insert_subjects = Subjects(subjects[0], subjects[1], subjects[2], subjects[3], subjects[4], subjects[5], subjects[6], subjects[7], subjects[8])
    insert_subjects.save() # Create new subject

    # init biodata
    insert_biodata = Biodata()
    insert_biodata.save() # Create new biodata

    # Insert application
    insert_application = Applications(grade_choice, year_choice, paid_status, user_id, insert_subjects.id, insert_biodata.id)
    insert_application.save() # Create new application

    return {"success": True,
                "appID": insert_application.id,
                "msg": "The application are successfully registered"}, 200

    # Send acknowledgment email to the user with PDF containing payment and courser details