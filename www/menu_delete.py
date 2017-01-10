from flask import render_template, request, redirect, flash, url_for
from flask import session as login_session

import database_interaction
import prefabs.CSRF_state_generator


class Menu_delete:
    '''Class that handles deletion of menu from list.'''

    db_rest = database_interaction.DB_interaction()
    csrf = prefabs.CSRF_state_generator.CSRF_state_generator()

    def __init__(self):
        pass

    def launch(self, rest_id, menu_id):
        # Check if CSRF code is stored already and generate one if it isnt.
        if 'CSRF' not in login_session:
            login_session['CSRF'] = self.csrf.generate()

        # Get menu data with menu_id.
        menu = self.db_rest.query_menu_by_id(menu_id)

        if menu:
            if menu.user_id == self.db_rest.get_user_id(
                    login_session['email']):
                # Run only if user logged in is the menu creator.

                if request.method == "GET":
                    # Render delete menu page template.
                    return render_template('deletemenu.html', rest_id=rest_id,
                                           menu=menu)
                elif request.method == "POST":
                    if self.csrf.validate():
                        # If CSRF code is valid, generate flash message...
                        flash(u"%s menu was deleted." % menu.name)

                        # ... and perform deletion.
                        self.db_rest.delete_menu(menu_id)

                        # Redirect to menu list.
                        return redirect(url_for('show_menus', rest_id=rest_id))
                    else:
                        # If CSRF code is not valid, generate flash message
                        # and redirect to page not found.
                        flash(u"You are not authorized to access this page.")
                        return redirect(url_for('page_not_found'))
            else:
                # User logged in is not the menu creator.
                flash(u"You are not authorized to access this page.")
                return redirect(url_for('page_not_found'))

        else:
            # If menu doesnt exist in DB, generate flash message
            # and redirect to page not found.
            flash("The menu you are trying to delete does not exist!")
            return redirect(url_for('page_not_found'))
