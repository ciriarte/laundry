import os
import cgi
import wsgiref.handlers

from google.appengine.api        import users
from google.appengine.ext        import webapp
from google.appengine.ext.webapp import template

from django import newforms as forms

class ProfileForm(forms.Form):
    first_Name = forms.CharField(max_length=100)
    last_Name  = forms.CharField()
    country    = forms.CharField()
    state      = forms.CharField()
    city       = forms.CharField()
    street     = forms.CharField()
    zip        = forms.RegexField('^[0-9]{5}$')
    phone      = forms.RegexField('(^\d{5}$)|(^\d{5}-\d{4}$)')
    email      = forms.EmailField()

class Index(webapp.RequestHandler):    
  def get(self):	
	path = os.path.join(os.path.dirname(__file__),
	                    '../views/profile/index.html')
	
	profileForm = ProfileForm()
	self.response.out.write(template.render(path, {'form': profileForm})) 	

def main():
  application = webapp.WSGIApplication([('/profile/new', Index)], debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
  main()