import cgi, urllib, webapp2

from google.appengine.ext import ndb
from models import modelbase

# Add a baseModel
class Receipt(modelbase.ModelBase):
    """ Represents one receipt"""
    total = ndb.IntegerProperty()
    tax = ndb.IntegerProperty()
    merchant = ndb.StringProperty()
    date = ndb.DateTimeProperty()
    category = ndb.StringProperty()
    note = ndb.StringProperty()
    scankey = ndb.StringProperty()

    @classmethod
    def get_all(cls):
        return cls.query().fetch()
