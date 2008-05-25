from google.appengine.ext import db

from .product import Product

class Order(db.Model):
	client      = db.UserProperty()
	status      = db.CategoryProperty()
	createdOn   = db.DateTimeProperty(auto_now_add=True)
