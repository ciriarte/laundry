from google.appengine.ext import bulkload
from google.appengine.api import datastore_types
from google.appengine.ext import db
from google.appengine.api import users
import datetime

class OrderLoader(bulkload.Loader):
  def __init__(self):
    # Loads orders
    bulkload.Loader.__init__(self, 'Order',
			     [('client', str),
			      ('status', str),
			      ('createdOn', lambda x: datetime.datetime.strptime(x, "%d/%m/%Y %H:%M")),
			     ])

if __name__ == '__main__':
  bulkload.main(OrderLoader())
