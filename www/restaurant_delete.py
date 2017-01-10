from flask import render_template, request, redirect, flash, url_for
from flask import session as login_session
import database_interaction
import prefabs.CSRF_state_generator


class Restaurant_delete:
    '''Class that allows a user to delete a restaurant he has created.'''

    db_rest = database_interaction.DB_interaction()
    csrf = prefabs.CSRF_state_generator.CSRF_state_generator()

    def __init__(self):
        pass

    def launch(self, rest_id):
        # Check if CSRF code was already generated and generate one if it wasnt.
        if 'CSRF' not in login_session:
            login_session['CSRF'] = self.csrf.generate()

        # get restaurant data from DB with restaurant id.
        restaurant = self.db_rest.query_restaurant_by_id(rest_id)

        if restaurant:
            # Run if restaurant exists.

            if restaurant.user_id == self.db_rest.get_user_id(
                    login_session['email']):
                # Run only if user logged in is the creator.
                if request.method == "GET":
                    # Render page template with restaurant data.
                    return render_template('deleterestaurant.html',
                                           restaurant=restaurant)
                elif request.method == "POST":
                    if self.csrf.validate():
                        # If CSRF code is valid perform deletion from DB
                        flash(u"%s was deleted." % restaurant.name)
                        self.db_rest.delete_restaurant(rest_id)
                        return redirect('/restaurants')
                    else:
                        # If CSRF is not valid, generate
                        # flash message and redirect to page not found.
                        flash(u"You are not authorized to access this page.")
                        return redirect(url_for('page_not_found'))
            else:
                # Run if user logged in is not the creator
                flash(u"You are not authorized to access this page.")
                return redirect(url_for('page_not_found'))
        else:
            # If restaurant doesnt exist in DB.
            flash("The restaurant you are trying to delete does not exist!")
            return redirect("/pagenotfound")







