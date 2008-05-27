import os
import cgi
import wsgiref.handlers

from google.appengine.api        import users
from google.appengine.ext        import webapp
from google.appengine.ext        import db

def requires(role):
  """Simple decorator for role based access"""
  def request_wrapper(handler_method):
    def verify_access(self, *args):
      user = users.GetCurrentUser()
      if user:
        profile = Profile.gql("WHERE user = :1", user)
        current_profile = profile.get()
        if role == current_profile.role:
          handler_method(self, *args)
          return
      self.response.out.write('<html><head></head><body>Access denied</body></html>')
    return verify_access
  return request_wrapper