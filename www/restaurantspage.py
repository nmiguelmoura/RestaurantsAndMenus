import db_interaction

class Restaurants_Page:

    db_rest = db_interaction.DB_interaction()

    def __init__(self):
        pass

    def launch(self, render_template):
        restaurants, num = self.db_rest.query_restaurants()
        return render_template('restaurants.html', num_restaurants=num, restaurants=restaurants)