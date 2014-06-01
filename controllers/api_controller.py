import urllib
import logging

from google.appengine.api import users
from google.appengine.ext import ndb
from webapp2_extras import json

from base import base_handlers
from models import receipt

import jinja2
import webapp2

class Image(webapp2.RequestHandler):
    """This is sorta deprecated now"""
    def get(self):
        logging.info("GID")
        logging.info(self.request.get('img_id'))
        #greeting = ndb.Key(Greeting, self.request.get('img_id')).get();
        #greeting = Greeting.get_by_id(int(self.request.get('img_id')))

        greetings_query = Greeting.query(
            ancestor=guestbook_key(DEFAULT_GUESTBOOK_NAME)).order(-Greeting.date)
        greetings = greetings_query.fetch(1)
        logging.info(greetings[0].pic)   
        if greetings[0].pic:
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(greetings[0].pic)
        else:
            self.error(404)

class ApiAdd(webapp2.RequestHandler):
    def get(self):
        pass #write some json output

class ApiAll(base_handlers.BaseApiHandler):
    def get(self):
        Rs = receipt.Receipt.get_all()
        return self.return_json([r.to_dict() for r in Rs])

