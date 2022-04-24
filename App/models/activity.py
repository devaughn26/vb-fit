from App.database import db

class Activity(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(80),nullable=True)
	type = db.Column(db.String(80),nullable=True)
	topic = db.Column(db.String(80),nullable = True)