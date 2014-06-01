from google.appengine.ext.webapp import template
from google.appengine.ext import ndb
from google.appengine.api import users
from datetime import datetime, date, time

import logging
import os.path
import webapp2
import jinja2
import json

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/../views/"),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def get_user(self):
        return users.get_current_user()

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        #if(self.get_user()):
        #    params['user'] = self.get_user()

        logging.info("=========" + view_filename)
        tmpl = JINJA_ENVIRONMENT.get_template(view_filename)
        self.response.write(tmpl.render(params))

    def display_message(self, message):
        """Utility function to display a template with a simple message."""
        params = {
            'message': message
        }
        self.render_template('message.html', params)

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        # If this is a key, you might want to grab the actual model.
        if isinstance(o, ndb.Key):
            return o.id
        if isinstance(o, ndb.Model):
            return ndb.to_dict(o)
        elif isinstance(o, (datetime, date, time)):
            return str(o.isoformat())  # Or whatever other date format you're OK with...

class BaseApiHandler(webapp2.RequestHandler):
    def return_json(self, obj):
        self.response.write(JSONEncoder().encode(obj))

