from flask import render_template, request, redirect, flash

import database_interaction
import prefabs.validate_form_input


class Restaurant_edit:

    db_rest = database_interaction.DB_interaction()
    val = prefabs.validate_form_input.Validate_form_input()

    def __init__(self):
        return

    def launch(self, rest_id):
        restaurant = self.db_rest.query_restaurant_by_id(rest_id)
        if restaurant:
            if request.method == "GET":
                return render_template("editrestaurant.html", restaurant=restaurant, name=restaurant.name)
            elif request.method == "POST":
                name = request.form['rest_name']

                if name:
                    val_name = self.val.validate_string(name, 80)

                    if val_name["response"]:
                        flash(u"%s was edited." % name)
                        self.db_rest.update_restaurant_by_id(rest_id, name)
                        return redirect("/restaurants")
                    else:
                        flash(u"Please insert a restaurant name with no more than 80 characters.")
                        return render_template("editrestaurant.html", restaurant=restaurant, name=name)
                else:
                    flash(u"Please choose a new name or cancel operation.")
                    return render_template("editrestaurant.html", restaurant=restaurant)
        else:
            flash(u"The restaurant you are trying to edit does not exist!")
            return redirect("/pagenotfound")