import webapp2


from controllers import api_controller
from controllers import home_controller
from controllers import receipt_controller

app = webapp2.WSGIApplication([
    ('/', home_controller.Home),
    ('/add', receipt_controller.Add),
    ('/scan/([^/]+)?', receipt_controller.Scan),
    ('/upload', receipt_controller.Add),
    ('/view', receipt_controller.View),  # add the id route here
    ('/api/all', api_controller.ApiAll),  # remove api search thing.
], debug=True)
