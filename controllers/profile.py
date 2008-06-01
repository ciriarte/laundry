import os
import cgi
import wsgiref.handlers

from google.appengine.api        import users
from google.appengine.ext        import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.db     import djangoforms

from django                      import newforms as forms

from models.profile              import Profile

class ProfileForm(djangoforms.ModelForm):
  class Meta:
    model = Profile 
    exclude = ['user',
               'role']

class Index(webapp.RequestHandler):
 def get(self):	
	path = os.path.join(os.path.dirname(__file__),
	                    '../views/profiles/index.html')

	template_values = {
		'name': self.__class__.__name__,
		'profiles': Profile.all().order('-last_Name'),
	}

	self.response.out.write(template.render(path, template_values)) 

class New(webapp.RequestHandler):    
  def get(self):	
	  path = os.path.join(os.path.dirname(__file__),
	                      '../views/profiles/new.html')	
	  profileForm = ProfileForm()
	  self.response.out.write(template.render(path, {'form': profileForm})) 	
    
  def post(self):
	  profileForm = ProfileForm(data=self.request.POST)
	  if profileForm.is_valid():
	    entity = profileForm.save(commit=False) 
	    entity.put() 
	    self.redirect('/profiles')
	  else:
	    self.response.out.write(template.render(path, {'form': profileForm}))
	    
def main():
  application = webapp.WSGIApplication([('/profiles',     Index),
                                        ('/profiles/new', New)],
                                        debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
  main()