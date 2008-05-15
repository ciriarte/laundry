import cgi
import wsgiref.handlers
import os

from google.appengine.ext        import db
from google.appengine.api        import users
from google.appengine.ext        import webapp
from google.appengine.ext.webapp import template

class HomeController(webapp.RequestHandler):
  def get(self):
	path = os.path.join(os.path.dirname(__file__),
	                    '../views/%s.html' % ("home"
	                    if self.request.path == "/" else self.request.path[1:]))
	
	template_values = {
      'section': self.request.path[1:],
    }
	
	self.response.out.write(template.render(path, template_values))

class LoginController(webapp.RequestHandler):
	def get(self):
	    user = users.get_current_user()
	    if user:
	      self.redirect(user.nickname() + "/dashboard")
	    else:
	      self.redirect(users.create_login_url(self.request.uri))

def main():
  application = webapp.WSGIApplication(
                                       [('/',         HomeController),
                                        ('/home',     HomeController),
										('/services', HomeController),
										('/contact',  HomeController),
										('/login',    LoginController)],
                                       debug=False)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
  main()
