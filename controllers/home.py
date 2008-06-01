import os
import cgi
import wsgiref.handlers

from google.appengine.api        import users
from google.appengine.ext        import webapp
from google.appengine.ext.webapp import template

from models.profile              import Profile

class Index(webapp.RequestHandler):
  def get(self):
	  path = os.path.join(os.path.dirname(__file__),
	                      '../views/home/index.html')
	  self.response.out.write(template.render(path, None))

class Login(webapp.RequestHandler):
	def get(self):
		user = users.get_current_user()
		if user:
		  profile = Profile.gql("WHERE user = :1", user).get()
		  if not profile:
		    self.redirect("/profiles/new")
		    return
		  self.redirect("/dashboard")
		else:
		  self.redirect(users.create_login_url(self.request.uri))

def main():
  application = webapp.WSGIApplication(
			                           [('/',                  Index),
			                           ('/services',           Index),
			                           ('/contact',            Index),
			                           ('/login',              Login)],
									   debug=True)
  wsgiref.handlers.CGIHandler().run(application)			
if __name__ == "__main__":
  main()