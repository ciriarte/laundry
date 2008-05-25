import os
import cgi
import wsgiref.handlers

from google.appengine.api        import users
from google.appengine.ext        import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext        import db

from models.order   import Order
from models.product import Product

class Index(webapp.RequestHandler):
  def get(self):	
	path = os.path.join(os.path.dirname(__file__),
	                    '../views/orders/index.html')
	
	template_values = {
		'name': self.__class__.__name__,
		'orders': Order.all().order('-createdOn'),		
	}
	
	self.response.out.write(template.render(path, template_values))

class Edit(webapp.RequestHandler):
  def get(self, id):	
	path = os.path.join(os.path.dirname(__file__),
	                    '../views/orders/edit.html')
	
	template_values = {
		'name': self.__class__.__name__,
		'order': Order.get_by_id(int(id))
	}
	
	self.response.out.write(template.render(path, template_values))
		
def main():
  application = webapp.WSGIApplication(
		                               [
									   ('/dashboard',      			    Index),
									   ('/dashboard/orders/new', 	    Edit),
									   ('/dashboard/orders/edit/(\d+)', Edit)],
		                                 debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
  main()		