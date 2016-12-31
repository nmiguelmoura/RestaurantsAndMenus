from flask import render_template, request, redirect, url_for, flash

import db_interaction
import validateforminput

class New_Restaurant_Page:

    db_rest = db_interaction.DB_interaction()
    val = validateforminput.Validate_Form_Input()

    def __init__(self):
        pass

    def launch(self):
        if request.method == 'GET':
            return render_template('newrestaurant.html')
        elif request.method == 'POST':
            name = request.form["rest_name"]

            if name:
                val_name = self.val.validate_string(name, 80)

                if val_name["response"]:
                    flash(u"%s was added to the list." % name)
                    self.db_rest.add_restaurant(name)
                    return redirect(url_for('show_restaurants'))
                else:
                    flash(u"Please insert a restaurant name with no more than 80 characters.")
                    return render_template('newrestaurant.html', name=name)
            else:
                flash(u"Please insert a restaurant name.")
                return render_template('newrestaurant.html')

