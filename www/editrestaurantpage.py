from flask import render_template, request, redirect, url_for, flash
import db_interaction

class Edit_Restaurant_Page:

    db_rest = db_interaction.DB_interaction()

    def __init__(self):
        return

    def launch(self, rest_id):
        restaurant = self.db_rest.query_restaurant_by_id(rest_id)
        if restaurant:
            if request.method == "GET":
                return render_template("editrestaurant.html", restaurant=restaurant)
            elif request.method == "POST":
                name = request.form['rest_name']

                if name:
                    self.db_rest.update_restaurant_by_id(rest_id, name)
                    return redirect("/restaurants")
                else:
                    flash("Please choose a new name or cancel operation.")
                    return render_template("editrestaurant.html", restaurant=restaurant)
        else:
            flash("The restaurant you are trying to edit does not exist!")
            return redirect("/pagenotfound")
