from flask import render_template, redirect, flash
import database_interaction
import os.path
import prefabs.file_extension_check


class Menus:
    '''Class that lists all menus for a given restaurant.'''

    db_rest = database_interaction.DB_interaction()
    extension_check = prefabs.file_extension_check.File_extension_check()

    def __init__(self):
        pass

    def launch(self, rest_id):
        # get restaurant data from DB, based in restaurant id.
        restaurant = self.db_rest.query_restaurant_by_id(rest_id)

        if restaurant:
            # If restaurant exists in DB, get menus...
            menus = self.db_rest.query_menus(rest_id)

            # ... and restaurant creator.
            creator = self.db_rest.get_user_info(restaurant.user_id)

            # Create a dictionary to store paths to menu pictures.
            menu_pictures = {}

            if menus:
                # If there are menus associated to the restaurant, get list
                # of image extensions allowed
                extensions = self.extension_check.get_available_extensios()

                # Create a variable to store a path to image file.
                path = ''

                for m in menus:
                    for ext in extensions:
                        # For each menu, and for each extension, check generate
                        # a path based on menu id.
                        path = 'uploads/image_menu_%s.%s' % (m.id, ext)

                        if os.path.isfile('static/%s' % path):
                            # If a file exists in generated path, add path
                            # to menu_pictures dictionary, under menu id key
                            # and continue to next menu.
                            menu_pictures['m_%s' % m.id] = path
                            continue

                # Render menu page with restaurant, menus and creator data,
                # and picture paths.
                return render_template("menu.html",
                                       restaurant=restaurant,
                                       menus=menus,
                                       creator=creator,
                                       menu_pictures=menu_pictures)
            else:
                # Render if no menus are created yet!
                return render_template("menu.html",
                                       restaurant=restaurant,
                                       menus=[],
                                       menu_pictures=[],
                                       creator=creator,
                                       no_menus=True)
        else:
            # If restaurant does not exist, generate flash message
            #  and redirect to page not found.
            flash("The restaurant you are trying to see does not exist!")
            return redirect("/pagenotfound")
