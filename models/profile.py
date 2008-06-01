from google.appengine.ext import db

class Profile(db.Model):
	user       = db.UserProperty()
	role       = db.CategoryProperty()
	first_Name = db.StringProperty()
	last_Name  = db.StringProperty()
	country    = db.StringProperty()
	state      = db.StringProperty()
	city       = db.StringProperty()
	zip_Code   = db.StringProperty()
	phone      = db.StringProperty()
	email      = db.EmailProperty()