import logging

from google.appengine.api import users
from google.appengine.ext import ndb

from base import base_handlers
from base import auth_helper
from models import receipt


class Home(base_handlers.BaseHandler):
    @auth_helper.user_required
    def get(self):
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'url': url,
            'url_linktext': url_linktext,
            'greetings': receipt.Receipt.get_all(),
        }
        # logging.info(receipt.Receipt.get_all())
        self.render_template("home.html", template_values)
