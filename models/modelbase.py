from google.appengine.ext import ndb

class ModelBase(ndb.Model):
    def to_dict(self):
        result = super(ModelBase, self).to_dict()
        result['key'] = self.key.id()  # get the key as a string
        return result

