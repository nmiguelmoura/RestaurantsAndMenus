from flask import request
from flask import session as login_session
import random
import string


class CSRF_state_generator():
    '''Class that generates and validates random code to prevent Cross-Site
    Request Forgery (CSRF).'''

    def __init__(self):
        pass

    def generate(self):
        # Generate random code
        return ''.join(
            random.choice(string.ascii_uppercase + string.digits) for x in
            xrange(32))

    def validate(self):
        # Check if code in form matches session code.

        # Get code in form.
        csrf_form = request.form['CSRF']
        if csrf_form == login_session.get('CSRF'):
            # If comparison between form code and session code, return True
            # if both are equal.
            return True

        return False
