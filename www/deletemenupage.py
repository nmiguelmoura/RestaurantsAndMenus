from flask import render_template, request, redirect, flash, url_for
import db_interaction

class Delete_Menu_Page:

    db_rest = db_interaction.DB_interaction()

    def __init__(self):
        pass

    def launch(self, rest_id, menu_id):
        menu = self.db_rest.query_menu_by_id(menu_id)

        if menu:
            if request.method == "GET":
                return render_template('deletemenu.html', rest_id=rest_id, menu=menu)
            elif request.method == "POST":
                flash(u"%s menu was deleted." % menu.name)
                self.db_rest.delete_menu(menu_id)
                return redirect(url_for('show_menus', rest_id=rest_id))
        else:
            flash("The menu you are trying to delete does not exist!")
            return redirect("/pagenotfound")
