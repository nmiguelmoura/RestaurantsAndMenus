from flask import render_template, redirect, flash
import database_interaction

class Menus:

    db_rest = database_interaction.DB_interaction()

    def __init__(self):
        pass


    def launch(self, rest_id):
        restaurant = self.db_rest.query_restaurant_by_id(rest_id)

        if restaurant:
            menus = self.db_rest.query_menus(rest_id)
            if menus:
                return render_template("menu.html", restaurant=restaurant, menus=menus)
            else:
                return render_template("menu.html", restaurant=restaurant, menus=[], no_menus=True)
        else:
            flash("The restaurant you are trying to see does not exist!")
            return redirect("/pagenotfound")
