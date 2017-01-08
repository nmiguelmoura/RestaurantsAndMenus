from flask import redirect, flash, url_for, make_response
from flask import session as login_session
import json
import httplib2


class Disconnect():
    def __init__(self):
        pass

    def g_disconnect(self):
        # Only disconnect a connected user.
        credentials = login_session.get('credentials')
        if credentials is None:
            response = make_response(
                json.dumps('Current user not connected.'), 401)
            response.headers['Content-Type'] = 'application/json'
            return response
        access_token = login_session['credentials']
        url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
        h = httplib2.Http()
        result = h.request(url, 'GET')[0]
        if result['status'] != '200':
            # For whatever reason, the given token was invalid.
            response = make_response(
                json.dumps('Failed to revoke token for given user.'), 400)
            response.headers['Content-Type'] = 'application/json'
            return response

    def fb_disconnect(self):
        pass

    def launch(self):
        if 'provider' in login_session:
            if login_session['provider'] == 'google':
                self.g_disconnect()
                del login_session['gplus_id']
                del login_session['credentials']
            elif login_session['provider'] == 'facebook':
                self.fb_disconnect()
                del login_session['facebook_id']

            del login_session['username']
            del login_session['email']
            del login_session['picture']
            del login_session['provider']

            flash('You have successfuly been logged out!')
            return redirect(url_for('show_restaurants'))
        else:
            flash('You are not logged in!')
            return redirect(url_for('show_restaurants'))
