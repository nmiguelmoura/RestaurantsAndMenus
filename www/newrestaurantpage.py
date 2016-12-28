from flask import render_template, request, redirect, url_for, flash

import db_interaction

class New_Restaurant_Page:

    db_rest = db_interaction.DB_interaction()

    def __init__(self):
        pass

    def launch(self):
        if request.method == 'GET':
            return render_template('newrestaurant.html')
        elif request.method == 'POST':
            name = request.form["rest_name"]

            if name:
                self.db_rest.add_restaurant(name)
                return redirect(url_for('show_restaurants'))
            else:
                flash("Please insert a restaurant name.")
                return render_template('newrestaurant.html')

