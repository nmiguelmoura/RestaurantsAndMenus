from flask import render_template, request, redirect, flash, url_for
import db_interaction
import validateforminput

class New_Menu_page:

    db_rest = db_interaction.DB_interaction()
    val = validateforminput.Validate_Form_Input()

    def __init__(self):
        pass


    def launch(self, rest_id):
        restaurant = self.db_rest.query_restaurant_by_id(rest_id)

        if restaurant:
            if request.method == "GET":
                return render_template("newmenu.html", restaurant=restaurant)
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

                if val_name["response"] and val_course["response"] and val_description["response"] and val_price["response"]:
                    flash(u"%s menu was added to %s." % (name,restaurant.name))
                    self.db_rest.add_menu(name, course, description, val_price["response"], rest_id)
                    return redirect(url_for("show_menus", rest_id=rest_id))
                else:
                    return render_template("newmenu.html", restaurant=restaurant, name=name, description=description, price=price, name_message=val_name["error_message"], course_message=val_course["error_message"], description_message=val_description["error_message"], price_message=val_price["error_message"])


        else:
            flash("The restaurant you are trying to add menus does not exist!")
            return redirect("/pagenotfound")