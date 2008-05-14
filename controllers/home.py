import cgi
import wsgiref.handlers
import os

from google.appengine.ext        import db
from google.appengine.api        import users
from google.appengine.ext        import webapp
from google.appengine.ext.webapp import template

class HomeController(webapp.RequestHandler):
  def get(self):
	path = os.path.join(os.path.dirname(__file__), '../views/home.html')
	
	template_values = {
		
	}
	
	self.response.out.write(template.render(path, template_values))

def main():
  application = webapp.WSGIApplication(
                                       [('/', HomeController)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
  main()
