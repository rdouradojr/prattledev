from google.appengine.ext import ndb

class DataName(ndb.Model):
  field1 = ndb.StringProperty(required=True)
  field2 = ndb.IntegerProperty(required=True)
