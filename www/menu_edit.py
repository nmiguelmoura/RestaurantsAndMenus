from flask import render_template, request, redirect, flash, url_for
from flask import session as login_session

import os
from werkzeug.utils import secure_filename

import database_interaction
import prefabs.validate_form_input
import prefabs.CSRF_state_generator
import prefabs.file_extension_check


class Menu_edit:
    db_rest = database_interaction.DB_interaction()
    val = prefabs.validate_form_input.Validate_form_input()
    csrf = prefabs.CSRF_state_generator.CSRF_state_generator()
    extension_check = prefabs.file_extension_check.File_extension_check()

    def __init__(self):
        pass

    def launch(self, rest_id, menu_id, app):
        if 'CSRF' not in login_session:
            login_session['CSRF'] = self.csrf.generate()

        menu = self.db_rest.query_menu_by_id(menu_id)

        if menu:
            if request.method == "GET":
                return render_template("editmenu.html", rest_id=rest_id, menu=menu, name=menu.name,
                                       description=menu.description, price=menu.price)
            elif request.method == "POST":
                if self.csrf.validate():
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

                    if val_name["response"] and val_course["response"] and val_description["response"] and val_price[
                        "response"]:
                        flash(u"%s menu was edited" % name)
                        menu = self.db_rest.update_menu(menu_id, name, course, description, val_price["response"])

                        file = request.files.get('file')
                        print "333333333"
                        print file
                        if file and self.extension_check.check(file.filename):
                            ext = self.extension_check.get_extension(file.filename)
                            print file.filename
                            print ext
                            print app.config['UPLOAD_FOLDER']
                            file.filename = 'image_menu_%s.%s' % (menu, ext)
                            filename = secure_filename(file.filename)
                            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                        return redirect(url_for("show_menus", rest_id=rest_id))
                    else:
                        return render_template("editmenu.html", rest_id=rest_id, menu=menu, name=name,
                                               description=description,
                                               price=price, name_message=val_name["error_message"],
                                               course_message=val_course["error_message"],
                                               description_message=val_description["error_message"],
                                               price_message=val_price["error_message"])
                else:
                    flash(u"You are not authorized to access this page.")
                    return redirect(url_for('page_not_found'))

        else:
            flash("The menu you are trying to edit does not exist!")
            return redirect("/pagenotfound")
