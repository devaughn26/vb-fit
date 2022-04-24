from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(80),nullable=False,unique=True)
	email = db.Column(db.String(120),nullable=False,unique=True)
	password = db.Column(db.String(120),nullable=False,unique=True)
	
	def toDict(self):
		return{
		"id":self.id,
		"username":self.username,
		"email":self.email,
		"password":self.password
		}

	def set_password(self,password):
		self.password = generate_password_hash(password, method='sha256')

	def check_password(self,password):
		return check_password_hash(self.password,password)

