from App.database import db

class Topic(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	Title = db.Column(db.String(80),nullable=True)
	content = content = db.Column(db.Text,nullable=True)

    