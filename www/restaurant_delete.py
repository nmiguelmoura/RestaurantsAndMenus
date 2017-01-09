from flask import render_template, request, redirect, flash, url_for
from flask import session as login_session
import database_interaction
import prefabs.CSRF_state_generator

class Restaurant_delete:

    db_rest = database_interaction.DB_interaction()
    csrf = prefabs.CSRF_state_generator.CSRF_state_generator()

    def __init__(self):
        pass

    def launch(self, rest_id):
        if 'CSRF' not in login_session:
            login_session['CSRF'] = self.csrf.generate()

        restaurant = self.db_rest.query_restaurant_by_id(rest_id)

        if restaurant:
            if request.method == "GET":
                return render_template('deleterestaurant.html', restaurant=restaurant)
            elif request.method == "POST":
                if self.csrf.validate():
                    flash(u"%s was deleted." % restaurant.name)
                    self.db_rest.delete_restaurant(rest_id)
                    return redirect('/restaurants')
                else:
                    flash(u"You are not authorized to access this page.")
                    return redirect(url_for('page_not_found'))
        else:
            flash("The restaurant you are trying to delete does not exist!")
            return redirect("/pagenotfound")
