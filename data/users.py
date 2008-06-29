from google.appengine.ext import bulkload
from google.appengine.api import datastore_types

class ProfileLoader(bulkload.Loader):
  def __init__(self):
    # Loads management profiles
    bulkload.Loader.__init__(self, 'Profile',
                             [('first_Name', str),
                              ('last_Name', str),
                              ('role', str),
                              ('country', str),
                              ('state', str),
                              ('city', str),
                              ('zip_Code', str),
                              ('phone', str),
                              ('email', datastore_types.Email),
                             ])

if __name__ == '__main__':
  bulkload.main(ProfileLoader())