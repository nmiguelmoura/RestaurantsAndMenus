from flask import render_template, request, redirect, flash
import database_interaction

class Restaurant_delete:

    db_rest = database_interaction.DB_interaction()

    def __init__(self):
        pass

    def launch(self, rest_id):
        restaurant = self.db_rest.query_restaurant_by_id(rest_id)

        if restaurant:
            if request.method == "GET":
                return render_template('deleterestaurant.html', restaurant=restaurant)
            elif request.method == "POST":
                flash(u"%s was deleted." % restaurant.name)
                self.db_rest.delete_restaurant(rest_id)
                return redirect('/restaurants')
        else:
            flash("The restaurant you are trying to delete does not exist!")
            return redirect("/pagenotfound")
