from google.appengine.ext import bulkload
from google.appengine.api import datastore_types

class ProductLoader(bulkload.Loader):
  def __init__(self):
    # Loads products
    bulkload.Loader.__init__(self, 'Product',
                             [('description', str),
                              ('price', float),
                             ])

if __name__ == '__main__':
  bulkload.main(ProductLoader())