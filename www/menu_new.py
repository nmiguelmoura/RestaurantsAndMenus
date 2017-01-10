from flask import Flask, render_template, request, redirect, flash, url_for
from flask import session as login_session

import os
from werkzeug.utils import secure_filename

import database_interaction
import prefabs.validate_form_input
import prefabs.CSRF_state_generator
import prefabs.file_extension_check


class Menu_new:
    '''Class that allows the creation of a new, storing it in DB.'''

    db_rest = database_interaction.DB_interaction()
    val = prefabs.validate_form_input.Validate_form_input()
    csrf = prefabs.CSRF_state_generator.CSRF_state_generator()
    extension_check = prefabs.file_extension_check.File_extension_check()

    def __init__(self):
        pass

    def launch(self, rest_id, app):
        # Check if CSRF code is stored already and generate one if it isnt.
        if 'CSRF' not in login_session:
            login_session['CSRF'] = self.csrf.generate()

        # Get restaurant data with restaurant id.
        restaurant = self.db_rest.query_restaurant_by_id(rest_id)

        if restaurant:
            if restaurant.user_id == self.db_rest.get_user_id(
                    login_session['email']):
                # If restaurant exists, menu can be added
                if request.method == "GET":
                    # Render page template.
                    return render_template("newmenu.html",
                                           restaurant=restaurant)
                elif request.method == "POST":
                    if self.csrf.validate():
                        # If CSRF code is valid, get name, course, description
                        # and price from form.
                        name = request.form['menu_name']

                        try:
                            course = request.form['menu_course']
                        except:
                            course = "None"

                        description = request.form['menu_description']
                        price = request.form['menu_price']

                        # Validate data input.
                        val_name = self.val.validate_string(name, 80)
                        val_course = self.val.validate_course(course)
                        val_description = self.val.validate_string(description,
                                                                   250)
                        val_price = self.val.validate_price(price)

                        if val_name["response"] and val_course["response"] and \
                                val_description["response"] and val_price[
                            "response"]:
                            # If data input passed validation test, save menu in DB.
                            flash(u"%s menu was added to %s." % (
                                name, restaurant.name))
                            menu = self.db_rest.add_menu(name, course,
                                                         description,
                                                         val_price["response"],
                                                         rest_id)

                            # Check if there is a file submited by user.
                            file = request.files.get('file')
                            if file and self.extension_check.check(
                                    file.filename):
                                # If user submited a file with correct extension,
                                # save file in folder

                                # Get File extension to allow
                                # new filename composition.
                                ext = self.extension_check.get_extension(
                                    file.filename)

                                # Give new name to file, according to menu id in DB.
                                file.filename = 'image_menu_%s.%s' % (menu, ext)

                                # Save file in folder.
                                # Code as seen in flask docs
                                # (http://flask.pocoo.org/docs/0.12/patterns/fileuploads/)
                                filename = secure_filename(file.filename)
                                file.save(
                                    os.path.join(app.config['UPLOAD_FOLDER'],
                                                 filename))

                            # Show menu list after save.
                            return redirect(
                                url_for("show_menus", rest_id=rest_id))
                        else:
                            # If data doesnt pass validation tests,
                            # render page again with generated error messages.
                            return render_template("newmenu.html",
                                                   restaurant=restaurant,
                                                   name=name,
                                                   description=description,
                                                   price=price,
                                                   name_message=val_name[
                                                       "error_message"],
                                                   course_message=val_course[
                                                       "error_message"],
                                                   description_message=
                                                   val_description[
                                                       "error_message"],
                                                   price_message=val_price[
                                                       "error_message"])
                    else:
                        # If CSRF code isnt valid, generate flash message and
                        # redirect to page not found.
                        flash(u"You are not authorized to access this page.")
                        return redirect(url_for('page_not_found'))
            else:
                # User logged in is not the menu creator.
                flash(u"You are not authorized to access this page.")
                return redirect(url_for('page_not_found'))

        else:
            # If menu does not exist in DB, generate flash message and
            # redirect to page not found.
            flash("The restaurant you are trying to add menus does not exist!")
            return redirect("/pagenotfound")
