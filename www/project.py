from flask import Flask, render_template, request, redirect, url_for
import restaurantspage
import newrestaurantpage

app = Flask(__name__)

restaurants = restaurantspage.Restaurants_Page()
new_restaurant = newrestaurantpage.New_Restaurant_Page()

@app.route('/')
@app.route('/restaurants')
def show_restaurants():
    return restaurants.launch(render_template)


@app.route('/restaurants/new', methods=['GET', 'POST'])
def add_restaurant():
    return new_restaurant.launch(render_template, request, redirect, url_for)

@app.route('/restaurants/<int:rest_id>/edit')
def edit_restaurant(rest_id):
    return render_template('editrestaurant.html')

@app.route('/restaurants/<int:rest_id>/delete')
def delete_restaurant(rest_id):
    return render_template('deleterestaurant.html')

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


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
