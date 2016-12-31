from flask import Flask, render_template, jsonify
import restaurantspage
import newrestaurantpage
import editrestaurantpage
import deleterestaurantpage
import menuspage
import newmenupage
import editmenupage
import deletemenupage
import db_interaction

app = Flask(__name__)

restaurants_page = restaurantspage.Restaurants_Page()
new_restaurant_page = newrestaurantpage.New_Restaurant_Page()
edit_restaurant_page = editrestaurantpage.Edit_Restaurant_Page()
delete_restaurant_page = deleterestaurantpage.Delete_Restaurant_Page()
menus_page = menuspage.Menus_Page()
new_menu_page = newmenupage.New_Menu_page()
edit_menu_page = editmenupage.Edit_Menu_Page()
delete_menu_page = deletemenupage.Delete_Menu_Page()
db_rest = db_interaction.DB_interaction()

@app.route('/')
@app.route('/restaurants')
def show_restaurants():
    return restaurants_page.launch()


@app.route('/restaurants/new', methods=['GET', 'POST'])
def add_restaurant():
    return new_restaurant_page.launch()

@app.route('/restaurants/<int:rest_id>/edit', methods=['GET', 'POST'])
def edit_restaurant(rest_id):
    return edit_restaurant_page.launch(rest_id)

@app.route('/restaurants/<int:rest_id>/delete', methods=['GET', 'POST'])
def delete_restaurant(rest_id):
    return delete_restaurant_page.launch(rest_id)

@app.route('/restaurants/<int:rest_id>/menu')
def show_menus(rest_id):
    return menus_page.launch(rest_id)

@app.route('/restaurants/<int:rest_id>/menu/new', methods=['GET', 'POST'])
def add_menu(rest_id):
    return new_menu_page.launch(rest_id)

@app.route('/restaurants/<int:rest_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def edit_menu(rest_id, menu_id):
    return edit_menu_page.launch(rest_id, menu_id)

@app.route('/restaurants/<int:rest_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def delete_menu(rest_id, menu_id):
    return delete_menu_page.launch(rest_id, menu_id)

@app.route('/pagenotfound')
def page_not_found():
    return render_template('pagenotfound.html')

@app.route('/restaurants/JSON')
def restaurant_JSON():
    restaurants, num = db_rest.query_restaurants()
    return jsonify(Restaurants=[r.serialize for r in restaurants])

@app.route('/restaurants/<int:rest_id>/menu/JSON')
def restaurant_menu_JSON(rest_id):
    menus = db_rest.query_menus(rest_id)
    return jsonify(Menus=[m.serialize for m in menus])

@app.route('/restaurants/<int:rest_id>/menu/<int:menu_id>/JSON')
def menu_JSON(rest_id, menu_id):
    menu = db_rest.query_menu_by_id(menu_id)
    return jsonify(Menu=[menu.serialize])


if __name__ == '__main__':
    app.secret_key = "secret_key"
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
