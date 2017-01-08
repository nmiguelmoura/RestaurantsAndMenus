from flask import render_template, request, redirect, flash, url_for

import database_interaction
import prefabs.validate_form_input


class Menu_edit:

    db_rest = database_interaction.DB_interaction()
    val = prefabs.validate_form_input.Validate_form_input()

    def __init__(self):
        pass

    def launch(self, rest_id, menu_id):
        menu = self.db_rest.query_menu_by_id(menu_id)

        if menu:
            if request.method == "GET":
                return render_template("editmenu.html", rest_id=rest_id, menu=menu, name=menu.name, description=menu.description, price=menu.price)
            elif request.method == "POST":
                name = request.form['menu_name']

                try:
                    course = request.form['menu_course']
                except:
                    course = "None"

                description = request.form['menu_description']
                price = request.form['menu_price']

                val_name = self.val.validate_string(name, 80)
                val_course = self.val.validate_course(course)
                val_description = self.val.validate_string(description, 250)
                val_price = self.val.validate_price(price)

                print val_name["response"]
                print val_course["response"]
                print val_description["response"]
                print val_price["response"]

                if val_name["response"] and val_course["response"] and val_description["response"] and val_price[
                    "response"]:
                    flash(u"%s menu was edited" % name)
                    self.db_rest.update_menu(menu_id, name, course, description, val_price["response"])
                    return redirect(url_for("show_menus", rest_id=rest_id))
                else:
                    return render_template("editmenu.html", rest_id=rest_id, menu=menu, name=name, description=description,
                                           price=price, name_message=val_name["error_message"],
                                           course_message=val_course["error_message"],
                                           description_message=val_description["error_message"],
                                           price_message=val_price["error_message"])
        else:
            flash("The menu you are trying to edit does not exist!")
            return redirect("/pagenotfound")