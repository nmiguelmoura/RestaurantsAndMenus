from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/restaurants')
def show_restaurants():
    return render_template('restaurants.html')

@app.route('/restaurants/new')
def add_restaurant():
    return render_template('newrestaurant.html')

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
