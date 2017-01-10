from flask import render_template, redirect, flash
import database_interaction
import os.path
import prefabs.file_extension_check


class Menus:
    db_rest = database_interaction.DB_interaction()
    extension_check = prefabs.file_extension_check.File_extension_check()

    def __init__(self):
        pass

    def launch(self, rest_id):
        restaurant = self.db_rest.query_restaurant_by_id(rest_id)

        if restaurant:
            menus = self.db_rest.query_menus(rest_id)
            creator = self.db_rest.get_user_info(restaurant.user_id)
            menu_pictures = {}

            if menus:
                extensions = self.extension_check.get_available_extensios()
                path = ''

                for m in menus:
                    for ext in extensions:
                        path = 'uploads/image_menu_%s.%s' % (m.id, ext)
                        if os.path.isfile('static/%s' % path):
                            print path
                            menu_pictures['m_%s' % m.id] = path
                            continue

                print menu_pictures

                return render_template("menu.html",
                                       restaurant=restaurant,
                                       menus=menus,
                                       creator=creator,
                                       menu_pictures=menu_pictures)
            else:
                return render_template("menu.html",
                                       restaurant=restaurant,
                                       menus=[],
                                       menu_pictures=[],
                                       creator=creator,
                                       no_menus=True)
        else:
            flash("The restaurant you are trying to see does not exist!")
            return redirect("/pagenotfound")
