"""Database models."""
from . import db, ma
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    #__tablename__ = 'users_accounts'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    entrance_exam_date = db.Column(db.String(30))
    passwd = db.Column(db.String(800), nullable=False)
    application = db.relationship('Applications', backref='user', lazy=True)

    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def set_password(self, password):
        """Create hashed password."""
        self.passwd = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.passwd, password)

# create db schema class
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'phone', 'email')

class Subjects(db.Model):
    #__tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key = True)
    subject_1 = db.Column(db.String(80), nullable=False)
    subject_2 = db.Column(db.String(80), nullable=False)
    subject_3 = db.Column(db.String(80), nullable=False)
    subject_4 = db.Column(db.String(80), nullable=False)
    subject_5 = db.Column(db.String(80), nullable=False)
    subject_6 = db.Column(db.String(80), nullable=False)
    subject_7 = db.Column(db.String(80), nullable=False)
    subject_8 = db.Column(db.String(80), nullable=False)
    subject_9 = db.Column(db.String(80), nullable=False)
    grade_subject_1 = db.Column(db.String(10))
    grade_subject_2 = db.Column(db.String(10))
    grade_subject_3 = db.Column(db.String(10))
    grade_subject_4 = db.Column(db.String(10))
    grade_subject_5 = db.Column(db.String(10))
    grade_subject_6 = db.Column(db.String(10))
    grade_subject_7 = db.Column(db.String(10))
    grade_subject_8 = db.Column(db.String(10))
    grade_subject_9 = db.Column(db.String(10))
    application = db.relationship('Applications', backref='subjects', lazy=True)

    def __init__(self, subject_1, subject_2, subject_3, subject_4, subject_5, subject_6, subject_7, subject_8, subject_9):
        self.subject_1 = subject_1
        self.subject_2 = subject_2
        self.subject_3 = subject_3
        self.subject_4 = subject_4
        self.subject_5 = subject_5
        self.subject_6 = subject_6
        self.subject_7 = subject_7
        self.subject_8 = subject_8
        self.subject_9 = subject_9
    
    def save(self):
        db.session.add(self)
        db.session.commit()

class Biodata(db.Model):
    #__tablename__ = 'biodata'
    id = db.Column(db.Integer, primary_key = True)
    student_name = db.Column(db.String(80))
    student_gender  = db.Column(db.String(20))
    student_birth = db.Column(db.DateTime)
    student_country = db.Column(db.String(80))
    student_pic = db.Column(db.String(80))
    application = db.relationship('Applications', backref='biodata', lazy=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

class Applications(db.Model):
    #__tablename__ = 'applications'
    id = db.Column(db.Integer, primary_key = True)
    app_grade = db.Column(db.String(80), nullable=False)
    app_year = db.Column(db.String(80), nullable=False)
    paid_status = db.Column(db.Integer, default=0, nullable=False)
    app_status = db.Column(db.Integer, default=0, nullable=False)
    subjects_status = db.Column(db.Integer, default=0, nullable=False)
    biodata_status = db.Column(db.Integer, default=0, nullable=False)
    app_result = db.Column(db.String(80))
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subjects_id= db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)
    biodata_id = db.Column(db.Integer, db.ForeignKey('biodata.id'), nullable=False)

    def __init__(self, app_grade, app_year, paid_status, user_id, subjects_id, biodata_id):
        self.app_grade = app_grade
        self.app_year = app_year
        self.paid_status = paid_status
        self.user_id = user_id
        self.subjects_id = subjects_id
        self.biodata_id = biodata_id
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    