'''
    signup_endpoints module
    [] new user signup
    [] email availability check
'''

import flask
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
log_formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('server/logs/signup_endpoints.log')
file_handler.setFormatter(log_formatter)
logger.addHandler(file_handler)

endpoints = flask.Blueprint('signup', __name__)

@endpoints.route("/api/v0/signup", methods=['POST'])
def signup():
    pass
