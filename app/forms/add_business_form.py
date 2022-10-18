from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired

PRICES = ['$', '$$', '$$$', '$$$$']

TYPES = [
    ( 'bakeries','Bakeries' ),
    ( 'bubbletea','Bubble Tea' ),
    ( 'cocktailbars','Cocktails' ),
    ( 'bars','Bars' ),
    ( 'brazilian','Brazilian' ),
    ( 'coffee','Coffee & Tea' ),
    ( 'chickenshop','Chicken Shop' ),
    ( 'desserts','Desserts' ),
    ( 'donuts','Donuts' ),
    ( 'dimsum','Dim Sum' ),
    ( 'ethiopian','Ethiopian' ),
    ( 'icecream','Ice Cream & Frozen Yogurt' ),
    ( 'juicebars','Juice Bars & Smoothies' ),
    ( 'bbq','Barbeque' ),
    ( 'breakfast_brunch','Breakfast & Brunch' ),
    ( 'burgers','Burgers' ),
    ( 'cafes','Cafes' ),
    ( 'chicken_wings','Chicken Wings' ),
    ( 'chinese','Chinese' ),
    ( 'gluten_free','Gluten-Free' ),
    ( 'german','German' ),
    ( 'gastropubs','Gastropubs' ),
    ( 'french','French' ),
    ( 'hotdogs','Fast Food' ),
    ( 'indpak','Indian' ),
    ( 'latin','Latin' ),
    ( 'italian','Italian' ),
    ( 'japanese','Japanese' ),
    ( 'korean','Korean' ),
    ( 'newamerican','American (New)' ),
    ( 'mediterranean','Mediterranean' ),
    ( 'mexican','Mexican' ),
    ( 'pizza','Pizza' ),
    ( 'ramen','Ramen' ),
    ( 'noodles','Noodles' ),
    ( 'raw_food','Raw Food' ),
    ( 'salad','Salad' ),
    ( 'sandwiches','Sandwiches' ),
    ( 'soulfood','Soul Food' ),
    ( 'soup','Soup' ),
    ( 'seafood','Seafood' ),
    ( 'steak','Steakhouses' ),
    ( 'sushi','Sushi Bars' ),
    ( 'tacos','Tacos' ),
    ( 'tradamerican','American (Traditional)' ),
    ( 'taiwanese','Taiwanese' ),
    ( 'thai','Thai' ),
    ( 'tapasmallplates','Tapas/Small Plates' ),
    ( 'vegetarian','Vegetarian' ),
    ( 'vegan','Vegan' ),
    ( 'vietnamese','Vietnamese' ),
    ('waffles','Waffles' ),
]


TRANSACTIONS = [('delivery','Delivery'), ('pickup','Pick Up'), ('restaurant_reservation','Reservations')]

class AddBusinessForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    zipcode = StringField('Zipcode', validators=[DataRequired()])
    lat = StringField('Latitude')
    lng = StringField('Longitude')
    price_range = SelectField('Price Range', validators=[DataRequired()], choices=PRICES)
    start_time = StringField('Start Time', validators=[DataRequired()])
    end_time = StringField('End Time', validators=[DataRequired()])
    preview_img = StringField('Preview Image URL (optional)')
    phone_number = StringField('Phone Number (optional)')
    types = SelectMultipleField('Categories (select up to 3)', choices=TYPES)
    transactions = SelectMultipleField('Customer Transaction Options', choices=TRANSACTIONS)

    submit = SubmitField('Submit')
