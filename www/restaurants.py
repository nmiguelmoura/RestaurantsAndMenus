from flask import render_template

import database_interaction

class Restaurants:
    '''Class that presents all restaurants in db to user.'''
    db_rest = database_interaction.DB_interaction()

    def __init__(self):
        pass

    def launch(self):
        # Get restaurants list and restaurants count from DB.
        restaurants, num = self.db_rest.query_restaurants()

        # Render page.
        return render_template('restaurants.html', num_restaurants=num, restaurants=restaurants)