from flask import render_template, request, redirect, flash, url_for
from flask import session as login_session

import database_interaction
import prefabs.validate_form_input
import prefabs.CSRF_state_generator


class Restaurant_edit:
    '''Class that allows a user to edit a restaurant he has created.'''

    db_rest = database_interaction.DB_interaction()
    val = prefabs.validate_form_input.Validate_form_input()
    csrf = prefabs.CSRF_state_generator.CSRF_state_generator()

    def __init__(self):
        return

    def launch(self, rest_id):
        # Check if CSRF code was already generated and generate one if it wasnt.
        if 'CSRF' not in login_session:
            login_session['CSRF'] = self.csrf.generate()

        # Get restaurant data from DB.
        restaurant = self.db_rest.query_restaurant_by_id(rest_id)

        if restaurant:
            # If restaurant exists, check if user logged in is the creator.
            if restaurant.user_id == self.db_rest.get_user_id(
                    login_session['email']):
                # Run only if user logged in is the creator.
                if request.method == "GET":
                    # Render edit page with restaurant info.
                    return render_template("editrestaurant.html",
                                           restaurant=restaurant,
                                           name=restaurant.name)
                elif request.method == "POST":
                    if self.csrf.validate():
                        # Run only if CSRF is valid.

                        # Get new name from form input.
                        name = request.form['rest_name']

                        if name:
                            # If new name exists, validate it.
                            val_name = self.val.validate_string(name, 80)

                            if val_name["response"]:
                                # If new name is valid, store it.
                                flash(u"%s was edited." % name)
                                self.db_rest.update_restaurant_by_id(rest_id,
                                                                     name)
                                return redirect("/restaurants")
                            else:
                                # Run if new name isnt valid.
                                flash(
                                    u"Please insert a restaurant name with no "
                                    u"more than 80 characters.")
                                return render_template("editrestaurant.html",
                                                       restaurant=restaurant,
                                                       name=name)
                        else:
                            # Run if no name has been given.
                            flash(
                                u"Please choose a new name or cancel operation.")
                            return render_template("editrestaurant.html",
                                                   restaurant=restaurant)
                    else:
                        # Run it csrf code isnt valid.
                        flash(u"You are not authorized to access this page.")
                        return redirect(url_for('page_not_found'))
            else:
                # Run if user logged in is not the creator.
                flash(u"You are not authorized to access this page.")
                return redirect(url_for('page_not_found'))

        else:
            # Run if restaurant does not exists.
            flash(u"The restaurant you are trying to edit does not exist!")
            return redirect("/pagenotfound")
