from flask import request
from flask import session as login_session
import random
import string

class CSRF_state_generator():
    def __init__(self):
        pass

    def generate(self):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))

    def validate(self):
        csrf_form = request.form['CSRF']
        if csrf_form == login_session.get('CSRF'):
            return True

        return False
