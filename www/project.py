from flask import Flask, render_template, jsonify
from flask import session as login_session
import restaurants
import restaurant_new
import restaurant_edit
import restaurant_delete
import menus
import menu_new
import menu_edit
import menu_delete
import database_interaction
import random
import string
import google_connect

app = Flask(__name__)

restaurants_page = restaurants.Restaurants()
new_restaurant_page = restaurant_new.Restaurant_new()
edit_restaurant_page = restaurant_edit.Restaurant_edit()
delete_restaurant_page = restaurant_delete.Restaurant_delete()
menus_page = menus.Menus()
new_menu_page = menu_new.Menu_new()
edit_menu_page = menu_edit.Menu_edit()
delete_menu_page = menu_delete.Menu_delete()
db_rest = database_interaction.DB_interaction()
g_connect = google_connect.Google_connect()

@app.route('/')
@app.route('/restaurants/')
def show_restaurants():
    return restaurants_page.launch()


@app.route('/restaurants/new/', methods=['GET', 'POST'])
def add_restaurant():
    return new_restaurant_page.launch()

@app.route('/restaurants/<int:rest_id>/edit/', methods=['GET', 'POST'])
def edit_restaurant(rest_id):
    return edit_restaurant_page.launch(rest_id)

@app.route('/restaurants/<int:rest_id>/delete/', methods=['GET', 'POST'])
def delete_restaurant(rest_id):
    return delete_restaurant_page.launch(rest_id)

@app.route('/restaurants/<int:rest_id>/menu/')
def show_menus(rest_id):
    return menus_page.launch(rest_id)

@app.route('/restaurants/<int:rest_id>/menu/new/', methods=['GET', 'POST'])
def add_menu(rest_id):
    return new_menu_page.launch(rest_id)

@app.route('/restaurants/<int:rest_id>/menu/<int:menu_id>/edit/', methods=['GET', 'POST'])
def edit_menu(rest_id, menu_id):
    return edit_menu_page.launch(rest_id, menu_id)

@app.route('/restaurants/<int:rest_id>/menu/<int:menu_id>/delete/', methods=['GET', 'POST'])
def delete_menu(rest_id, menu_id):
    return delete_menu_page.launch(rest_id, menu_id)

@app.route('/pagenotfound/')
def page_not_found():
    return render_template('pagenotfound.html')

@app.route('/restaurants/JSON/')
def restaurant_JSON():
    restaurants, num = db_rest.query_restaurants()
    return jsonify(Restaurants=[r.serialize for r in restaurants])

@app.route('/restaurants/<int:rest_id>/menu/JSON/')
def restaurant_menu_JSON(rest_id):
    menus = db_rest.query_menus(rest_id)
    return jsonify(Menus=[m.serialize for m in menus])

@app.route('/restaurants/<int:rest_id>/menu/<int:menu_id>/JSON/')
def menu_JSON(rest_id, menu_id):
    menu = db_rest.query_menu_by_id(menu_id)
    return jsonify(Menu=[menu.serialize])

@app.route('/login/')
def login_show():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)

@app.route('/gconnect', methods=['POST'])
def gconnect():
    print"#############"
    print "$$$$$$$$$$$"
    return g_connect.launch()

@app.route('/fbconnect/', methods=['POST'])
def fbconnect():
    return 'connected width facebook'

@app.route('/disconnect/')
def disconnect():
    return 'disconnected'


if __name__ == '__main__':
    app.secret_key = "secret_key"
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
