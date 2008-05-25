from google.appengine.ext import db

class Product(db.Model):
	id			= db.IntegerProperty()
	description = db.StringProperty(multiline=False)
	price		= db.FloatProperty()