from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session

import database_interaction
import prefabs.validate_form_input
import prefabs.CSRF_state_generator


class Restaurant_new:
    db_rest = database_interaction.DB_interaction()
    val = prefabs.validate_form_input.Validate_form_input()
    csrf = prefabs.CSRF_state_generator.CSRF_state_generator()

    def __init__(self):
        pass

    def launch(self):
        # Check if CSRF code is stored already and generate one if it isnt.
        if 'CSRF' not in login_session:
            login_session['CSRF'] = self.csrf.generate()

        if request.method == 'GET':
            # Render page.
            return render_template('newrestaurant.html')
        elif request.method == 'POST':
            if self.csrf.validate():
                # If CSRF is valid, get name to new restaurant.
                name = request.form["rest_name"]

                if name:
                    # If name was inputed, try to validate it.
                    val_name = self.val.validate_string(name, 80)

                    if val_name["response"]:
                        # If name passed validation, store it.
                        flash(u"%s was added to the list." % name)
                        self.db_rest.add_restaurant(name)
                        return redirect(url_for('show_restaurants'))
                    else:
                        # If name didnt passed validation, re-render page with
                        #  flash message
                        flash(
                            u"Please insert a restaurant name with no more "
                            u"than 80 characters.")
                        return render_template('newrestaurant.html', name=name)
                else:
                    # Run if no name was inserted.
                    flash(u"Please insert a restaurant name.")
                    return render_template('newrestaurant.html')
            else:
                # Run if csrf isnt valid.
                flash(u"You are not authorized to access this page.")
                return redirect(url_for('page_not_found'))
