from app.models import Type, db

types = [
    {'alias': 'bakeries', 'title': 'Bakeries'},
    {'alias': 'bubbletea', 'title': 'Bubble Tea'},
    {'alias': 'coffee', 'title': 'Coffee & Tea'},
    {'alias': 'desserts', 'title': 'Desserts'},
    {'alias': 'donuts', 'title': 'Donuts'},
    {'alias': 'icecream', 'title': 'Ice Cream & Frozen Yogurt'},
    {'alias': 'juicebars', 'title': 'Juice Bars & Smoothies'},
    {'alias': 'bbq', 'title': 'Barbeque'},
    {'alias': 'breakfast_brunch', 'title': 'Breakfast & Brunch'},
    {'alias': 'burgers', 'title': 'Burgers'},
    {'alias': 'cafes', 'title': 'Cafes'},
    {'alias': 'chicken_wings', 'title': 'Chicken Wings'},
    {'alias': 'chinese', 'title': 'Chinese'},
    {'alias': 'gluten_free', 'title': 'Gluten-Free'},
    {'alias': 'hotdogs', 'title': 'Fast Food'},
    {'alias': 'indpak', 'title': 'Indian'},
    {'alias': 'italian', 'title': 'Italian'},
    {'alias': 'japanese', 'title': 'Japanese'},
    {'alias': 'korean', 'title': 'Korean'},
    {'alias': 'mediterranean', 'title': 'Mediterranean'},
    {'alias': 'mexican', 'title': 'Mexican'},
    {'alias': 'pizza', 'title': 'Pizza'},
    {'alias': 'salad', 'title': 'Salad'},
    {'alias': 'sandwiches', 'title': 'Sandwiches'},
    {'alias': 'seafood', 'title': 'Seafood'},
    {'alias': 'steak', 'title': 'Steakhouses'},
    {'alias': 'sushi', 'title': 'Sushi Bars'},
    {'alias': 'thai', 'title': 'Thai'},
    {'alias': 'vegetarian', 'title': 'Vegetarian'},
    {'alias': 'vietnamese', 'title': 'Vietnamese'},
]
instances = []

for type in types:
    instances.append(Type(type=type['title'], alias=type['alias']))


def seed_types():
  for instance in instances:
    db.session.add(instance)

  db.session.commit()


def undo_types():
  db.session.execute('TRUNCATE types RESTART IDENTITY CASCADE;')
  db.session.commit()
