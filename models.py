from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.Text())
    year = db.Column(db.Text())
    student = db.Column(db.Text())
    supervisor = db.Column(db.Text())
    matric_no = db.Column(db.Text())
    submitted = db.Column(db.Text())