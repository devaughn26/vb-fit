from App.database import db

class Workout(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(80),nullable=True)
	author = db.Column(db.String(80),nullable=True)
	E1 = db.Column(db.Integer,nullable=True)
	E2 = db.Column(db.Integer,nullable=True)
	E3 = db.Column(db.Integer,nullable=True)
	E4 = db.Column(db.Integer,nullable=True)
	E5 = db.Column(db.Integer,nullable=True)
	R1 = db.Column(db.Integer,nullable=True)
	R2 = db.Column(db.Integer,nullable=True)
	R3 = db.Column(db.Integer,nullable=True)
	R4 = db.Column(db.Integer,nullable=True)
	R5 = db.Column(db.Integer,nullable=True)
	S1 = db.Column(db.Integer,nullable=True)
	S2 = db.Column(db.Integer,nullable=True)
	S3 = db.Column(db.Integer,nullable=True)
	S4 = db.Column(db.Integer,nullable=True)
	S5 = db.Column(db.Integer,nullable=True)

	def toDict(self):
		return{
		"id":self.id,
		"content":self.content,
		}