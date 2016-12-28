from flask import Flask, render_template
import restaurantspage
import newrestaurantpage
import editrestaurantpage
import deleterestaurantpage

app = Flask(__name__)

restaurants_page = restaurantspage.Restaurants_Page()
new_restaurant_page = newrestaurantpage.New_Restaurant_Page()
edit_restaurant_page = editrestaurantpage.Edit_Restaurant_Page()
delete_restaurant_page = deleterestaurantpage.Delete_Restaurant_Page()

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
    return render_template('menu.html')

@app.route('/restaurants/<int:rest_id>/menu/new')
def add_menu(rest_id):
    return render_template('newmenu.html')

@app.route('/restaurants/<int:rest_id>/menu/<int:menu_id>/edit')
def edit_menu(rest_id, menu_id):
    return render_template('editmenu.html')

@app.route('/restaurants/<int:rest_id>/menu/<int:menu_id>/delete')
def delete_menu(rest_id, menu_id):
    return render_template('deletemenu.html')

@app.route('/pagenotfound')
def page_not_found():
    return render_template('pagenotfound.html')


if __name__ == '__main__':
    app.secret_key = "secret_key"
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
