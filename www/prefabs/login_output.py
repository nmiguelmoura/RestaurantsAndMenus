from flask import session as login_session

class Login_output:
    def __init__(self):
        pass

    def get_output(self):
        output = ''
        output += '<h1>Welcome, '
        output += login_session['username']
        output += '!</h1>'
        output += '<img src="'
        output += login_session['picture']
        output += ' "> '
        output += '<p>Redirecting to restaurants page...</p>'
        return output