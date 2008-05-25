from google.appengine.ext import db

class Profile(db.Model):
	user = UserProperty()
	role = db.Category()