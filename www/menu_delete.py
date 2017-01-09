from flask import render_template, request, redirect, flash, url_for
from flask import session as login_session

import database_interaction
import prefabs.CSRF_state_generator

class Menu_delete:

    db_rest = database_interaction.DB_interaction()
    csrf = prefabs.CSRF_state_generator.CSRF_state_generator()

    def __init__(self):
        pass

    def launch(self, rest_id, menu_id):
        if 'CSRF' not in login_session:
            login_session['CSRF'] = self.csrf.generate()

        menu = self.db_rest.query_menu_by_id(menu_id)

        if menu:
            if request.method == "GET":
                return render_template('deletemenu.html', rest_id=rest_id, menu=menu)
            elif request.method == "POST":
                if self.csrf.validate():
                    flash(u"%s menu was deleted." % menu.name)
                    self.db_rest.delete_menu(menu_id)
                    return redirect(url_for('show_menus', rest_id=rest_id))
                else:
                    flash(u"You are not authorized to access this page.")
                    return redirect(url_for('page_not_found'))
        else:
            flash("The menu you are trying to delete does not exist!")
            return redirect("/pagenotfound")
