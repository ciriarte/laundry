import os
import cgi
import wsgiref.handlers

from google.appengine.api        import users
from google.appengine.ext        import webapp
from google.appengine.ext.webapp import template

class Index(webapp.RequestHandler):
  def get(self):	
	path = os.path.join(os.path.dirname(__file__),
	                    '../views/admin/index.html')
	
	template_values = {
		'name': self.__class__.__name__,
		'profiles': Profile.all(),
	}
	
	self.response.out.write(template.render(path, template_values))