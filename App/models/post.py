from App.database import db


class Post(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	content = db.Column(db.Text,nullable=True)
	topic = db.Column(db.String(80),nullable=True)
	rating = db.Column(db.Integer)
	author = db.Column(db.String(80),nullable=True)
	
	def toDict(self): 
		return{
		"id":self.id,
		"content":self.content,
		}