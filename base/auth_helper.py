from google.appengine.api import users

def user_required(handler):
    def check_login(self, *args, **kwargs):
        if not users.get_current_user():
            self.redirect(users.create_login_url(self.request.uri))
        else:
            return handler(self, *args, **kwargs)
    return check_login

