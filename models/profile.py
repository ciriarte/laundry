from google.appengine.ext import db

class Profile(db.Model):
	user = db.UserProperty()
	role = db.CategoryProperty()