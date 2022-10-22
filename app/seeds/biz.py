from random import choice
from app.models import Business, Transaction, Type, Image, Review, User, db

types_alias = [
    'bakeries',         'bubbletea',
    'coffee',           'desserts',
    'donuts',           'icecream',
    'juicebars',        'bbq',
    'breakfast_brunch', 'burgers',
    'cafes',            'chicken_wings',
    'chinese',          'gluten_free',
    'hotdogs',          'indpak',
    'italian',          'japanese',
    'korean',           'mediterranean',
    'mexican',          'pizza',
    'salad',            'sandwiches',
    'seafood',          'steak',
    'sushi',            'thai',
    'vegetarian',       'vietnamese'
]

types = [
    { 'alias': 'bakeries', 'title': 'Bakeries' },
    { 'alias': 'bubbletea', 'title': 'Bubble Tea' },
    { 'alias': 'cocktailbars', 'title': 'Cocktails' },
    { 'alias': 'bars', 'title': 'Bars' },
    { 'alias': 'brazilian', 'title': 'Brazilian' },
    { 'alias': 'coffee', 'title': 'Coffee & Tea' },
    { 'alias': 'chickenshop', 'title': 'Chicken Shop' },
    { 'alias': 'desserts', 'title': 'Desserts' },
    { 'alias': 'donuts', 'title': 'Donuts' },
    { 'alias': 'dimsum', 'title': 'Dim Sum' },
    { 'alias': 'ethiopian', 'title': 'Ethiopian' },
    { 'alias': 'icecream', 'title': 'Ice Cream & Frozen Yogurt' },
    { 'alias': 'juicebars', 'title': 'Juice Bars & Smoothies' },
    { 'alias': 'bbq', 'title': 'Barbeque' },
    { 'alias': 'breakfast_brunch', 'title': 'Breakfast & Brunch' },
    { 'alias': 'burgers', 'title': 'Burgers' },
    { 'alias': 'cafes', 'title': 'Cafes' },
    { 'alias': 'chicken_wings', 'title': 'Chicken Wings' },
    { 'alias': 'chinese', 'title': 'Chinese' },
    { 'alias': 'gluten_free', 'title': 'Gluten-Free' },
    { 'alias': 'german', 'title': 'German' },
    { 'alias': 'gastropubs', 'title': 'Gastropubs' },
    { 'alias': 'french', 'title': 'French' },
    { 'alias': 'hotdogs', 'title': 'Fast Food' },
    { 'alias': 'indpak', 'title': 'Indian' },
    { 'alias': 'latin', 'title': 'Latin' },
    { 'alias': 'italian', 'title': 'Italian' },
    { 'alias': 'japanese', 'title': 'Japanese' },
    { 'alias': 'korean', 'title': 'Korean' },
    { 'alias': 'newamerican', 'title': 'American (New)' },
    { 'alias': 'mediterranean', 'title': 'Mediterranean' },
    { 'alias': 'mexican', 'title': 'Mexican' },
    { 'alias': 'pizza', 'title': 'Pizza' },
    { 'alias': 'ramen', 'title': 'Ramen' },
    { 'alias': 'noodles', 'title': 'Noodles' },
    { 'alias': 'raw_food', 'title': 'Raw Food' },
    { 'alias': 'salad', 'title': 'Salad' },
    { 'alias': 'sandwiches', 'title': 'Sandwiches' },
    { 'alias': 'soulfood', 'title': 'Soul Food' },
    { 'alias': 'soup', 'title': 'Soup' },
    { 'alias': 'seafood', 'title': 'Seafood' },
    { 'alias': 'steak', 'title': 'Steakhouses' },
    { 'alias': 'sushi', 'title': 'Sushi Bars' },
    { 'alias': 'tacos', 'title': 'Tacos' },
    { 'alias': 'tradamerican', 'title': 'American (Traditional)' },
    { 'alias': 'taiwanese', 'title': 'Taiwanese' },
    { 'alias': 'thai', 'title': 'Thai' },
    { 'alias': 'tapasmallplates', 'title': 'Tapas/Small Plates' },
    { 'alias': 'vegetarian', 'title': 'Vegetarian' },
    { 'alias': 'vegan', 'title': 'Vegan' },
    { 'alias': 'vietnamese', 'title': 'Vietnamese' },
    {'alias': 'waffles', 'title': 'Waffles' },
]

cities = ['Los Angeles', 'San Jose', 'Oakland', 'San Francisco', 'San Diego', 'Austin', 'Dallas', 'Seattle', 'Denver', 'Chicago', 'NYC']

transaction_types = ['pickup', 'delivery', 'restaurant_reservation']

bizzies = [
    {
        # 'id': 'amNWerp63joyW5M6tVbMcQ'0
        'name': 'SK Donuts & Croissant',
        'location': {
            'address1': '5850 W 3rd St',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90036',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['5850 W 3rd St', 'Los Angeles, CA 90036'],
        'lat': 34.06895,
        'lng': -118.34747,
        'price': '$',
        'phone': '+13239352409',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/KJMZ0eazBbMFmg9ode6uoA/o.jpg',
        'categories': ['donuts', 'bakeries', 'vegan'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/KJMZ0eazBbMFmg9ode6uoA/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/gVAKp5bTzSNVcKKW2kw5KA/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/VjIONT6WXkWCNrjbzHOihA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0530', 'end': '1900', 'day': 2}
    },
    {
        # 'id': 'xVSv26KBQexP4M0l63SGlg',1
        'name': 'Alcove Café & Bakery',
        'location': {
            'address1': '1929 Hillhurst Ave',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90027',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1929 Hillhurst Ave', 'Los Angeles, CA 90027'],
        'lat': 34.106215,
        'lng': -118.28776,
        'price': '$$',
        'phone': '+13236440100',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/dOIdDlf-Da34-Xfv6x4V_w/o.jpg',
        'categories': ['bakeries', 'breakfast_brunch', 'newamerican'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/dOIdDlf-Da34-Xfv6x4V_w/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/Iz-jv9nys7Xz3a7Q8VZIvw/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/V83NUEjmbDR8t3EJDHHG9w/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0900', 'end': '2200', 'day': 0}
    },
    {
        # 'id': 'kXrHt3XkNd_q5rISuvuvVg',2
        'name': 'Berlins',
        'location': {
            'address1': '8474 W 3rd St',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90048',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['8474 W 3rd St', 'Los Angeles, CA 90048'],
        'lat': 34.0729528592999,
        'lng': -118.375559776552,
        'price': '$$',
        'phone': '+13237465409',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/pfdYpPzqNEsV-8chnoySsQ/o.jpg',
        'categories': ['bubbletea', 'german', 'sandwiches'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/pfdYpPzqNEsV-8chnoySsQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/J_1Ll9VKLvDn9WxQUzAM1Q/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/gJRFjHeBBV-sZkMDPLk0_g/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2130', 'day': 0}
    },
    {
        # 'id': 'bJVTVJYJL8Es0PzhBsHz8g',4
        'name': 'Tea Master Matcha Cafe & Green Tea Shop',
        'location': {
            'address1': '450 E 2nd St',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90012',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['450 E 2nd St', 'Los Angeles, CA 90012'],
        'lat': 34.0471823589909,
        'lng': -118.238639755523,
        'price': '$',
        'phone': '+12136801006',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/Fua3LsXjQYSdkIXEM9ZYkQ/o.jpg',
        'categories': ['coffee', 'icecream', 'juicebars'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/Fua3LsXjQYSdkIXEM9ZYkQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/mubnqGPodeWqNeqlUlx7Hw/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/FyeX8pklC4nXxGyV6n7cPA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1200', 'end': '1900', 'day': 2}
    },
    {
        # 'id': 'OSYoTFAfq9_wFyDH_qUsTA',5
        'name': 'The Griddle Cafe',
        'location': {
            'address1': '7916 Sunset Blvd',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90046',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['7916 Sunset Blvd', 'Los Angeles, CA 90046'],
        'lat': 34.097727,
        'lng': -118.362275,
        'price': '$$',
        'phone': '+13238740377',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/MpZJYde1MX2FdG5P1Fd44A/o.jpg',
        'categories': ['breakfast_brunch', 'coffee', 'cocktailbars'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/MpZJYde1MX2FdG5P1Fd44A/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/DKzSjXnSTh-TGyDNCm8q7g/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/k55Hvz8FpRYmaN8dkk_Utg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0800', 'end': '1500', 'day': 2}
    },
    {
        # 'id': 'TkFEKhsCixPWlShULKvMdQ',6
        'name': 'Bottega Louie',
        'location': {
            'address1': '700 S Grand Ave',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90017',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['700 S Grand Ave', 'Los Angeles, CA 90017'],
        'lat': 34.047056,
        'lng': -118.256544,
        'price': '$$',
        'phone': '+12138021470',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/rAImnKvUNcNY8i6qEDWrZA/o.jpg',
        'categories': ['italian', 'desserts', 'breakfast_brunch'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/rAImnKvUNcNY8i6qEDWrZA/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/fHHbRyUWjBS2WelSzpqk1A/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/wnawBUv9WbnybmHfnpPexw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0800', 'end': '2300', 'day': 0}
    },
    {
        # 'id': '0WyRlH-fxOVLh1b3oEBEEQ',7
        'name': 'Urth Caffé- Downtown LA',
        'location': {
            'address1': '451 S Hewitt St',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90013',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['451 S Hewitt St', 'Los Angeles, CA 90013'],
        'lat': 34.041974,
        'lng': -118.235426,
        'price': '$$',
        'phone': '+12137974534',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/iv70AVFqtwZpI3AmMkHZjw/o.jpg',
        'categories': ['coffee', 'desserts', 'sandwiches'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/iv70AVFqtwZpI3AmMkHZjw/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/-v9YZ965d1ITd5bw7aQ2Fg/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/N3wYK8XLAFXfe7TyKeHduQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0700', 'end': '2200', 'day': 0}
    },
    {
        # 'id': 'fnieyvmWe2B3bJ19bnxt6g',9
        'name': 'Donut Friend',
        'location': {
            'address1': '5107 York Blvd',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90065',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['5107 York Blvd', 'Los Angeles, CA 90065'],
        'lat': 34.12115,
        'lng': -118.20442,
        'price': '$',
        'phone': '+12139956191',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/hPdtEPpccOVvNScPCT-Tfw/o.jpg',
        'categories': ['desserts', 'donuts', 'vegan'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/hPdtEPpccOVvNScPCT-Tfw/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/1t9hN9A7anBRz1Jt3Lr8_w/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/03d7SGn9zW4cPCRw3UWMpw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1000', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'ikF6L0HiC3_AhAiywWzS3g',11
        'name': 'Salt & Straw',
        'location': {
            'address1': '240 N Larchmont Blvd',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90004',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['240 N Larchmont Blvd', 'Los Angeles, CA 90004'],
        'lat': 34.075825,
        'lng': -118.3235051,
        'price': '$$',
        'phone': '+13234660485',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/j1R2YEl6bC8muSCgo3VL3w/o.jpg',
        'categories': ['icecream'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/j1R2YEl6bC8muSCgo3VL3w/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/VK8jCA8IbxYM6QtsDMsWtQ/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/yvFGooItq1_-GiIt7LcdHg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2300', 'day': 0}
    },
    {
        # 'id': 'CP0ICg1dZqEOt3UtNapjKg',13
        'name': 'Au Lac',
        'location': {
            'address1': '710 W 1st St',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90012',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['710 W 1st St', 'Los Angeles, CA 90012'],
        'lat': 34.0563590452504,
        'lng': -118.250936711212,
        'price': '$$',
        'phone': '+12136172533',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/XiXHckr1WQC7U6gMYhE56g/o.jpg',
        'categories': ['vietnamese', 'raw_food', 'juicebars'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/XiXHckr1WQC7U6gMYhE56g/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/0ubttvwQNth-vIz9PlobOA/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/v1neEqXAfD0HVv6WPVCWsg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1200', 'end': '1500', 'day': 1}
    },
    {
        # 'id': 'qAAoilHU25Qr45FOQlA19g',15
        'name': 'Kang Ho-dong Baekjeong',
        'location': {
            'address1': '3465 W 6th St',
            'address2': 'Ste 20',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90020',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['3465 W 6th St', 'Ste 20', 'Los Angeles, CA 90020'],
        'lat': 34.06375298900917,
        'lng': -118.29728290552232,
        'price': '$$$',
        'phone': '+12133849678',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/0LQSELQTy5LFG3xLUPbRpQ/o.jpg',
        'categories': ['bbq', 'korean'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/0LQSELQTy5LFG3xLUPbRpQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/3SkgsOxmYClY0--3aZj2Jg/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/7TZlLNAtsR2k1w5a9JMi8Q/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1130', 'end': '0000', 'day': 0}
    },
    {
        # 'id': 'z0zaCVA-p_5xTsyUZrmR0g',
        'name': 'Republique',
        'location': {
            'address1': '624 S La Brea Ave',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90036',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['624 S La Brea Ave', 'Los Angeles, CA 90036'],
        'lat': 34.06412,
        'lng': -118.34386,
        'price': '$$',
        'phone': '+13103626115',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/Xy6oJ25E2QUzw_zsBD-dhA/o.jpg',
        'categories': ['french', 'breakfast_brunch', 'cocktailbars'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/Xy6oJ25E2QUzw_zsBD-dhA/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/yUNfbZeF88v_E0xnO1Neuw/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/NhyHvajU0HtP5XWA9glrCQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0800', 'end': '1400', 'day': 0}
    },
    {
        # 'id': 'sYn3SNQP-j2t2XSwjlCbRg',
        'name': "Monty's Good Burger",
        'location': {
            'address1': '516 S Western Ave',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90020',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['516 S Western Ave', 'Los Angeles, CA 90020'],
        'lat': 34.06469,
        'lng': -118.30876,
        'price': '$$',
        'phone': '+12139150257',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/NaDjAGKMS7KhTX9dYMo7_Q/o.jpg',
        'categories': ['burgers', 'vegan', 'chickenshop'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/NaDjAGKMS7KhTX9dYMo7_Q/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/bWC_nY9I9nu7Rk-nOawmug/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/UUQEJw_RVO3CVChbiLPWTA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2300', 'day': 0}
    },
    {
        # 'id': 'h2u-coGd8WWClyU3b7jf8w',
        'name': 'Met Her At A Bar',
        'location': {
            'address1': '759 S La Brea Ave',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90036',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['759 S La Brea Ave', 'Los Angeles, CA 90036'],
        'lat': 34.0609448,
        'lng': -118.3446759,
        'price': '$$',
        'phone': '+13238475013',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/pAzx5GDMh8IdYrOi-1Te6A/o.jpg',
        'categories': ['cafes', 'breakfast_brunch', 'newamerican'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/pAzx5GDMh8IdYrOi-1Te6A/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/6xEsHak_tKgFXtpry-eaQQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/2Vy-EsE-VCAewKh7le7Log/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0800', 'end': '1500', 'day': 0}
    },
    {
        # 'id': 'bdm3708B0OJW9xDdaKVH_A',
        'name': 'Gol Tong Chicken',
        'location': {
            'address1': '361 S Western Ave',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90020',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['361 S Western Ave', 'Los Angeles, CA 90020'],
        'lat': 34.067421417266026,
        'lng': -118.30952639941192,
        'price': '$$',
        'phone': '+12137166116',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/R491zkfeikrD-q8FRY1ISg/o.jpg',
        'categories': ['chicken_wings', 'korean'],
        'transactions': ['delivery', 'pickup'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/R491zkfeikrD-q8FRY1ISg/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/XMc-IAVEe0dcGnT8AOK43Q/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/2ho9qwaLnXTOv0vYovIyLA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1200', 'end': '2200', 'day': 1}
    },
    {
        # 'id': 'ki5SNb4Lli6uOklz6BXXGw',
        'name': 'Blu Jam Café',
        'location': {
            'address1': '7371 Melrose Ave',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90046',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['7371 Melrose Ave', 'Los Angeles, CA 90046'],
        'lat': 34.0837144354804,
        'lng': -118.350571407739,
        'price': '$$',
        'phone': '+13239519191',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/W3j6aLTVb_nH8k6nN8qPTg/o.jpg',
        'categories': ['newamerican', 'breakfast_brunch', 'cafes'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/W3j6aLTVb_nH8k6nN8qPTg/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/5yxyYg7Oa8CP7ijbCswpvQ/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/vipxHa2Iq21FaecuOxS7MA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0900', 'end': '1400', 'day': 0}
    },
    {
        # 'id': 'pAWfcO6e2ae2pIkJXWO-yA',
        'name': "Roscoe's House of Chicken & Waffles - Hollywood",
        'location': {
            'address1': '1514 N Gower St',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90028',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1514 N Gower St', 'Los Angeles, CA 90028'],
        'lat': 34.098566064717666,
        'lng': -118.32219707646978,
        'price': '$$',
        'phone': '+13234667453',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/KO12qRQtLvct2F7u-5nKLw/o.jpg',
        'categories': ['soulfood', 'waffles', 'chicken_wings'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/KO12qRQtLvct2F7u-5nKLw/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/DhT3A1u3BHMfDCdTaf62oA/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/O47uvLc5fdMgl5Gm71fUxQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0800', 'end': '0000', 'day': 0}
    },
    {
        # 'id': 'kdTFcDSl9vAR-btEm1Q2uw',
        'name': 'Bao Dim Sum House',
        'location': {
            'address1': '8256 Beverly Blvd',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90048',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['8256 Beverly Blvd', 'Los Angeles, CA 90048'],
        'lat': 34.07577,
        'lng': -118.36982,
        'price': '$$',
        'phone': '+13236556556',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/Su6hAn4L13LnK_1aZ-dDqQ/o.jpg',
        'categories': ['dimsum', 'bars', 'tapasmallplates'],
        'transactions': ['pickup', 'delivery', 'restaurant_reservation'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/Su6hAn4L13LnK_1aZ-dDqQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/ja9ElKphf6Kk3YbNyVqTAw/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/gf2qjbyQn7gnvjEHW1cluw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1200', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'ohosmz6FXVAeoW5nUkYwng',
        'name': 'Pine & Crane',
        'location': {
            'address1': '1521 Griffith Park Blvd',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90026',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1521 Griffith Park Blvd', 'Los Angeles, CA 90026'],
        'lat': 34.0905963760163,
        'lng': -118.277172084005,
        'price': '$$',
        'phone': '+13236681128',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/3snVXYvGw054cWzcDBvMmQ/o.jpg',
        'categories': ['taiwanese', 'chinese', 'bubbletea'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/3snVXYvGw054cWzcDBvMmQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/MxNriDMd8Otkt4zqOmc0jg/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/04xZ0MmSeWQPUHEzUtfBgQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1200', 'end': '2200', 'day': 0}
    },
    {
        # 'id': '3OJt-Xj45NfCCFwaeKMaeg',
        'name': 'Luv2Eat Thai Bistro',
        'location': {
            'address1': '6660 W Sunset Blvd',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90028',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['6660 W Sunset Blvd', 'Los Angeles, CA 90028'],
        'lat': 34.09773,
        'lng': -118.335936,
        'price': '$$',
        'phone': '+13234985835',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/JmmI2XBvXxbbXW2jGM0eSQ/o.jpg',
        'categories': ['thai', 'gluten_free'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/JmmI2XBvXxbbXW2jGM0eSQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/h_gTJl2vvkGo96rgLwrV8w/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/cQjYBmmK_PZ3R3XYpEd6jw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2145', 'day': 0}
    },
    {
        # 'id': 'KOuqS-inE44o9-1Jix9Tag',
        'name': 'Shojin Downtown',
        'location': {
            'address1': '333 S Alameda St',
            'address2': 'Ste 310',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90013',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['333 S Alameda St', 'Ste 310', 'Los Angeles, CA 90013'],
        'lat': 34.0444135100443,
        'lng': -118.23828298221306,
        'price': '$$$',
        'phone': '+12136170305',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/pkc3hMhYVk_50y-Wn1RbVg/o.jpg',
        'categories': ['japanese', 'vegan', 'gluten_free'],
        'transactions': ['pickup', 'restaurant_reservation', 'delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/pkc3hMhYVk_50y-Wn1RbVg/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/S8rlHVNzbqVL9vJFCH-YvQ/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/-EVQ0OXZ7oZo1Gpj4uhGeg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1730', 'end': '2130', 'day': 1}
    },
    {
        # 'id': 'wjU7E9cMWgxZO9HNTn_tig',
        'name': 'Everytable',
        'location': {
            'address1': '1101 W 23rd St',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90007',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1101 W 23rd St', 'Los Angeles, CA 90007'],
        'lat': 34.0350353531902,
        'lng': -118.283531060368,
        'price': '$',
        'phone': '+12139735095',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/_nXRruiD7InYJMWFBlx09A/o.jpg',
        'categories': ['salad', 'hotdogs'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/_nXRruiD7InYJMWFBlx09A/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/FDeh-mgixAXHZc5lqpBV1Q/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/wEMmAT6F1F4_sIgA1vCpMw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0900', 'end': '2000', 'day': 0}
    },
    {
        # 'id': 'SAowTowinOSZUBm2U7zggQ',
        'name': "Original Tommy's",
        'location': {
            'address1': '2575 Beverly Blvd',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90057',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['2575 Beverly Blvd', 'Los Angeles, CA 90057'],
        'lat': 34.06953,
        'lng': -118.27647,
        'price': '$',
        'phone': '+12133899060',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/LwgLzyhG9jzOF5xP_btYdA/o.jpg',
        'categories': ['burgers', 'hotdogs'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/LwgLzyhG9jzOF5xP_btYdA/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/L00XXets-n5EdRqpDanC_A/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/mY081TCtR13PIIjiDZJ8YA/o.jpg'
        ],
        'hours': {'is_overnight': True, 'start': '0000', 'end': '0000', 'day': 0}
    },
    {
        # 'id': '3XTjerBg_PywBN81Ts45Bg',
        'name': "India's Restaurant",
        'location': {
            'address1': '4366 Fountain Ave',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90029',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['4366 Fountain Ave', 'Los Angeles, CA 90029'],
        'lat': 34.09556,
        'lng': -118.28516,
        'price': '$$',
        'phone': '+13239129230',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/W6wouvpHpHpZR6Ma87Oycg/o.jpg',
        'categories': ['indpak'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/W6wouvpHpHpZR6Ma87Oycg/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/7Y4mpwOgzQ607-Xm7B9wcg/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/jbHcecIXCXH5ZnFHNejF5Q/o.jpg'
        ],
        'hours': {'is_overnight': True, 'start': '1100', 'end': '0100', 'day': 0}
    },
    {
        # 'id': 'uteG6HIb4an-y5fFCXWo7w',
        'name': 'Anarkali Indian Restaurant',
        'location': {
            'address1': '7013 Melrose Ave',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90038',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['7013 Melrose Ave', 'Los Angeles, CA 90038'],
        'lat': 34.08366,
        'lng': -118.34327,
        'price': '$$',
        'phone': '+13239346488',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/PYCWHPhdBfvbdSitZZFoeg/o.jpg',
        'categories': ['indpak'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/PYCWHPhdBfvbdSitZZFoeg/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/yEt68E49xXO-KJgqMt3ojQ/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/kAYwF5TAcT_MRuskQXTbGw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2300', 'day': 0}
    },
    {
        # 'id': 'fEY0zHaDMfIW3-N__joDKQ',
        'name': 'Bestia',
        'location': {
            'address1': '2121 E 7th Pl',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90021',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['2121 E 7th Pl', 'Los Angeles, CA 90021'],
        'lat': 34.03402,
        'lng': -118.22919,
        'price': '$$$',
        'phone': '+12135145724',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/QWniJCG7Jk0GXf9u8lNI4g/o.jpg',
        'categories': ['italian', 'cocktailbars', 'pizza'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/QWniJCG7Jk0GXf9u8lNI4g/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/OiK29eJfT4PyMjCRYlkU8A/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/HYhd80kUtmc5BS-FeW-ilw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1700', 'end': '2300', 'day': 0}
    },
    {
        # 'id': 'iSZpZgVnASwEmlq0DORY2A',
        'name': 'Daikokuya Little Tokyo',
        'location': {
            'address1': '327 E 1st St',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90012',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['327 E 1st St', 'Los Angeles, CA 90012'],
        'lat': 34.05008090944,
        'lng': -118.2401804513,
        'price': '$$',
        'phone': '+12136261680',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/GG71SxFbzBd9-SRMRtB1EQ/o.jpg',
        'categories': ['ramen', 'noodles'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/GG71SxFbzBd9-SRMRtB1EQ/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/oVLiO_X9gWcLoFtRpj7-_A/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/lAmY2NB2tIqcWRb8TSXX1g/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2200', 'day': 0}
    },
    {
        # 'id': 'MlmcOkwaNnxl3Zuk6HsPCQ',
        'name': "Slurpin' Ramen Bar - Los Angeles",
        'location': {
            'address1': '3500 W 8th St',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90005',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['3500 W 8th St', 'Los Angeles, CA 90005'],
        'lat': 34.0573614429986,
        'lng': -118.306769744705,
        'price': '$$',
        'phone': '+12133888607',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/axO_FH4VwDYcPQOuabFi6g/o.jpg',
        'categories': ['ramen', 'noodles'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/axO_FH4VwDYcPQOuabFi6g/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/2CWFcG5Yu-TbQNlWR-XwPw/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/ItfyyYyNjKLYQ-F0cppwMQ/o.jpg'
        ],
        'hours': {'is_overnight': True, 'start': '1130', 'end': '0100', 'day': 0}
    },
    {
        # 'id': 'JYGPEUZy4k5ObXGIjcD3DA',
        'name': 'Hae Jang Chon',
        'location': {
            'address1': '3821 W 6th St',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90020',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['3821 W 6th St', 'Los Angeles, CA 90020'],
        'lat': 34.06383295052755,
        'lng': -118.30612569141431,
        'price': '$$$',
        'phone': '+12133898777',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/UE_ZY3fBqOaun7z-75Drbw/o.jpg',
        'categories': ['korean', 'bbq'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/UE_ZY3fBqOaun7z-75Drbw/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/utraQPqRWf9B9j3pp-5YtQ/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/NIOq3JXvAozR56R8CFNVWA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '0000', 'day': 0}
    },
    {
        # 'id': 'YetYHIRKrZDGHZ50I_RMag',
        'name': "Joe's Falafel",
        'location': {
            'address1': '3535 Cahuenga Blvd W',
            'address2': 'Ste 105',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90068',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['3535 Cahuenga Blvd W', 'Ste 105', 'Los Angeles, CA 90068'],
        'lat': 34.1331825256348,
        'lng': -118.357154846191,
        'price': '$$',
        'phone': '+13235124447',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/FetenpnEfmxBcnNockUffQ/o.jpg',
        'categories': ['mediterranean'],
        'transactions': ['delivery', 'pickup'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/FetenpnEfmxBcnNockUffQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/ocYy6nBSXDc7kLBmc4cBdQ/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/3JVw9Jr5EqCAhoYF6e3XKg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2000', 'day': 0}
    },
    {
        # 'id': 'sXdOBghhw-ZU9S-1HxVZVA',
        'name': 'Bacari Silverlake',
        'location': {
            'address1': '3626 Sunset Blvd',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90026',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['3626 Sunset Blvd', 'Los Angeles, CA 90026'],
        'lat': 34.09031981540568,
        'lng': -118.2775804,
        'price': '$$',
        'phone': '+13234107304',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/rYqoE4hKPWzxKOJ6wZwxfg/o.jpg',
        'categories': ['mediterranean', 'breakfast_brunch', 'cocktailbars'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/rYqoE4hKPWzxKOJ6wZwxfg/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/T-LIqrkSb5MPDbtkbxD9TQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/u0T6fGS05t25F-y1S6bAVA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1700', 'end': '0000', 'day': 0}
    },
    {
        # 'id': 'BDRVlHnK4l0T0ANb7M-Eqg',
        'name': 'Guisados',
        'location': {
            'address1': '1261 W Sunset Blvd',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90026',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1261 W Sunset Blvd', 'Los Angeles, CA 90026'],
        'lat': 34.0702395145121,
        'lng': -118.250448424643,
        'price': '$$',
        'phone': '+12132507600',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/fRSFc5v0r6DdGl5rWkIU4Q/o.jpg',
        'categories': ['mexican'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/fRSFc5v0r6DdGl5rWkIU4Q/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/uz5sMW6Tj4ytmQ0yJYJZOQ/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/JqGxcZ8L2TmRLYRNf59G_g/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1000', 'end': '2200', 'day': 0}
    },
    {
        # 'id': 'beA_DlDpij8O9xK2B-NjEA',
        'name': 'Mex Peru Gipsy',
        'location': {
            'address1': '414 E 12th St',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90015',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['414 E 12th St', 'Los Angeles, CA 90015'],
        'lat': 34.035217,
        'lng': -118.25591,
        'price': '$$',
        'phone': '+12137481773',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/_XRM04RXlzNcj25F5bvpNQ/o.jpg',
        'categories': ['mexican', 'seafood'],
        'transactions': ['delivery', 'pickup'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/_XRM04RXlzNcj25F5bvpNQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/B9_7NNpPbIUNFsPD_BGHug/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/f3CwVoUK_8-FefecLqz7SQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0800', 'end': '2000', 'day': 0}
    },
    {
        # 'id': 'HvDYCHDpgBy3CmzRD6gcMg',
        'name': 'Ktown Pho',
        'location': {
            'address1': '974 S Western Ave',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90006',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['974 S Western Ave', 'Los Angeles, CA 90006'],
        'lat': 34.0533378,
        'lng': -118.3089351,
        'price': '$$',
        'phone': '+13236434772',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/8Go2QkK399BbLAx6TYUZag/o.jpg',
        'categories': ['vietnamese', 'soup', 'salad'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/8Go2QkK399BbLAx6TYUZag/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/c4mwzK43M9bN3uvBOfz3VQ/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/qXX6XUybq8ucntWYXhpvzg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'CbW8U0QAwh5XRkaLt0xNZA',
        'name': 'Masa of Echo Park',
        'location': {
            'address1': '1800 W Sunset Blvd',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90026',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1800 W Sunset Blvd', 'Los Angeles, CA 90026'],
        'lat': 34.077585,
        'lng': -118.259599,
        'price': '$$',
        'phone': '+12139891558',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/k8LDtpavOtjYyjgHcErZaA/o.jpg',
        'categories': ['pizza'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/k8LDtpavOtjYyjgHcErZaA/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/W3ZRmgPx88Fh7S8N-KdoQw/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/ksBVuSWb9Kx-NVAI5rDhcA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2200', 'day': 2}
    },
    {
        # 'id': 'DJek3FUewBzMc0gS-Gms9w',
        'name': 'Morrison Atwater Village',
        'location': {
            'address1': '3179 Los Feliz Blvd',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90039',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['3179 Los Feliz Blvd', 'Los Angeles, CA 90039'],
        'lat': 34.12384,
        'lng': -118.26868,
        'price': '$$',
        'phone': '+13236671839',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/rSDJYD7foVFKvk0Dy6SzzQ/o.jpg',
        'categories': ['gastropubs', 'burgers', 'salad'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/rSDJYD7foVFKvk0Dy6SzzQ/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/8O4EZg0MY12WO388erwViA/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/idYwGqdaJlrEyvLt6T4TNA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1200', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'qCJ2LFfNbXYBIcjXNva1cA',
        'name': "Langer's Delicatessen",
        'location': {
            'address1': '704 S Alvarado St',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90057',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['704 S Alvarado St', 'Los Angeles, CA 90057'],
        'lat': 34.05609,
        'lng': -118.27658,
        'price': '$$',
        'phone': '+12134838050',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/ToD4kygUCYvdcR0GmiAgJQ/o.jpg',
        'categories': ['sandwiches'],
        'transactions': ['delivery', 'pickup'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/ToD4kygUCYvdcR0GmiAgJQ/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/yY0cUmT8STzYJ6P9j5xbAQ/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/_ZeYnqEIsGLfU1zwc5PoXw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0800', 'end': '1600', 'day': 0}
    },
    {
        # 'id': 'TzIJzamxdVGc3zReKbLGaA',
        'name': 'Providence',
        'location': {
            'address1': '5955 Melrose Ave',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90038',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['5955 Melrose Ave', 'Los Angeles, CA 90038'],
        'lat': 34.083628,
        'lng': -118.330168,
        'price': '$$$$',
        'phone': '+13234604170',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/-FiS-IdAwaB3HCgg5OsZ-Q/o.jpg',
        'categories': ['newamerican', 'seafood'],
        'transactions': ['pickup'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/-FiS-IdAwaB3HCgg5OsZ-Q/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/Qm2FBhz3md0dyzQbDQWNVA/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/NQ4NEdMjvj121E4yEAdy3g/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1800', 'end': '2100', 'day': 1}
    },
    {
        # 'id': 'b4SH4SbQUJfXxh6hNkF0wg',
        'name': 'Eggslut',
        'location': {
            'address1': '317 S Broadway',
            'address2': '',
            'address3': 'Grand Central Market',
            'city': 'Los Angeles',
            'zip_code': '90013',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': [
            '317 S Broadway',
            'Grand Central Market',
            'Los Angeles, CA 90013'
        ],
        'lat': 34.05074087639161,
        'lng': -118.2485842438198,
        'price': '$$',
        'phone': '+12136250292',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/MgkGV_YW91JoE5iQBxF7sQ/o.jpg',
        'categories': ['breakfast_brunch', 'sandwiches'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/MgkGV_YW91JoE5iQBxF7sQ/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/5UgA-7elMdTMuxSB7UUJzw/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/6LqCRH8czKvSYMfjdiCPlA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0800', 'end': '1400', 'day': 0}
    },
    {
        # 'id': 'KtEMG1Aln3vQzte92QJxlw',
        'name': 'Genwa Korean BBQ',
        'location': {
            'address1': '5115 Wilshire Blvd',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90036',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['5115 Wilshire Blvd', 'Los Angeles, CA 90036'],
        'lat': 34.062321315088,
        'lng': -118.340898970219,
        'price': '$$',
        'phone': '+13235490760',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/PDf5OepGu6awz-Wi_dX0tA/o.jpg',
        'categories': ['korean', 'bbq', 'seafood'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/PDf5OepGu6awz-Wi_dX0tA/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/2oFZbW7K8gAPqccRIW67qg/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/Xh0-nuXLbKcy32X1Ax8UXQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1200', 'end': '2200', 'day': 0}
    },
    {
        # 'id': 'h_VkRMpSrtjdKDxUJ7sDOQ',
        'name': "Lala's Argentine Grill",
        'location': {
            'address1': '7229 Melrose Ave',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90046',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['7229 Melrose Ave', 'Los Angeles, CA 90046'],
        'lat': 34.08376,
        'lng': -118.34725,
        'price': '$$',
        'phone': '+13239346838',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/GWm8ksNnbrK2XmzxNaEdqQ/o.jpg',
        'categories': ['steak', 'seafood'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/GWm8ksNnbrK2XmzxNaEdqQ/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/mvj-HLdVQN47v3YMRYzbdg/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/TK__ORMK24gBFJf-6S6-0g/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2300', 'day': 0}
    },
    {
        # 'id': 'h9PSJ18gQ4kos8A0XAGlng',
        'name': 'Carlitos Gardel Argentine Steakhouse',
        'location': {
            'address1': '7963 Melrose Ave',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90046',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['7963 Melrose Ave', 'Los Angeles, CA 90046'],
        'lat': 34.0839249,
        'lng': -118.3630799,
        'price': '$$$',
        'phone': '+13236550891',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/zfDw1OksJEHY-Zi18RYKAg/o.jpg',
        'categories': ['steak'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/zfDw1OksJEHY-Zi18RYKAg/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/4m5a_m-hxZ5yk5NNowMTOw/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/rZh_C-siSXJivn2tygd7rg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1700', 'end': '2200', 'day': 0}
    },
    {
        # 'id': 'hC745S5W4HTq606ySmBJNw',
        'name': 'KazuNori  | The Original Hand Roll Bar',
        'location': {
            'address1': '421 S Main St',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90013',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['421 S Main St', 'Los Angeles, CA 90013'],
        'lat': 34.0476390576719,
        'lng': -118.247747561303,
        'price': '$$',
        'phone': '+12134936956',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/9D63gCmIesyBQO15NNG9Xw/o.jpg',
        'categories': ['sushi', 'japanese'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/9D63gCmIesyBQO15NNG9Xw/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/olg_kr395I-XxtSIS_vVZg/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/eVKpFz-g2aBR5MubQnnb7w/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1130', 'end': '2300', 'day': 0}
    },
    {
        # 'id': 'YBmk31pBPukmnRyioe5uBA',
        'name': 'Sushi Gen',
        'location': {
            'address1': '422 E 2nd St',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90012',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['422 E 2nd St', 'Los Angeles, CA 90012'],
        'lat': 34.0470000646326,
        'lng': -118.238502456345,
        'price': '$$$',
        'phone': '+12136170552',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/sAw_hpXedIY_cMzAP5Xa2w/o.jpg',
        'categories': ['sushi', 'japanese'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/sAw_hpXedIY_cMzAP5Xa2w/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/39pgjI_5ck6qni4d9ibjmA/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/iB7cv9reBRQimZ2n8R_-Vw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '1400', 'day': 1}
    },
    {
        # 'id': 'BzmbRSKGs56Yw2w2R12khw',
        'name': 'Hoy-Ka Thai Restaurant',
        'location': {
            'address1': '5908 Sunset Blvd',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90028',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['5908 Sunset Blvd', 'Los Angeles, CA 90028'],
        'lat': 34.09784367,
        'lng': -118.31833767,
        'price': '$$',
        'phone': '+13234632979',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/KC7NEeSA3rnnPVFDhCkZpg/o.jpg',
        'categories': ['thai', 'noodles'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/KC7NEeSA3rnnPVFDhCkZpg/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/WqLEN7q75MfzqfEjQKsK2Q/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/s_HBwPzvUjHbnIT4Ybd5Eg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '1500', 'day': 0}
    },
    {
        # 'id': 'adrzBN4C3jpoCAzJX-xscw',
        'name': 'Pa Ord Noodle',
        'location': {
            'address1': '5301 W Sunset Blvd',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90027',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['5301 W Sunset Blvd', 'Los Angeles, CA 90027'],
        'lat': 34.0985027788903,
        'lng': -118.306131251156,
        'price': '$$',
        'phone': '+13234613945',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/CKjKhF-d3coLGcI4Am3zQA/o.jpg',
        'categories': ['thai', 'noodles'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/CKjKhF-d3coLGcI4Am3zQA/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/mpFa0-QqpKtfU_Jm1kWzhA/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/NGWydvlIgfIqUUuzdqiHFQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2200', 'day': 0}
    },
    {
        # 'id': '6GTaESIP0r1oFunFqqevsw',
        'name': 'Cafe Gratitude',
        'location': {
            'address1': '639 N Larchmont Blvd',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90004',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['639 N Larchmont Blvd', 'Los Angeles, CA 90004'],
        'lat': 34.08279,
        'lng': -118.32404,
        'price': '$$',
        'phone': '+13235806383',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/72A-zETSjEOUoM991M5LKQ/o.jpg',
        'categories': ['vegan', 'vegetarian', 'cafes'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/72A-zETSjEOUoM991M5LKQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/5bijqhM9Q98M-JYpIxAbwQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/M1CRtUS5N41L_QXmpVZB-Q/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0900', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'PMj1TDcrvYTxEXd-g9LcWA',
        'name': 'Zinc Cafe & Market',
        'location': {
            'address1': '580 Mateo St',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90013',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['580 Mateo St', 'Los Angeles, CA 90013'],
        'lat': 34.039413,
        'lng': -118.232504,
        'price': '$$',
        'phone': '+13238255381',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/ht1YCHqrpeQ_DxV5hX_KaQ/o.jpg',
        'categories': ['breakfast_brunch', 'vegetarian'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/ht1YCHqrpeQ_DxV5hX_KaQ/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/xvZ9ACm3G981Cj7w3FJ5CQ/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/z0IimKPZRvOL70x_vXXNhA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0900', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'EiGZST3PxwKs94PTOsD4eQ',
        'name': 'Pho 87',
        'location': {
            'address1': '1019 N Broadway',
            'address2': '',
            'address3': '',
            'city': 'Los Angeles',
            'zip_code': '90012',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1019 N Broadway', 'Los Angeles, CA 90012'],
        'lat': 34.0672573,
        'lng': -118.2356333,
        'price': '$$',
        'phone': '+13232270758',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/OzwvP4wW1MP1a22IOyTT6A/o.jpg',
        'categories': ['vietnamese', 'noodles', 'chinese'],
        'transactions': [],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/OzwvP4wW1MP1a22IOyTT6A/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/OZfCeGXBKAGaDMOPeYE9KQ/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/FqId-kbabPsgVlQ84PUv8g/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2000', 'day': 0}
    },
    {
        # 'id': 'baEPmtktizrZDmH4p_OJ4A',
        'name': 'Shuei-Do Manju Shop',
        'location': {
            'address1': '217 Jackson St',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95112',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['217 Jackson St', 'San Jose, CA 95112'],
        'lat': 37.34935,
        'lng': -121.89401,
        'price': '$',
        'phone': '+14082944148',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/1uHzL2BYW2AlqfMlrfZmFA/o.jpg',
        'categories': ['bakeries', 'japanese'],
        'transactions': [],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/1uHzL2BYW2AlqfMlrfZmFA/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/66Kck-tTOB3QQdZ-7ryyxw/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/9NPUAxsDNe6FooPshx19fg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1000', 'end': '1600', 'day': 3}
    },
    {
        # 'id': 'lPkQK2N4g658SR_7BBxeaQ',
        'name': "Peters' Bakery",
        'location': {
            'address1': '3108 Alum Rock Ave',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95127',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['3108 Alum Rock Ave', 'San Jose, CA 95127'],
        'lat': 37.36573,
        'lng': -121.82734,
        'price': '$',
        'phone': '+14082583529',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/QDjFZWIqoF16igCnvUPwdw/o.jpg',
        'categories': ['bakeries', 'donuts'],
        'transactions': [],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/QDjFZWIqoF16igCnvUPwdw/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/bt6iSI9vgTZWxIr5w2Gumw/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/mAIpm2TK7DsmQs-H6q8iBw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0630', 'end': '1800', 'day': 1}
    },
    {
        # 'id': 'VkV85hclKc8saSU4UDNjQQ',
        'name': 'Pekoe',
        'location': {
            'address1': '3276 S White Rd',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95148',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['3276 S White Rd', 'San Jose, CA 95148'],
        'lat': 37.3145584994999,
        'lng': -121.790188997984,
        'price': '$$',
        'phone': '+14088180696',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/ce6dy5tUbo3XxSUK6Qht0w/o.jpg',
        'categories': ['coffee', 'bubbletea'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/ce6dy5tUbo3XxSUK6Qht0w/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/6bayfRO6-R9A4PwWwwOmTQ/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/7WyzRWAJUCBAAPQVbYWmVg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1000', 'end': '0000', 'day': 0}
    },
    {
        # 'id': 'gQInCoEeqCNiSuomfFPkwA',
        'name': 'Sweet Gelato Tea Lounge',
        'location': {
            'address1': '979 Story Rd',
            'address2': 'Ste 7084',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95122',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['979 Story Rd', 'Ste 7084', 'San Jose, CA 95122'],
        'lat': 37.3313361147367,
        'lng': -121.857381949738,
        'price': '$$',
        'phone': '+14082759999',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/PM7ZePHQQnUa2G26NGj0CQ/o.jpg',
        'categories': ['bubbletea', 'coffee'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/PM7ZePHQQnUa2G26NGj0CQ/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/Cekx5mRqcW1jK6u2KqMC0w/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/mQhdBQkPdTnOmN2FhfMyVw/o.jpg'
        ],
        'hours': {'is_overnight': True, 'start': '1700', 'end': '0100', 'day': 0}
    },
    {
        # 'id': 'eXprR2i_W8UKMmsYYbZFQQ',
        'name': 'Philz Coffee',
        'location': {
            'address1': '118 Paseo De San Antonio Walk',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95112',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['118 Paseo De San Antonio Walk', 'San Jose, CA 95112'],
        'lat': 37.333609,
        'lng': -121.884901,
        'price': '$$',
        'phone': '+14089714212',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/gKyzJmgR_XzLkV1HzoOUWQ/o.jpg',
        'categories': ['coffee'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/gKyzJmgR_XzLkV1HzoOUWQ/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/Zn5KEGCw7I8NUjsq_9p8Cw/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/IHXnh89OSbd3XLX0m6pZyg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0630', 'end': '1800', 'day': 0}
    },
    {
        # 'id': 'vgseXwt9c975jus_PBM-zA',
        'name': 'Anton SV Pâtisserie',
        'location': {
            'address1': '1969 Otoole Way',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95131',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1969 Otoole Way', 'San Jose, CA 95131'],
        'lat': 37.38477,
        'lng': -121.9074193,
        'price': '$$$',
        'phone': '+16502737357',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/q6wrUAGdFJCYdk7wkMUBcA/o.jpg',
        'categories': ['bakeries', 'desserts'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/q6wrUAGdFJCYdk7wkMUBcA/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/t9T3jvy31NI7qlW3C3RVcQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/XWCa9MDHTMCIcpqbq5JT1Q/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '1800', 'day': 0}
    },
    {
        # 'id': 'lDLzKkPIB6mE7FKroJleug',
        'name': "Charlie's Cheesecake Works",
        'location': {
            'address1': '1179 Redmond Ave',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95120',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1179 Redmond Ave', 'San Jose, CA 95120'],
        'lat': 37.229854,
        'lng': -121.871857,
        'price': '$$',
        'phone': '+14082684555',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/Juxg8u7rF2tbbJMT_WyLag/o.jpg',
        'categories': ['bakeries', 'desserts'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/Juxg8u7rF2tbbJMT_WyLag/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/3iCqsaxCCFp2nM0g2PNoQQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/7BmG7q9GettkawrQnZBZLw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0700', 'end': '1800', 'day': 0}
    },
    {
        # 'id': 'V0UiBNqNEx1YmR1SOI4lQw',
        'name': 'Mexico Bakery',
        'location': {
            'address1': '2811 Story Rd',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95127',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['2811 Story Rd', 'San Jose, CA 95127'],
        'lat': 37.3531827354946,
        'lng': -121.824288292862,
        'price': '$',
        'phone': '+14082723838',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/dw9vjiMXXRBTvWYgA-Fadw/o.jpg',
        'categories': ['bakeries', 'sandwiches', 'donuts'],
        'transactions': ['delivery', 'pickup'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/dw9vjiMXXRBTvWYgA-Fadw/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/YFaeSC4P84HllIoA3dhYbA/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/faDpVegSw1nPGuMYbxOFRA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0500', 'end': '2200', 'day': 0}
    },
    {
        # 'id': 'k901qMpKUjNES5mFJOComA',
        'name': 'Sweet Rendezvous',
        'location': {
            'address1': '668 Blossom Hill Rd',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95123',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['668 Blossom Hill Rd', 'San Jose, CA 95123'],
        'lat': 37.2492499194819,
        'lng': -121.845885111639,
        'price': '$$',
        'phone': '+14082255004',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/bR08hkGqs_vu33KI2q27og/o.jpg',
        'categories': ['desserts', 'icecream'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/bR08hkGqs_vu33KI2q27og/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/6Mu4yRT9RSpBA8ilu149mQ/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/5Rh8rLRdovvvIMLfgtgeDw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1200', 'end': '2100', 'day': 0}
    },
    {
        # 'id': '0ba79WK2mc1txlZoWGpcRA',
        'name': 'Willow Glen Creamery',
        'location': {
            'address1': '1100 Lincoln Ave',
            'address2': 'Ste 130',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95125',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1100 Lincoln Ave', 'Ste 130', 'San Jose, CA 95125'],
        'lat': 37.308404,
        'lng': -121.900321,
        'price': '$',
        'phone': '+14082925961',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/xJ2mnV1j2tyKCLATak7Qew/o.jpg',
        'categories': ['icecream'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/xJ2mnV1j2tyKCLATak7Qew/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/8ZPqna4jcRfzVWDR7tdomw/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/InI08C0koeTE4Mc6OfGgfw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1200', 'end': '2200', 'day': 1}
    },
    {
        # 'id': 'xfoNyFG72oPSjf9x9nAHVw',
        'name': 'Vegan Donut And Cafe',
        'location': {
            'address1': '449 E Santa Clara St',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95113',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['449 E Santa Clara St', 'San Jose, CA 95113'],
        'lat': 37.34084,
        'lng': -121.8814,
        'price': '$$',
        'phone': '+14086068664',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/5dLilrC0Iu9eo3hOuHN7Zw/o.jpg',
        'categories': ['donuts', 'juicebars'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/5dLilrC0Iu9eo3hOuHN7Zw/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/X0rh2imDP9A8dY9igZxVIw/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/z0CXoo6URZcjNAQCVXZX-w/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0800', 'end': '1400', 'day': 3}
    },
    {
        # 'id': 'Y4wgkkCvoclvVxTkTS8MCw',
        'name': 'Tiger Tea & Juice - San Jose',
        'location': {
            'address1': '1706 Oakland Rd',
            'address2': 'Ste 25',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95131',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1706 Oakland Rd', 'Ste 25', 'San Jose, CA 95131'],
        'lat': 37.3834901708966,
        'lng': -121.893125809729,
        'price': '$$',
        'phone': '+16502019822',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/lnOVwgKZf4kii-BFHKaikQ/o.jpg',
        'categories': ['bubbletea', 'juicebars'],
        'transactions': ['delivery', 'pickup'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/lnOVwgKZf4kii-BFHKaikQ/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/6LMpMNT25v9efj5nafe7BA/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/gG_v402oP7cmaRvqVIFSgA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2130', 'day': 0}
    },
    {
        # 'id': 'jfMK6n5Mln7ilco6r2YXoA',
        'name': 'QPOT',
        'location': {
            'address1': '1610 E Capitol Expy',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95121',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1610 E Capitol Expy', 'San Jose, CA 95121'],
        'lat': 37.305813,
        'lng': -121.812039,
        'price': '$$',
        'phone': '+16692343095',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/n2flHH6CC6OVTNULFDLLDQ/o.jpg',
        'categories': ['korean', 'bbq'],
        'transactions': ['pickup'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/n2flHH6CC6OVTNULFDLLDQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/wFRgyzSt0JzQUPgrEhouCw/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/MBFIClNpn3vmfp6t-5_LGQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2300', 'day': 0}
    },
    {
        # 'id': 'TQEfj1-QhyWCJ29u3l9Kjw',
        'name': 'Gen Korean BBQ House',
        'location': {
            'address1': '1628 Hostetter Rd',
            'address2': 'Ste F',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95131',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1628 Hostetter Rd', 'Ste F', 'San Jose, CA 95131'],
        'lat': 37.3872324410459,
        'lng': -121.885422354631,
        'price': '$$',
        'phone': '+14084772773',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/-g5mYPUvxsX7hfor95Iq-Q/o.jpg',
        'categories': ['korean', 'bbq'],
        'transactions': [],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/-g5mYPUvxsX7hfor95Iq-Q/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1030', 'end': '2300', 'day': 0}
    },
    {
        # 'id': 'rjUOwXNxsg0tstFssAjfsQ',
        'name': 'LUNA Mexican Kitchen - The Alameda',
        'location': {
            'address1': '1495 The Alameda',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95126',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1495 The Alameda', 'San Jose, CA 95126'],
        'lat': 37.33399,
        'lng': -121.915279,
        'price': '$$',
        'phone': '+14083202654',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/JjzG0auXHdUing7hHn7keQ/o.jpg',
        'categories': ['mexican', 'breakfast_brunch', 'vegetarian'],
        'transactions': ['pickup'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/JjzG0auXHdUing7hHn7keQ/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/vs_mNhVvxbuREFkLbH8A2A/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/em0WYcE5FoREmHGMLR1zcw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0900', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'i50BEr4Pq6-D8tmsegmVyA',
        'name': 'The Table',
        'location': {
            'address1': '1110 Willow St',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95125',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1110 Willow St', 'San Jose, CA 95125'],
        'lat': 37.308203,
        'lng': -121.901284,
        'price': '$$',
        'phone': '+14086387911',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/KMiVsvM886v1DpX7Ic9oxg/o.jpg',
        'categories': ['newamerican', 'breakfast_brunch', 'salad'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/KMiVsvM886v1DpX7Ic9oxg/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/cmtZvexB_X4zSFsk8XcDSA/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/2X-lw7TSzGrTkCdhxJWTnw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0900', 'end': '2100', 'day': 2}
    },
    {
        # 'id': 'yMPz0Hj-Y5Z_cSCeuUNV8w',
        'name': 'The Counter Santana Row',
        'location': {
            'address1': '3055 Olin Ave',
            'address2': 'Ste 1035',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95128',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['3055 Olin Ave', 'Ste 1035', 'San Jose, CA 95128'],
        'lat': 37.320965,
        'lng': -121.94892,
        'price': '$$',
        'phone': '+14086101362',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/xQI8u-GnGY-iI9-WzFCTWA/o.jpg',
        'categories': ['burgers', 'sandwiches'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/xQI8u-GnGY-iI9-WzFCTWA/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/zh5L2UiZD2RLXi5PsYbosg/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/yJJLDlIw5z7QRPwN22bPfA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1130', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'rSe_sHr66XDGGIzjQO9K3w',
        'name': 'Sliders Burgers',
        'location': {
            'address1': '1645 W San Carlos St',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95128',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1645 W San Carlos St', 'San Jose, CA 95128'],
        'lat': 37.323965,
        'lng': -121.92096,
        'price': '$$',
        'phone': '+14082984340',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/rdlckhxgIMwKhrxna9IwuQ/o.jpg',
        'categories': ['burgers', 'hotdogs', 'tradamerican'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/rdlckhxgIMwKhrxna9IwuQ/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/ZMMlEEgSYT6j0H7e771W7g/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/7jQxMVh14S-7YN91dUwIng/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2100', 'day': 1}
    },
    {
        # 'id': 'HnMZ-pm4P3sUnASbg05ZlQ',
        'name': 'Yeganeh Bakery & Kafe Unik',
        'location': {
            'address1': '3275 Stevens Creek Blvd',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95117',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['3275 Stevens Creek Blvd', 'San Jose, CA 95117'],
        'lat': 37.3234875728828,
        'lng': -121.954808267698,
        'price': '$$',
        'phone': '+14086661229',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/vnZGnGRfTeuSWPF69Iws0g/o.jpg',
        'categories': ['breakfast_brunch', 'sandwiches', 'cafes'],
        'transactions': ['delivery', 'pickup'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/vnZGnGRfTeuSWPF69Iws0g/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/iU0tsMLUdeymTpZhsHx9RA/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/wjoQ4GHxNVjJT7uHb_kLTA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0800', 'end': '2000', 'day': 0}
    },
    {
        # 'id': 'NQ0KQoCTdkXICx36Z0t_lA',
        'name': 'Clover Bakery & Cafe',
        'location': {
            'address1': '4342 Moorpark Ave',
            'address2': 'Ste A',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95129',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['4342 Moorpark Ave', 'Ste A', 'San Jose, CA 95129'],
        'lat': 37.3155397971275,
        'lng': -121.978173101276,
        'price': '$',
        'phone': '+14082573412',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/eGSzb1OGJAjbe23HiuX_MA/o.jpg',
        'categories': ['bakeries', 'cafes', 'sandwiches'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/eGSzb1OGJAjbe23HiuX_MA/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/j6xYoxN42jHqICW-S62DGA/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/Nxm8ZHbO7vg8d8ZMJLbYGg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0800', 'end': '1700', 'day': 1}
    },
    {
        # 'id': '7HBtj81aBo2DEZFTPaaeqg',
        'name': 'Slice of Homage Pizza',
        'location': {
            'address1': '152 Post St',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95113',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['152 Post St', 'San Jose, CA 95113'],
        'lat': 37.33401377933768,
        'lng': -121.89231238444917,
        'price': '$$',
        'phone': '+14082867678',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/Pin-QLGXFrVLM88HEu4Pzw/o.jpg',
        'categories': ['pizza', 'newamerican', 'chicken_wings'],
        'transactions': [],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/Pin-QLGXFrVLM88HEu4Pzw/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/ToFHMsAVcuomRGSbo8rZTg/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/oNzGXQeD0_GGguFltceBAQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1600', 'end': '2000', 'day': 2}
    },
    {
        # 'id': 'OeePb_OQIgCnt3nO53XEtA',
        'name': 'Claw Shack',
        'location': {
            'address1': '1696 Berryessa Rd',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95133',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1696 Berryessa Rd', 'San Jose, CA 95133'],
        'lat': 37.3732322,
        'lng': -121.873416,
        'price': '$$',
        'phone': '+14086496741',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/eXg0Lo6O-3co2BERIPBJlw/o.jpg',
        'categories': ['seafood', 'chicken_wings'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/eXg0Lo6O-3co2BERIPBJlw/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/lzOrPJKjYOe50s0syDcCCQ/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/09J7eoBn26L_j-ekWNV72w/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1500', 'end': '2000', 'day': 1}
    },
    {
        # 'id': 'RDIjI4qSHkvVlHkfJ3AxCQ',
        'name': 'Sweet Mango',
        'location': {
            'address1': '1040 Willow St',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95125',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1040 Willow St', 'San Jose, CA 95125'],
        'lat': 37.308871,
        'lng': -121.899619,
        'price': '$$',
        'phone': '+14082932268',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/j9-Bgo70cTxAZ5lQ2JLO2w/o.jpg',
        'categories': ['chinese', 'thai'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/j9-Bgo70cTxAZ5lQ2JLO2w/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/3ylQUldC32zNBdj7XDakQg/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/0m3cRigQ99VrAPx-p31TWA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '1430', 'day': 0}
    },
    {
        # 'id': 'dRTsqnuEtOT3DoYaGnBCSw',
        'name': 'China Chen',
        'location': {
            'address1': '400 S 3rd St',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95112',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['400 S 3rd St', 'San Jose, CA 95112'],
        'lat': 37.3309756,
        'lng': -121.8836463,
        'price': '$$',
        'phone': '+14082942525',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/dEkntJHJfumGS7_tJAjt6A/o.jpg',
        'categories': ['chinese', 'vietnamese', 'noodles'],
        'transactions': ['pickup'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/dEkntJHJfumGS7_tJAjt6A/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/SRTNHXL63uF_zuP_O2VM1A/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/JAenczAcTbL9IZeLqEDUiA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1000', 'end': '1900', 'day': 0}
    },
    {
        # 'id': 'srBchC4ngf1sRefmSGseJA',
        'name': 'Walia Ethiopian Cuisine',
        'location': {
            'address1': '2208 Business Cir',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95128',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['2208 Business Cir', 'San Jose, CA 95128'],
        'lat': 37.322462,
        'lng': -121.932442,
        'price': '$$',
        'phone': '+14086455001',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/ktU3fsSWjKm5vwoKMWR55Q/o.jpg',
        'categories': ['ethiopian', 'gluten_free', 'vegetarian'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/ktU3fsSWjKm5vwoKMWR55Q/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/ydxNEFl15uMMmy4XdkYOgg/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/VPhnp1-N1IrToUsuka7K-Q/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1130', 'end': '1500', 'day': 2}
    },
    {
        # 'id': '42Wz6MMu9vz4Kg21cErXsQ',
        'name': 'Gojo Ethiopian Restaurant',
        'location': {
            'address1': '1261 W San Carlos St',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95126',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1261 W San Carlos St', 'San Jose, CA 95126'],
        'lat': 37.323724,
        'lng': -121.910823,
        'price': '$$',
        'phone': '+14082959546',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/n2AT8ya5S2e8EooizyyaJA/o.jpg',
        'categories': ['ethiopian', 'gluten_free'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/n2AT8ya5S2e8EooizyyaJA/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/TRsB6BOp9dVeCr7TiPN99Q/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/WPmU0nJcaSPX4VNc3Q28PQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1130', 'end': '2130', 'day': 1}
    },
    {
        # 'id': 'jw7wkWmTX04fRYLcp9vlPQ',
        'name': "Falafel's Drive-In",
        'location': {
            'address1': '2301 Stevens Creek Blvd',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95128',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['2301 Stevens Creek Blvd', 'San Jose, CA 95128'],
        'lat': 37.323719276993586,
        'lng': -121.93508055499373,
        'price': '$$',
        'phone': '+14082947886',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/9oY9kB9GMCsd7dGWB_ttfg/o.jpg',
        'categories': ['hotdogs'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/9oY9kB9GMCsd7dGWB_ttfg/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/blNelTuTid-WCnQdmpCMzQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/mHmUEG_gdQWBU0I7ymM07A/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1000', 'end': '2000', 'day': 0}
    },
    {
        # 'id': '9so8PQIG3Q-6mXQg5756CQ',
        'name': 'Sam and Curry',
        'location': {
            'address1': '1751 N 1st St',
            'address2': 'Ste 40',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95112',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1751 N 1st St', 'Ste 40', 'San Jose, CA 95112'],
        'lat': 37.37082474435312,
        'lng': -121.91692008435224,
        'price': '$$',
        'phone': '+16692427956',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/oFTEmX487cZkynG796Skdg/o.jpg',
        'categories': ['indpak'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/oFTEmX487cZkynG796Skdg/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/eMp6nMuGggj_T8oFhUZ7Eg/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/dGsN_JdwxFA4fcNn18ptpA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2000', 'day': 0}
    },
    {
        # 'id': 'fuQOU_6-sjCuitcCvtYOvw',
        'name': 'Punjab Cafe',
        'location': {
            'address1': '322 E Santa Clara St',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95113',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['322 E Santa Clara St', 'San Jose, CA 95113'],
        'lat': 37.33918,
        'lng': -121.88356,
        'price': '$$',
        'phone': '+14082955470',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/YkEq42na4gjc0IOVwdhYkA/o.jpg',
        'categories': ['indpak'],
        'transactions': ['delivery', 'pickup'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/YkEq42na4gjc0IOVwdhYkA/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/Ws_rzLGQstZCRwfIKI4tKg/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/vh7gD4SaUBcBzvBZVB8Fdw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1030', 'end': '1430', 'day': 1}
    },
    {
        # 'id': 'zXQF2Z_tyujpn9hJlJhURQ',
        'name': "Antipasto's By Derose Gourmet Meat Fish & Deli",
        'location': {
            'address1': '3454 McKee Rd',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95127',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['3454 McKee Rd', 'San Jose, CA 95127'],
        'lat': 37.3801496200615,
        'lng': -121.827435493469,
        'price': '$$',
        'phone': '+14082515647',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/oufwnq30P5CeVYoLhoKbew/o.jpg',
        'categories': ['italian'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/oufwnq30P5CeVYoLhoKbew/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/MBEQMQ-79qRhkCK1lpTbMQ/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/cz4PKevCEGTlutQZm6i2BQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1000', 'end': '1700', 'day': 1}
    },
    {
        # 'id': 'Q7OkRjnqIJmeZJHCnbnIcA',
        'name': "Bertucelli's La Villa",
        'location': {
            'address1': '1319 Lincoln Ave',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95125',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1319 Lincoln Ave', 'San Jose, CA 95125'],
        'lat': 37.30458,
        'lng': -121.89858,
        'price': '$$',
        'phone': '+14082957851',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/B05XRqHtuEe4TRXYRqJH0g/o.jpg',
        'categories': ['sandwiches', 'italian'],
        'transactions': ['delivery', 'pickup'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/B05XRqHtuEe4TRXYRqJH0g/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/tBwu8oR_G0GNN1ZtZU2gTw/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/xkquIVHijztubrTkaE2GKw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1030', 'end': '1730', 'day': 1}
    },
    {
        # 'id': 'cCKea_ufuGcxI14fhe84vw',
        'name': 'Cha Cha Sushi',
        'location': {
            'address1': '547 W Capitol Expy',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95136',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['547 W Capitol Expy', 'San Jose, CA 95136'],
        'lat': 37.2758545677726,
        'lng': -121.852952245369,
        'price': '$$',
        'phone': '+14082652416',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/532FKhWbs6msCiuDjU3NwA/o.jpg',
        'categories': ['sushi', 'japanese'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/532FKhWbs6msCiuDjU3NwA/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/UVGds0XA_DTvRRs4F6FGZA/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/Vh2q3mQ-IFmYQ_WYV9H9kQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'ZMdteLcR8y2N-oJAd9cmEg',
        'name': "Souvlaki's Greek Skewers",
        'location': {
            'address1': '577 W Alma Ave',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95125',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['577 W Alma Ave', 'San Jose, CA 95125'],
        'lat': 37.3092867427984,
        'lng': -121.887104945135,
        'price': '$$',
        'phone': '+14082891452',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/oz6rQqG6fZc9wi5gsddzOA/o.jpg',
        'categories': ['mediterranean'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/oz6rQqG6fZc9wi5gsddzOA/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/DDfoKTNmh3iYHOmjYl_6cg/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/VEKytZ3kyGOqx1eTRanN7g/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2030', 'day': 0}
    },
    {
        # 'id': 'CWb2lApN-MvcmzdPp_9jpA',
        'name': 'Tacos El Compa Taqueria',
        'location': {
            'address1': '1321 Blossom Hill Rd',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95118',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1321 Blossom Hill Rd', 'San Jose, CA 95118'],
        'lat': 37.2473719369747,
        'lng': -121.885735362849,
        'price': '$$',
        'phone': '+14086228035',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/G8VT83HQOczDzcJcbU7ohQ/o.jpg',
        'categories': ['mexican'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/G8VT83HQOczDzcJcbU7ohQ/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/CHagy7Y5SVNGRUnB1Z8o9Q/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/gvi9us2uOiBagDp75QrQSw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2030', 'day': 0}
    },
    {
        # 'id': 'vZ41QYMBQvtHgpAfw1IToQ',
        'name': 'Pizza Antica',
        'location': {
            'address1': '334 Santana Row',
            'address2': 'Ste 1065',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95128',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['334 Santana Row', 'Ste 1065', 'San Jose, CA 95128'],
        'lat': 37.3217489749968,
        'lng': -121.948049744656,
        'price': '$$',
        'phone': '+14085578373',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/HJpZ0j3hBEbUJVo5urlCvw/o.jpg',
        'categories': ['pizza'],
        'transactions': ['delivery', 'pickup'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/HJpZ0j3hBEbUJVo5urlCvw/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/SAFLQwI8uXeMqptjx54abw/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/4y1e4k_M3l0R22VDMF9TjA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1130', 'end': '2200', 'day': 0}
    },
    {
        # 'id': '7NOpkoAUAGqMKEZgSu1QmA',
        'name': 'A Slice of New York',
        'location': {
            'address1': '3443 Stevens Creek Blvd',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95117',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['3443 Stevens Creek Blvd', 'San Jose, CA 95117'],
        'lat': 37.3235243214913,
        'lng': -121.959063137967,
        'price': '$',
        'phone': '+14082475423',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/O0byts1kxDUO-I8mz_H01g/o.jpg',
        'categories': ['pizza'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/O0byts1kxDUO-I8mz_H01g/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/Kn8w6zIHWTOJq6drKO-SIQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/Ft4nSk8x726ZuJhhA2b2EA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2200', 'day': 1}
    },
    {
        # 'id': 'OGwQYjE3ThC_gF92mHO0_g',
        'name': 'Mendocino Farms',
        'location': {
            'address1': '3090 Olsen Dr',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95128',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['3090 Olsen Dr', 'San Jose, CA 95128'],
        'lat': 37.3190837,
        'lng': -121.9486391,
        'price': '$$',
        'phone': '+14082071390',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/P9NbNV8RSw33yfrwz2-OqQ/o.jpg',
        'categories': ['salad', 'sandwiches'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/P9NbNV8RSw33yfrwz2-OqQ/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/GweT6WttkF6aiv1smGRPLA/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/xjmKdOjhY9E45pT0k4dG9g/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'j1jgz10pCfC6T4k2WW3o9A',
        'name': 'Freshly Baked Eatery',
        'location': {
            'address1': '152 N 3rd St',
            'address2': 'Ste 101',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95112',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['152 N 3rd St', 'Ste 101', 'San Jose, CA 95112'],
        'lat': 37.33965279706127,
        'lng': -121.88947963521625,
        'price': '$$',
        'phone': '+14082989370',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/VYiF73PQgmiDGnY1smmxZw/o.jpg',
        'categories': ['sandwiches'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/VYiF73PQgmiDGnY1smmxZw/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/Y0LIh0TANe1JcVz-waiUpA/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/1RbxVJuiZ0M3y0yi9Scfog/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1030', 'end': '1430', 'day': 0}
    },
    {
        # 'id': 'tyr85X7PWdx54LOVzLzjAw',
        'name': 'Hannah Coffee',
        'location': {
            'address1': '754 The Alameda',
            'address2': 'Ste 80',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95126',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['754 The Alameda', 'Ste 80', 'San Jose, CA 95126'],
        'lat': 37.33160866072895,
        'lng': -121.90553722829216,
        'price': '$$',
        'phone': '+14089711207',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/3V1U4uWRngcW-nxqLx3b8g/o.jpg',
        'categories': ['coffee', 'sandwiches', 'breakfast_brunch'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/3V1U4uWRngcW-nxqLx3b8g/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/ruLtJXv-iHeucsG4J9FrWg/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/trO42uS0XyzmPbPiJBXI0A/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0700', 'end': '1400', 'day': 0}
    },
    {
        # 'id': 'zYljE3M9zSoZdipfFQidpA',
        'name': 'The Boiling Crab',
        'location': {
            'address1': '1631 E Capitol Expy',
            'address2': 'Ste 101',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95121',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1631 E Capitol Expy', 'Ste 101', 'San Jose, CA 95121'],
        'lat': 37.30656,
        'lng': -121.81228,
        'price': '$$',
        'phone': '+14085326147',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/pLF4cC32yHOTNxsEfl4BAw/o.jpg',
        'categories': ['seafood'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/pLF4cC32yHOTNxsEfl4BAw/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/d5APn2G0aeRZnFhQbDliKA/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/acvDtomGm7X-8eFvHWnbAw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1500', 'end': '2200', 'day': 0}
    },
    {
        # 'id': 'QJJd1N0QjQgUtv4hIuhqGg',
        'name': 'Taurinus Brazilian Steakhouse',
        'location': {
            'address1': '167 W San Fernando St',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95113',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['167 W San Fernando St', 'San Jose, CA 95113'],
        'lat': 37.333145,
        'lng': -121.892216,
        'price': '$$$$',
        'phone': '+14082940110',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/gUqj6xQJgOWcRFbTYKWEWg/o.jpg',
        'categories': ['brazilian', 'steak', 'bars'],
        'transactions': ['pickup', 'restaurant_reservation', 'delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/gUqj6xQJgOWcRFbTYKWEWg/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/o-qqj1qtxLE8-AP2d3oPxQ/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/aFECGUXqoTfNW_7CRKVyQw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1700', 'end': '2030', 'day': 1}
    },
    {
        # 'id': '3eKhFdXHvne3_YVjxfrTGQ',
        'name': 'Fogo de Chao Brazilian Steakhouse',
        'location': {
            'address1': '377 Santana Row',
            'address2': 'Ste 1090',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95128',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['377 Santana Row', 'Ste 1090', 'San Jose, CA 95128'],
        'lat': 37.3202585632998,
        'lng': -121.949787738762,
        'price': '$$$',
        'phone': '+14082447001',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/DWFemT5KPCv36LW1MUnpDw/o.jpg',
        'categories': ['brazilian', 'steak'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/DWFemT5KPCv36LW1MUnpDw/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/_gsirD5coR8O9cnl3FyqGg/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/Yb1TbOmjsXvKyrOnTCJ3qg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1130', 'end': '1400', 'day': 0}
    },
    {
        # 'id': 'PoqyugcuH71tkEwXnDcmYQ',
        'name': 'Mizu Sushi Bar & Grill',
        'location': {
            'address1': '1035 S Winchester Blvd',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95128',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1035 S Winchester Blvd', 'San Jose, CA 95128'],
        'lat': 37.30805,
        'lng': -121.95056,
        'price': '$$',
        'phone': '+14082607200',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/5zAyA6ZdjuzX3q9151dXcA/o.jpg',
        'categories': ['sushi', 'japanese', 'korean'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/5zAyA6ZdjuzX3q9151dXcA/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/bpKzmTL4N346bJFYF78Z8Q/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/3KVHFOj-IzIBGvPI5qzHhg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1130', 'end': '1400', 'day': 0}
    },
    {
        # 'id': '73WEetznHbLA6sp0k9rzQA',
        'name': 'Thai Elephant Express',
        'location': {
            'address1': '3005 Silver Creek Rd',
            'address2': 'Ste 128',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95121',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['3005 Silver Creek Rd', 'Ste 128', 'San Jose, CA 95121'],
        'lat': 37.30873594670218,
        'lng': -121.81343910770782,
        'price': '$$',
        'phone': '+14085288882',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/Fu01CqQLcWxAl8aLCYgi3g/o.jpg',
        'categories': ['thai'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/Fu01CqQLcWxAl8aLCYgi3g/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/DcBquQMO8sAAQOL9d0i31A/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/OtaOryhNtqMafBn8VGF5Fg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2100', 'day': 1}
    },
    {
        # 'id': '_cHIFoV6mqqOfnjNnHr0bQ',
        'name': 'Must be Thai',
        'location': {
            'address1': '3143 Stevens Creek Blvd',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95117',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['3143 Stevens Creek Blvd', 'San Jose, CA 95117'],
        'lat': 37.32387,
        'lng': -121.9515,
        'price': '$$',
        'phone': '+14088167179',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/cPIIVOJBN08LaAKpiGIXog/o.jpg',
        'categories': ['thai'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/cPIIVOJBN08LaAKpiGIXog/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/XnN_kl8yWBTlzZd2QIIUow/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/Llr_BXhr4gGgZDbXsiBUpQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2100', 'day': 0}
    },
    {
        # 'id': '7juJxsuoqYvWa9om6EcxsQ',
        'name': 'Bun Bo Hue An Nam',
        'location': {
            'address1': '740 Story Rd',
            'address2': 'Ste 3',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95122',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['740 Story Rd', 'Ste 3', 'San Jose, CA 95122'],
        'lat': 37.32861,
        'lng': -121.85831,
        'price': '$$',
        'phone': '+14089931755',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/OZBoPDu7WTqhiMpGH451eg/o.jpg',
        'categories': ['vietnamese', 'soup'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/OZBoPDu7WTqhiMpGH451eg/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/5O99FNvJPJecmpMJixBI3Q/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/dcfWuNsFLM3pIknbz394lg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0900', 'end': '2100', 'day': 0}
    },
    {
        # 'id': '6hCYuX14SeyJIuHXdp3AhA',
        'name': 'Tofoo Com Chay',
        'location': {
            'address1': '388 E Santa Clara St',
            'address2': '',
            'address3': '',
            'city': 'San Jose',
            'zip_code': '95113',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['388 E Santa Clara St', 'San Jose, CA 95113'],
        'lat': 37.3399585,
        'lng': -121.8822796,
        'price': '$',
        'phone': '+14082866335',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/o3zKzoXheca_yGtIgNcG_w/o.jpg',
        'categories': ['vietnamese'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/o3zKzoXheca_yGtIgNcG_w/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/EayUCDFbDR3Nm_3HrxPXjQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/pYiL_s4Fx38njsoWmsSvuA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0900', 'end': '1800', 'day': 0}
    },
    {
        # 'id': 'PkLfjhJ_XExjwARO1RkQIw',
        'name': 'Bakesale Betty',
        'location': {
            'address1': '5098 Telegraph Ave',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94609',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '51st St & 49th St'
        },
        'address': ['5098 Telegraph Ave', 'Oakland, CA 94609'],
        'lat': 37.837041785668,
        'lng': -122.26217067875,
        'price': '$$',
        'phone': '+15109851213',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/pYQzgOSURwB5SYzgaf-PxQ/o.jpg',
        'categories': ['bakeries', 'sandwiches', 'tradamerican'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/pYQzgOSURwB5SYzgaf-PxQ/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/QQHIsBY4q9Pw_4ci9XDuMw/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/-fYVXmWzyqULRei59R2yog/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1030', 'end': '1400', 'day': 3}
    },
    {
        # 'id': 'Qfc4w5l92Uvq9BsrP15O4A',
        'name': 'Arizmendi Bakery',
        'location': {
            'address1': '3265 Lakeshore Ave',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94610',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Lake Park Ave & Trestle Glen Rd'
        },
        'address': ['3265 Lakeshore Ave', 'Oakland, CA 94610'],
        'lat': 37.8106889,
        'lng': -122.2448111,
        'price': '$',
        'phone': '+15102688849',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/psuH6qtkRl3j3UiJyFnxng/o.jpg',
        'categories': ['bakeries', 'pizza', 'coffee'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/psuH6qtkRl3j3UiJyFnxng/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/L2-9HTKXhrv1_51QjPLtgQ/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/Xl6ONENmIm-XiHBKyXpYLw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0800', 'end': '2000', 'day': 1}
    },
    {
        # 'id': 'kIM6q7OiC_olzruHoVMMSw',
        'name': 'Yokee Milk Tea',
        'location': {
            'address1': '1728 Franklin St',
            'address2': 'Ste A',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94612',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '19th St & 17th St'
        },
        'address': ['1728 Franklin St', 'Ste A', 'Oakland, CA 94612'],
        'lat': 37.8063683,
        'lng': -122.2681935,
        'price': '$$',
        'phone': '+15108363288',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/69KpX11ti3F4JpjusqfrEg/o.jpg',
        'categories': ['bubbletea', 'juicebars'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/69KpX11ti3F4JpjusqfrEg/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/eTwcgnhF9RjeZzsmSPNIZA/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/l32xs6itEhydAmcHHD-FdQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '1800', 'day': 0}
    },
    {
        # 'id': 'Y4JaDkuGs8Xk_dPZu02e2g',
        'name': 'UC Dessert',
        'location': {
            'address1': '388 9th St',
            'address2': 'Ste 159',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94607',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Webster St & Franklin St'
        },
        'address': ['388 9th St', 'Ste 159', 'Oakland, CA 94607'],
        'lat': 37.80046369370517,
        'lng': -122.27176016691539,
        'price': '$$',
        'phone': '+15109228857',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/2N6nlYGP3CI2w1nQj29gFA/o.jpg',
        'categories': ['desserts', 'bubbletea'],
        'transactions': ['delivery', 'pickup'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/2N6nlYGP3CI2w1nQj29gFA/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/3kjJa7AlZt02Fn0XV6lCHQ/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/8CvOcDl9UuGAqkWKXyOXMg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1200', 'end': '2200', 'day': 0}
    },
    {
        # 'id': 'CIrXV1DVcW9LmwINg4bH6A',
        'name': 'La Farine',
        'location': {
            'address1': '6323 College Ave',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94618',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '63rd St'
        },
        'address': ['6323 College Ave', 'Oakland, CA 94618'],
        'lat': 37.8506143,
        'lng': -122.2525786,
        'price': '$',
        'phone': '+15106540338',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/6NSTStM4EUNJFH1eUyKtBQ/o.jpg',
        'categories': ['bakeries', 'coffee'],
        'transactions': [],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/6NSTStM4EUNJFH1eUyKtBQ/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/BTnA3wsOAwl433Fm0O8fXA/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/S9WWzmslX4dYAdChJST7gg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0700', 'end': '1800', 'day': 0}
    },
    {
        # 'id': 'ACQxcER6RDR2NOLVu0DHEg',
        'name': 'Fentons Creamery',
        'location': {
            'address1': '4226 Piedmont Ave',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94611',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Glenwood Ave & Ridgeway Ave'
        },
        'address': ['4226 Piedmont Ave', 'Oakland, CA 94611'],
        'lat': 37.8278770446777,
        'lng': -122.250015258789,
        'price': '$$',
        'phone': '+15106587000',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/Qdj1bqEiVuxnWe-WL9a0FA/o.jpg',
        'categories': ['icecream', 'tradamerican', 'desserts'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/Qdj1bqEiVuxnWe-WL9a0FA/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/eB7S9ypz-QZoXyUXTQiGpg/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/iJyFgrmVxJm7X2Msl5u0OA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2200', 'day': 0}
    },
    {
        # 'id': 'cgImAqtrpVg7hN_6lsFJrQ',
        'name': 'Farmhouse Kitchen Thai Cuisine',
        'location': {
            'address1': '336 Water St',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94607',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['336 Water St', 'Oakland, CA 94607'],
        'lat': 37.794215,
        'lng': -122.275465,
        'price': '$$$',
        'phone': '+15104190541',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/htkVpfws9qBrWZgkoLrtEg/o.jpg',
        'categories': ['thai', 'cocktailbars', 'desserts'],
        'transactions': ['delivery', 'restaurant_reservation'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/htkVpfws9qBrWZgkoLrtEg/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/mJoSrX6X42mxFsfQxiUv4Q/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/qDC84iAyIplZE2b0w-cy4A/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '1330', 'day': 0}
    },
    {
        # 'id': 'hfVYUuJRS7Q4rgNVHCB0Rg',
        'name': 'Colonial Donuts',
        'location': {
            'address1': '3318 Lakeshore Ave',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94610',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Lake Park Ave & Trestle Glen Rd'
        },
        'address': ['3318 Lakeshore Ave', 'Oakland, CA 94610'],
        'lat': 37.81059,
        'lng': -122.24366,
        'price': '$',
        'phone': '+15108932503',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/wSH7Sd0XvyUb7AAzusnCrw/o.jpg',
        'categories': ['donuts', 'coffee', 'newamerican'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/wSH7Sd0XvyUb7AAzusnCrw/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/9JEkxj6QauYqbu2c0Isuvw/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/Uv7YNUxvTLllld75ttH_Ag/o.jpg'
        ],
        'hours': {'is_overnight': True, 'start': '0000', 'end': '0000', 'day': 0}
    },
    {
        # 'id': 'EMCfTcgvGlItfrPNBEgb9A',
        'name': 'Flavor Brigade',
        'location': {
            'address1': '3540 Fruitvale Ave',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94602',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Macarthur Blvd & Coloma St'
        },
        'address': ['3540 Fruitvale Ave', 'Oakland, CA 94602'],
        'lat': 37.8008344,
        'lng': -122.2157816,
        'price': '$',
        'phone': '+15104791672',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/eHI6taQ1ALYgOjh4vEf6Ng/o.jpg',
        'categories': ['icecream', 'desserts'],
        'transactions': ['delivery', 'pickup'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/eHI6taQ1ALYgOjh4vEf6Ng/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/9UBPn75Z0NnvNx3OEH6Y0w/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/X1T2Lj3y6HN88YolcyO6kA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1200', 'end': '2000', 'day': 0}
    },
    {
        # 'id': 'a9NgquuCzte0YT7M9VpLeA',
        'name': 'Modigliani Cafe',
        'location': {
            'address1': '3208-3210 Grand Ave',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94610',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['3208-3210 Grand Ave', 'Oakland, CA 94610'],
        'lat': 37.8115099,
        'lng': -122.2476793,
        'price': '$$',
        'phone': '+15109861599',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/l-eDG9nXbzPdoTyd0bDPhg/o.jpg',
        'categories': ['juicebars', 'cafes'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/l-eDG9nXbzPdoTyd0bDPhg/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/-xUpcLgdoY8GrUs9X22Siw/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/NmLOr6Fhncxa4TfVZ-pNyA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '1500', 'day': 0}
    },
    {
        # 'id': 'NQVqMCoY-Krhw8DY4UnJKw',
        'name': 'Ohgane Korean BBQ',
        'location': {
            'address1': '3915 Broadway',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94611',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '38th St & 40th St'
        },
        'address': ['3915 Broadway', 'Oakland, CA 94611'],
        'lat': 37.82721,
        'lng': -122.25735,
        'price': '$$$',
        'phone': '+15105948300',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/SThvsH-vqyk76dpyhyEnRA/o.jpg',
        'categories': ['korean', 'bbq'],
        'transactions': ['pickup'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/SThvsH-vqyk76dpyhyEnRA/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/GGZZFfKoHPHSlulAKO-FMA/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/sCA6pBGo50Jk5CrbXtLpMA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2130', 'day': 0}
    },
    {
        # 'id': '_mFhusiDiacM8w-7Hea5bg',
        'name': 'Jong Ga House',
        'location': {
            'address1': '372 Grand Ave',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94610',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Staten Ave & Ellita Ave'
        },
        'address': ['372 Grand Ave', 'Oakland, CA 94610'],
        'lat': 37.8089712,
        'lng': -122.2547232,
        'price': '$$',
        'phone': '+15104447658',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/krIokJ-WUcFXSER1QBgXIw/o.jpg',
        'categories': ['korean', 'bbq'],
        'transactions': ['pickup', 'restaurant_reservation', 'delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/krIokJ-WUcFXSER1QBgXIw/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/wMdbnZungmpqVkSxW05XcQ/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/f96wOkCSpwHviMDT4Jo6dQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2300', 'day': 0}
    },
    {
        # 'id': 'oQ2M416FwdHc9NRKDeCHng',
        'name': 'Portal Oakland',
        'location': {
            'address1': '1611 2nd Ave',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94606',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '16th St & Foothill Blvd'
        },
        'address': ['1611 2nd Ave', 'Oakland, CA 94606'],
        'lat': 37.7993046,
        'lng': -122.2546307,
        'price': '$$',
        'phone': '+15106637678',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/fxxIrqjzDNzQWC1qU78K5A/o.jpg',
        'categories': ['newamerican', 'breakfast_brunch', 'burgers'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/fxxIrqjzDNzQWC1qU78K5A/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/PJ3zdDDoq5-Mo-mViFpurw/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/36XqJ4m0xuLk-cGAOq_N_w/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'Jiz82V_WXIfZf02AuSSvDA',
        'name': 'Chop Bar',
        'location': {
            'address1': '190 4th St',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94607',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Madison St & Jackson St'
        },
        'address': ['190 4th St', 'Oakland, CA 94607'],
        'lat': 37.795275493551486,
        'lng': -122.26928717501382,
        'price': '$$',
        'phone': '+15108342467',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/amWKwEq3RO0WHHcl2cdXIw/o.jpg',
        'categories': ['newamerican', 'breakfast_brunch', 'cocktailbars'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/amWKwEq3RO0WHHcl2cdXIw/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/gHmZnJlwAhg71EOTMMtq_w/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/GkfcMHnNlk9au3xJfhOOAw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1130', 'end': '2130', 'day': 0}
    },
    {
        # 'id': 'nnjQ8m6oTbQbr5_zUhCiDQ',
        'name': 'Souley Vegan',
        'location': {
            'address1': '301 Broadway',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94607',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '3rd St'
        },
        'address': ['301 Broadway', 'Oakland, CA 94607'],
        'lat': 37.79702,
        'lng': -122.2761,
        'price': '$$',
        'phone': '+15109221615',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/qbuzOt1ng6XIqjqk3d8oaA/o.jpg',
        'categories': ['vegan', 'salad', 'burgers'],
        'transactions': ['delivery', 'pickup'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/qbuzOt1ng6XIqjqk3d8oaA/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/6r4YTSgHzOsTW0BaDYqw8A/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/Hq68935x6CkQVxS9LzCt7A/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2100', 'day': 1}
    },
    {
        # 'id': 'Ah9cWAseDdJ6WxO-TveJKg',
        'name': 'TrueBurger',
        'location': {
            'address1': '146 Grand Ave',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94612',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Valdez St & Harrison St'
        },
        'address': ['146 Grand Ave', 'Oakland, CA 94612'],
        'lat': 37.811351769499,
        'lng': -122.264015827435,
        'price': '$$',
        'phone': '+15102085678',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/tPEkRuz9cLXArpW54_9TFA/o.jpg',
        'categories': ['burgers'],
        'transactions': ['pickup'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/tPEkRuz9cLXArpW54_9TFA/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/-F9vx2YucLEq3_DdRjGjsA/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/-BMIQHS7jQEmip8B9kvSnA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'wo68vP1Y0iXNS-n6i8WpjQ',
        'name': 'Luckyduck Bicycle Cafe',
        'location': {
            'address1': '302 12th St',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94607',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Harrison St & Webster St'
        },
        'address': ['302 12th St', 'Oakland, CA 94607'],
        'lat': 37.8017726,
        'lng': -122.268675,
        'price': '$$',
        'phone': '+15108911830',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/I6nxC_Q99RT565ihkGFRFg/o.jpg',
        'categories': ['cafes', 'breakfast_brunch'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/I6nxC_Q99RT565ihkGFRFg/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/FVTLG1O2kwld9Br1boYvzg/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/JsNvGguJYOCQxTSzuOlfsA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0800', 'end': '1700', 'day': 1}
    },
    {
        # 'id': 'LHd3X9Of8ymOE5X3_fd0eA',
        'name': 'Moo Bong Ri Korean Restaurant',
        'location': {
            'address1': '4390 Telegraph Ave',
            'address2': 'Ste K',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94609',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '44th St & 43rd St'
        },
        'address': ['4390 Telegraph Ave', 'Ste K', 'Oakland, CA 94609'],
        'lat': 37.832094781567775,
        'lng': -122.2630403,
        'price': '$$',
        'phone': '+15106544606',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/f4YO5vOAi5H6_KN0z0Wr6w/o.jpg',
        'categories': ['korean', 'soup', 'chicken_wings'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/f4YO5vOAi5H6_KN0z0Wr6w/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/QveTDWoWpAOfE7v0G7plYQ/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/9B5DrFIp8i8OHU9dpfwjSg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '1430', 'day': 0}
    },
    {
        # 'id': '1aQn5XzAk_lVwxn997fphQ',
        'name': 'Mua',
        'location': {
            'address1': '2442 Webster St',
            'address2': 'Ste A',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94612',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '24th St & 25th St'
        },
        'address': ['2442 Webster St', 'Ste A', 'Oakland, CA 94612'],
        'lat': 37.8140830993652,
        'lng': -122.264350891113,
        'price': '$$',
        'phone': '+15102381100',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/jvB918DDMpyEyZfcPefCqg/o.jpg',
        'categories': ['bars', 'newamerican', 'chicken_wings'],
        'transactions': ['delivery', 'restaurant_reservation'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/jvB918DDMpyEyZfcPefCqg/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/dGPz_1qk0wCGgZFM6qEOqg/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/pHVMgkJojSZZOiOcP8PLcw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1700', 'end': '2200', 'day': 1}
    },
    {
        # 'id': 'wu596lAazmcSqAxrSqCpkw',
        'name': 'Huangcheng Noodle House',
        'location': {
            'address1': '911 Washington St',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94607',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '10th St & 9th St'
        },
        'address': ['911 Washington St', 'Oakland, CA 94607'],
        'lat': 37.80151958623863,
        'lng': -122.27464153967905,
        'price': '$$',
        'phone': '+17024813124',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/FjYlGWWvayMltY855e6JLw/o.jpg',
        'categories': ['chinese', 'noodles'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/FjYlGWWvayMltY855e6JLw/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/agdO12Lko9UmhDtXTjd9Rw/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/s_w29r92w3JnZbvSvglwYQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1000', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'DceTpSF9RJ9PBvfX-_EImQ',
        'name': 'Shandong Restaurant',
        'location': {
            'address1': '328 10th St',
            'address2': 'Ste 101',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94607',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Webster St & Harrison St'
        },
        'address': ['328 10th St', 'Ste 101', 'Oakland, CA 94607'],
        'lat': 37.800607171031,
        'lng': -122.26986193448,
        'price': '$$',
        'phone': '+15108392299',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/DKHAlj5Mpqs1HjZt36XsDg/o.jpg',
        'categories': ['chinese', 'seafood', 'noodles'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/DKHAlj5Mpqs1HjZt36XsDg/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/pEesHevaSJ9txbagz5xNRA/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/4UYQChtTCwGfVqXN0bJK6A/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '1500', 'day': 1}
    },
    {
        # 'id': 'JMVfRgQ-Rz6m3KWx9lFveQ',
        'name': 'Mariposa Baking Company',
        'location': {
            'address1': '5427 Telegraph Ave',
            'address2': 'Unit D3',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94609',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '55th St'
        },
        'address': ['5427 Telegraph Ave', 'Unit D3', 'Oakland, CA 94609'],
        'lat': 37.8398772799042,
        'lng': -122.262391602516,
        'price': '$$',
        'phone': '+15105950955',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/F0ggrzJ4U43WFNx5eivXhQ/o.jpg',
        'categories': ['bakeries', 'gluten_free', 'sandwiches'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/F0ggrzJ4U43WFNx5eivXhQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/rHN5HYrCfc0YbPXzqBUBdQ/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/ySpyqSe55rWQUl0zgL3g3g/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0900', 'end': '1700', 'day': 0}
    },
    {
        # 'id': '4a-VV_CbVMZQ8Wh4yfXT3g',
        'name': 'Obelisco Restaurant',
        'location': {
            'address1': '3411 E 12th St',
            'address2': 'Ste 110',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94601',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '35th Ave & 34th Ave'
        },
        'address': ['3411 E 12th St', 'Ste 110', 'Oakland, CA 94601'],
        'lat': 37.77538,
        'lng': -122.22394,
        'price': '$$',
        'phone': '+15105343752',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/IqncY3XNqD4sJyvdVFC4-w/o.jpg',
        'categories': ['mexican', 'gluten_free', 'vegetarian'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/IqncY3XNqD4sJyvdVFC4-w/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/YHByLeD4Zyab_3Qo5sabuA/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/4sxitVQ9wrZtElaTBntkHw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '1800', 'day': 0}
    },
    {
        # 'id': 'l1MROfbSETysLQQH1N3PIQ',
        'name': 'In-N-Out Burger',
        'location': {
            'address1': '8300 Oakport St',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94621',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['8300 Oakport St', 'Oakland, CA 94621'],
        'lat': 37.740369,
        'lng': -122.198397,
        'price': '$',
        'phone': '+18007861000',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/ZwTYLnJSgN68aBYzlWPlKg/o.jpg',
        'categories': ['burgers', 'hotdogs'],
        'transactions': [],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/ZwTYLnJSgN68aBYzlWPlKg/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/S9wiVbR6zdXm9oZk9p1knw/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/ZqyPbCIeBiUtChKCbKC9WQ/o.jpg'
        ],
        'hours': {'is_overnight': True, 'start': '1030', 'end': '0100', 'day': 0}
    },
    {
        # 'id': 'Q8jV2uPiBtI_FNys6mbcoQ',
        'name': "Ahn's Quarter Pound Burger",
        'location': {
            'address1': '439 Grand Ave',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94610',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Bellevue Ave & Staten Ave'
        },
        'address': ['439 Grand Ave', 'Oakland, CA 94610'],
        'lat': 37.8083442889045,
        'lng': -122.253061495721,
        'price': '$$',
        'phone': '+15107634328',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/4Rl2-o-baPrJOL_KRTJbWA/o.jpg',
        'categories': ['burgers', 'hotdogs'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/4Rl2-o-baPrJOL_KRTJbWA/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/F6Q3fE0YffaMDQwHv-_YBw/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/xv5ZS0HmVh7pT0Bww7TkkA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0800', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'XusKnltuKs9LTfAMCCxyPg',
        'name': 'Biryani Tika Kabab',
        'location': {
            'address1': '328 14th St',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94612',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Webster St & Harrison St'
        },
        'address': ['328 14th St', 'Oakland, CA 94612'],
        'lat': 37.8034,
        'lng': -122.26813,
        'price': '$$',
        'phone': '+15102388883',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/0B9tjZ8TLEctNPoLr2CA-g/o.jpg',
        'categories': ['indpak'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/0B9tjZ8TLEctNPoLr2CA-g/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/bTcOTW61lu1dJUoBXPYp4g/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/1mMWdKMzm0LeMa2JZBEWCw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2130', 'day': 0}
    },
    {
        # 'id': 'edcwzFKHIDpvS7Rj9gvU6Q',
        'name': 'Annapurna Restaurant and Bar',
        'location': {
            'address1': '948 Clay St',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94607',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '10th St & 9th St'
        },
        'address': ['948 Clay St', 'Oakland, CA 94607'],
        'lat': 37.80225,
        'lng': -122.27521,
        'price': '$$',
        'phone': '+15102509696',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/pN7g4cBXXiMktbNbBv1w2Q/o.jpg',
        'categories': ['indpak'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/pN7g4cBXXiMktbNbBv1w2Q/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/tR8rx5BTFj9ef-rZamMR-g/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/BohW5eZ3ONHS8qHELtdvMw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2130', 'day': 1}
    },
    {
        # 'id': 'a34HvdlrG5GZ1wjRuzRvlQ',
        'name': 'Pizzaiolo',
        'location': {
            'address1': '5008 Telegraph Ave',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94609',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '51st St & 49th St'
        },
        'address': ['5008 Telegraph Ave', 'Oakland, CA 94609'],
        'lat': 37.8366743827411,
        'lng': -122.262249116147,
        'price': '$$',
        'phone': '+15106524888',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/U8qzpZwDpWu2k4e1GSrW9g/o.jpg',
        'categories': ['italian', 'pizza', 'breakfast_brunch'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/U8qzpZwDpWu2k4e1GSrW9g/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/-GWQQOfI0QP4d7vcUMhbAA/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/P04h2Bx_MwNqe9W5ptTxiA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1700', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'v7GH_fTmGQGbjB4ignVnqA',
        'name': 'Belotti Ristorante E Bottega',
        'location': {
            'address1': '5403 College Ave',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94618',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Hudson St & Kales Ave'
        },
        'address': ['5403 College Ave', 'Oakland, CA 94618'],
        'lat': 37.840277044258,
        'lng': -122.251473292708,
        'price': '$$',
        'phone': '+15107887890',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/VMTMYgW0Kqc7okc9HPz6ZQ/o.jpg',
        'categories': ['italian', 'cocktailbars'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/VMTMYgW0Kqc7okc9HPz6ZQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/tWsqQIExh7PewZUdtH7ayA/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/b-XWEpab8k0Dble7SXXLCA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1130', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'UNE7QP_zp7oPnyqZcQkZiw',
        'name': 'Marufuku Ramen - Oakland',
        'location': {
            'address1': '4828 Telegraph Ave',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94609',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '48th St & 49th St'
        },
        'address': ['4828 Telegraph Ave', 'Oakland, CA 94609'],
        'lat': 37.835159813672,
        'lng': -122.262654751539,
        'price': '$$',
        'phone': '+15108232416',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/Us0JSHIU9lhTY3cKlOMuFg/o.jpg',
        'categories': ['ramen'],
        'transactions': ['delivery', 'pickup'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/Us0JSHIU9lhTY3cKlOMuFg/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/B-JVMUs4Nl7NXJT-4k57vg/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/9SFSucCYBJsGzmP0gsYkhA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1730', 'end': '2230', 'day': 0}
    },
    {
        # 'id': 'NqSVQ_DJZpVmCbJHaFcIsQ',
        'name': 'Geta',
        'location': {
            'address1': '165 41st St',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94611',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Piedmont Ave & Howe St'
        },
        'address': ['165 41st St', 'Oakland, CA 94611'],
        'lat': 37.82658,
        'lng': -122.25293,
        'price': '$$',
        'phone': '+15106534643',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/vRR7honMw5Nz5gqnAm6Xgw/o.jpg',
        'categories': ['japanese', 'sushi'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/vRR7honMw5Nz5gqnAm6Xgw/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/cnkEI5NrttJQJA7FMwKLNw/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/cTqCsr75ImEC2IsVm7s5WA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1130', 'end': '1400', 'day': 1}
    },
    {
        # 'id': '53BGTRdv8vnn6lwjMsjDUw',
        'name': "Wally's Cafe",
        'location': {
            'address1': '3900 San Pablo Ave',
            'address2': '',
            'address3': '',
            'city': 'Emeryville',
            'zip_code': '94608',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Yerba Buena Ave'
        },
        'address': ['3900 San Pablo Ave', 'Emeryville, CA 94608'],
        'lat': 37.8301438,
        'lng': -122.279408,
        'price': '$$',
        'phone': '+15105971303',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/zZs-nmJXFfIm2CRJFrpFiw/o.jpg',
        'categories': ['mediterranean'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/zZs-nmJXFfIm2CRJFrpFiw/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/2UlPab0LnPrZXpJ1lciuOw/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/y3VuOvTfCv-PWZzQwrr2bA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'jToTQStksqPPbcinvUqhlA',
        'name': 'Shakewell',
        'location': {
            'address1': '3407 Lakeshore Ave',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94610',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Longridge Rd & Trestle Glen Rd'
        },
        'address': ['3407 Lakeshore Ave', 'Oakland, CA 94610'],
        'lat': 37.8113694419706,
        'lng': -122.24299026164636,
        'price': '$$',
        'phone': '+15102510329',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/VlJ0xziaXK_vu67ryJ4OAA/o.jpg',
        'categories': ['bars', 'mediterranean'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/VlJ0xziaXK_vu67ryJ4OAA/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/HdPaQ7W4V9AmnRR6SN0Veg/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/9PneOd-ShTNXkJgrkGrusQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1630', 'end': '2100', 'day': 1}
    },
    {
        # 'id': 'PGJbyscmFcjFwQdrSDkoJg',
        'name': 'Tacos Sinaloa',
        'location': {
            'address1': '2138 International Blvd',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94606',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['2138 International Blvd', 'Oakland, CA 94606'],
        'lat': 37.78496,
        'lng': -122.2379,
        'price': '$',
        'phone': '+15105351206',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/bLvn1UlTwMg1sfl3C1b_HA/o.jpg',
        'categories': ['tacos'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/bLvn1UlTwMg1sfl3C1b_HA/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/lRBFJ7NnJRFYErmgW9WSIA/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/DkotgGpel_NPS6tDth085Q/o.jpg'
        ],
        'hours': {'is_overnight': True, 'start': '0900', 'end': '0100', 'day': 0}
    },
    {
        # 'id': 'UHFjEP5dVn4wqcjt7ByUog',
        'name': 'Cholita Linda',
        'location': {
            'address1': '4923 Telegraph Ave',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94609',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '51st St & 49th St'
        },
        'address': ['4923 Telegraph Ave', 'Oakland, CA 94609'],
        'lat': 37.8364704,
        'lng': -122.2625152,
        'price': '$$',
        'phone': '+15106792423',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/wVh5vn0PoNi8OhfEOjMo2A/o.jpg',
        'categories': ['latin', 'sandwiches', 'tacos'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/wVh5vn0PoNi8OhfEOjMo2A/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/Hdqxyis9kmVL9CFRloa67g/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/F0FiooJ4uilQMio1nkINXA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2200', 'day': 0}
    },
    {
        # 'id': 'JsqK99Ka8gIgu1ZtzDupRg',
        'name': "Zachary's Chicago Pizza",
        'location': {
            'address1': '5801 College Ave',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94618',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Chabot Rd & Oak Grove Ave'
        },
        'address': ['5801 College Ave', 'Oakland, CA 94618'],
        'lat': 37.846393,
        'lng': -122.252132,
        'price': '$$',
        'phone': '+15106556385',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/Wb0SdHS4sW6w_FJyPk5dTg/o.jpg',
        'categories': ['pizza'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/Wb0SdHS4sW6w_FJyPk5dTg/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/wqxsULWroEeV1kIy9PO01g/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/akTKIsCT0H6rVbCt6PibYA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2100', 'day': 0}
    },
    {
        # 'id': '6iT-NihtnFnDh8JOYxRvDQ',
        'name': 'Belly',
        'location': {
            'address1': '1901 San Pablo Ave',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94612',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'William St & 19th St'
        },
        'address': ['1901 San Pablo Ave', 'Oakland, CA 94612'],
        'lat': 37.80918,
        'lng': -122.27319,
        'price': '$$',
        'phone': '+15108390000',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/5KDrb-5QZ_dqfcXoZCVwLg/o.jpg',
        'categories': ['salad'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/5KDrb-5QZ_dqfcXoZCVwLg/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/jjZBMSIYbwju5jIIcyYiIA/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/4bdBl5wXfumHd5K4nrIlQw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'PGGtbjr8m4V54tWMgqYxmQ',
        'name': 'Marica',
        'location': {
            'address1': '5301 College Ave',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94618',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Hudson St & Manila Ave'
        },
        'address': ['5301 College Ave', 'Oakland, CA 94618'],
        'lat': 37.83798,
        'lng': -122.2517,
        'price': '$$',
        'phone': '+15109858388',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/QdNHCZg-4TyGCleKvMRX3w/o.jpg',
        'categories': ['seafood', 'newamerican'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/QdNHCZg-4TyGCleKvMRX3w/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/Io-8plfnPTTU_OCx1ChCQA/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/DumP47W52KNEshB5Vxj-ew/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1600', 'end': '2100', 'day': 1}
    },
    {
        # 'id': 'oT08T3Vpn1I7jDmrBBRMTw',
        'name': 'House of Prime Rib',
        'location': {
            'address1': '1906 Van Ness Ave',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94109',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1906 Van Ness Ave', 'San Francisco, CA 94109'],
        'lat': 37.79338,
        'lng': -122.4225,
        'price': '$$$',
        'phone': '+14158854605',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/HLrjaMoAgYSac0vx71YpCA/o.jpg',
        'categories': ['tradamerican', 'steak'],
        'transactions': [],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/HLrjaMoAgYSac0vx71YpCA/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/pBewcPxzGqOQCoqFg7OSiw/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/3S2Kl9ZOS0icGjiwcHRWMw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1700', 'end': '2200', 'day': 0}
    },
    {
        # 'id': 'E6OLQ9i9A3iS0tKI8qJK6g',
        'name': 'Galeto Brazilian Steakhouse',
        'location': {
            'address1': '1019 Clay St',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94607',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '11th St & 10th St'
        },
        'address': ['1019 Clay St', 'Oakland, CA 94607'],
        'lat': 37.80307,
        'lng': -122.27532,
        'price': '$$$',
        'phone': '+15102389388',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/rjhLkMmq4jgQkhkuuGv9yA/o.jpg',
        'categories': ['brazilian', 'steak'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/rjhLkMmq4jgQkhkuuGv9yA/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/5WZsQqwGxcjVxpJtODThXQ/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/tq7MbAAAz1VJPQQtOr_hVw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1700', 'end': '2100', 'day': 1}
    },
    {
        # 'id': '9-V4vgu2lJQ7FLrLu8lJjA',
        'name': 'Shimizu Sushi',
        'location': {
            'address1': '4290 Piedmont Ave',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94611',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Glenwood Ave & Echo Ave'
        },
        'address': ['4290 Piedmont Ave', 'Oakland, CA 94611'],
        'lat': 37.828493,
        'lng': -122.249325,
        'price': '$$',
        'phone': '+15106537672',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/iPeG-Io7Q546MfwsJHtAWg/o.jpg',
        'categories': ['japanese', 'sushi'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/iPeG-Io7Q546MfwsJHtAWg/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/NeuLCcu1geViWzA-KrNgsg/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/EME2CoDSTvNc7LO2cQKEGw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1600', 'end': '2030', 'day': 0}
    },
    {
        # 'id': 'Jlt5w5ItA8ugiXif2VVQ5g',
        'name': 'Champa Garden',
        'location': {
            'address1': '2102 8th Ave',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94606',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '21st St & 10th St'
        },
        'address': ['2102 8th Ave', 'Oakland, CA 94606'],
        'lat': 37.7981399,
        'lng': -122.2446,
        'price': '$$',
        'phone': '+15102388819',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/sAclWPVcRqkoQTXUlnjZXw/o.jpg',
        'categories': ['thai'],
        'transactions': ['delivery', 'pickup'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/sAclWPVcRqkoQTXUlnjZXw/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/WEJ9rYtkgJRnPFvkltZZpw/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/MJ2a5D-vyjOXNc8RuvTDrw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '1500', 'day': 0}
    },
    {
        # 'id': 'xrfNNIUAl2588mwyRtvH-w',
        'name': 'Golden Lotus Vegan Restaurant',
        'location': {
            'address1': '1301 Franklin St',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94612',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '13th St & 14th St'
        },
        'address': ['1301 Franklin St', 'Oakland, CA 94612'],
        'lat': 37.80348,
        'lng': -122.2705,
        'price': '$$',
        'phone': '+15108930383',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/zMca0ARV2trIyazPwztVOA/o.jpg',
        'categories': ['vegetarian', 'vietnamese', 'vegan'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/zMca0ARV2trIyazPwztVOA/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/tRASaO4i4bMz3FfKHJ_NIQ/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/eaP_n-4M-VW12oLHXkNcfg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2000', 'day': 1}
    },
    {
        # 'id': 'dHurSbFlqasZZdxVdNjayA',
        'name': 'Dimond Slice Pizza',
        'location': {
            'address1': '2208 MacArthur Blvd',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94602',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Fruitvale Ave & Champion St'
        },
        'address': ['2208 MacArthur Blvd', 'Oakland, CA 94602'],
        'lat': 37.80063,
        'lng': -122.21572,
        'price': '$',
        'phone': '+15108428773',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/ztuojQWoMF8wOrECEgYSNA/o.jpg',
        'categories': ['pizza', 'vegetarian'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/ztuojQWoMF8wOrECEgYSNA/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/Gvd5B08jSXSpHvEmzcqJvg/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/E4HNL0jfCNs_zgvgPDl85Q/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2000', 'day': 1}
    },
    {
        # 'id': 'L6WsyFVf9UahURn0Fudsbg',
        'name': 'Monster Pho',
        'location': {
            'address1': '360 40th St',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94609',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Opal St & Manila Ave'
        },
        'address': ['360 40th St', 'Oakland, CA 94609'],
        'lat': 37.82844,
        'lng': -122.25811,
        'price': '$$',
        'phone': '+15107884459',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/XbU4av3rYZ6rZ1nH4RnmbQ/o.jpg',
        'categories': ['vietnamese', 'soup', 'noodles'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/XbU4av3rYZ6rZ1nH4RnmbQ/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/l5gDNfB1uS153yIfcPIXJw/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/eZya1xvTVUd_sEosGWCO7g/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2000', 'day': 2}
    },
    {
        # 'id': 'IJF-4E8Mhm5teI5RHrH5yw',
        'name': 'Banh Mi Ba Le',
        'location': {
            'address1': '1909 International Blvd',
            'address2': '',
            'address3': '',
            'city': 'Oakland',
            'zip_code': '94606',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1909 International Blvd', 'Oakland, CA 94606'],
        'lat': 37.78606,
        'lng': -122.24101,
        'price': '$',
        'phone': '+15102619800',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/QhBrxaQVLBfLJhN4zU_MGg/o.jpg',
        'categories': ['vietnamese', 'sandwiches'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/QhBrxaQVLBfLJhN4zU_MGg/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/Vhr9d-McWYCiSoS6CSUBmg/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/qSSCg9THTtEO7h_M-28_qw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0730', 'end': '1500', 'day': 4}
    },
    {
        # 'id': '2XQm-uFcTS7oc8MFP-8olA',
        'name': 'B Patisserie',
        'location': {
            'address1': '2821 California St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94115',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Divisadero St & Broderick St'
        },
        'address': ['2821 California St', 'San Francisco, CA 94115'],
        'lat': 37.787873,
        'lng': -122.440882,
        'price': '$$',
        'phone': '+14154401700',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/bSlfEG1tlBtL6_n2_gIxjg/o.jpg',
        'categories': ['bakeries'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/bSlfEG1tlBtL6_n2_gIxjg/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/FK7xOOI-MowNBi4jFb21fg/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/c9hNm5WqemXnyMWXZSFBPQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0800', 'end': '1600', 'day': 2}
    },
    {
        # 'id': 'ri7UUYmx21AgSpRsf4-9QA',
        'name': 'Tartine Bakery',
        'location': {
            'address1': '600 Guerrero St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94110',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '19th St & 18th St'
        },
        'address': ['600 Guerrero St', 'San Francisco, CA 94110'],
        'lat': 37.76131,
        'lng': -122.42431,
        'price': '$$',
        'phone': '+14154872600',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/QRbC0TQ2zxTKXHt5NfpFCw/o.jpg',
        'categories': ['bakeries', 'cafes', 'desserts'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/QRbC0TQ2zxTKXHt5NfpFCw/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/_poQka9cZ-CzxWR0BNvcVQ/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/4lEDYdjdF0P-beJD8M9sJw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0800', 'end': '1700', 'day': 0}
    },
    {
        # 'id': 'V6L23CJAM9cm0zzWAhSwVA',
        'name': 'Belly Good Cafe & Crepes',
        'location': {
            'address1': '1737 Post St',
            'address2': 'Ste 393',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94115',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Webster St & Buchanan St'
        },
        'address': ['1737 Post St', 'Ste 393', 'San Francisco, CA 94115'],
        'lat': 37.785091,
        'lng': -122.430635,
        'price': '$',
        'phone': '+14153468383',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/qnsiyxylkTv5_Dcp_bi6Xg/o.jpg',
        'categories': ['icecream', 'bubbletea'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/qnsiyxylkTv5_Dcp_bi6Xg/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/EAE0ZvcSqwvO4Is6LFx4rg/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/C8VCRYvRe2XxivOgUwpcBQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1200', 'end': '1800', 'day': 0}
    },
    {
        # 'id': 'sSiUcnbwPQ4ssHY3EMV0Fw',
        'name': 'Matcha Cafe Maiko',
        'location': {
            'address1': '1581 Webster St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94115',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Post St & Geary Blvd'
        },
        'address': ['1581 Webster St', 'San Francisco, CA 94115'],
        'lat': 37.785051,
        'lng': -122.432095,
        'price': '$',
        'phone': '+14157570919',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/PG3nGYrtolcjKrxqlamvEQ/o.jpg',
        'categories': ['coffee', 'icecream', 'bubbletea'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/PG3nGYrtolcjKrxqlamvEQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/vyMkGIQKirBsjyME9cpvgQ/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/XmZLWn17TTp_hZhl_NXSTQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1130', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'aVskw5NKrs7ibAQ54E_bZw',
        'name': 'U :Dessert Story',
        'location': {
            'address1': '3489 16th St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94114',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Dehon St & Sanchez St'
        },
        'address': ['3489 16th St', 'San Francisco, CA 94114'],
        'lat': 37.7642642124321,
        'lng': -122.430517340788,
        'price': '$$',
        'phone': '+14157963633',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/gyIGiApFYGt_paOKgfbhxQ/o.jpg',
        'categories': ['desserts', 'coffee'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/gyIGiApFYGt_paOKgfbhxQ/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/FFvrEmgRuJtp090BTuBhBA/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/o-wu6nVt71ksXMimACyQsQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1500', 'end': '2200', 'day': 0}
    },
    {
        # 'id': 'b-ylC7pGKuh4yw6l1Q1k9g',
        'name': 'Golden Bear Trading Company',
        'location': {
            'address1': '1401 6th Ave',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94122',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Kirkham St & Judah St'
        },
        'address': ['1401 6th Ave', 'San Francisco, CA 94122'],
        'lat': 37.7621609,
        'lng': -122.463128,
        'price': '$$',
        'phone': '+14156645574',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/iQLrkk1vA1k1wfWXgk2xWQ/o.jpg',
        'categories': ['coffee'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/iQLrkk1vA1k1wfWXgk2xWQ/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/Gonhw7GEznSm7mmNXyuUYg/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/mqhdQZJnqoyuICKNYfUspg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0900', 'end': '2000', 'day': 0}
    },
    {
        # 'id': 'ttarnopezxmp2ROB1N2PaA',
        'name': 'Nopa',
        'location': {
            'address1': '560 Divisadero St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94117',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Fell St & Hayes St'
        },
        'address': ['560 Divisadero St', 'San Francisco, CA 94117'],
        'lat': 37.77483,
        'lng': -122.43746,
        'price': '$$$',
        'phone': '+14158648643',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/QOc_docjeCrDHlckTaDE2A/o.jpg',
        'categories': ['newamerican', 'desserts', 'cocktailbars'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/QOc_docjeCrDHlckTaDE2A/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/VF5PAA7ALdcjv0K1kx7ocg/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/yrB1ghsnmlISCIgIP44jGQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1730', 'end': '2200', 'day': 0}
    },
    {
        # 'id': 'GXu3PD4IPsxIHpo011aydg',
        'name': "Bob's Donuts & Pastry Shop",
        'location': {
            'address1': '1621 Polk St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94109',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Sacramento St & Clay St'
        },
        'address': ['1621 Polk St', 'San Francisco, CA 94109'],
        'lat': 37.791883,
        'lng': -122.4212,
        'price': '$',
        'phone': '+14157763141',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/NbXrMs9bEMJ1biVlLJgzXw/o.jpg',
        'categories': ['bakeries', 'donuts'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/NbXrMs9bEMJ1biVlLJgzXw/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/5O_75b1Dcudw7m35P_nE_A/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/1e0ZRRk5zRsksNJdeXZfKw/o.jpg'
        ],
        'hours': {'is_overnight': True, 'start': '0600', 'end': '0600', 'day': 0}
    },
    {
        # 'id': 'LFEBCjZ-M3XUFJDszYFX6A',
        'name': 'Milkbomb Ice Cream',
        'location': {
            'address1': '1717 17th St',
            'address2': 'Ste 105',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94103',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'De Haro St & Carolina St'
        },
        'address': ['1717 17th St', 'Ste 105', 'San Francisco, CA 94103'],
        'lat': 37.764788631805,
        'lng': -122.40119110172758,
        'price': '$$',
        'phone': '+14159034281',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/-7nJ9aFof1GMUUh2C21S9Q/o.jpg',
        'categories': ['icecream', 'donuts'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/-7nJ9aFof1GMUUh2C21S9Q/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/q5uBbbDYifVYDo3UIyoqVQ/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/QVnGPD8FdcSDtvjBweJJ0w/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1715', 'end': '2100', 'day': 4}
    },
    {
        # 'id': 'wGl_DyNxSv8KUtYgiuLhmA',
        'name': 'Bi-Rite Creamery',
        'location': {
            'address1': '3692 18th St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94110',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Dolores St & Oakwood St'
        },
        'address': ['3692 18th St', 'San Francisco, CA 94110'],
        'lat': 37.761591,
        'lng': -122.425717,
        'price': '$$',
        'phone': '+14156265600',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/c5-w8mU45PHJZveEz_wZ6Q/o.jpg',
        'categories': ['icecream'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/c5-w8mU45PHJZveEz_wZ6Q/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/k4ild0zOWGDOe-skHQ-Nug/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/1ZdpEThwJB7RC1vkMRyHMw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1200', 'end': '2100', 'day': 0}
    },
    {
        # 'id': '76smcUUGRvq3k1MVPUXbnA',
        'name': 'Mitchells Ice Cream',
        'location': {
            'address1': '688 San Jose Ave',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94110',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Valley St & 29th St'
        },
        'address': ['688 San Jose Ave', 'San Francisco, CA 94110'],
        'lat': 37.744221,
        'lng': -122.422791,
        'price': '$',
        'phone': '+14156482300',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/f4lzrsfJLSd4CW1-LWmO2w/o.jpg',
        'categories': ['icecream'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/f4lzrsfJLSd4CW1-LWmO2w/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/ayAdfgE4AS3be9YRinpZpg/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/s_U57TNuKZWo0lRXonYkJw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2300', 'day': 0}
    },
    {
        # 'id': 'ww-HKAff5xmQbiXgO-KcSQ',
        'name': 'Golden Era Vegan Restaurant',
        'location': {
            'address1': '395 Golden Gate Ave',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94102',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Larkin St'
        },
        'address': ['395 Golden Gate Ave', 'San Francisco, CA 94102'],
        'lat': 37.7814734450825,
        'lng': -122.416835837066,
        'price': '$$',
        'phone': '+14154878687',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/62yYvcZqOoVbRy31ms2FGQ/o.jpg',
        'categories': ['vegan', 'vietnamese', 'juicebars'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/62yYvcZqOoVbRy31ms2FGQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/95phTYOnHkeODb5t3UzRwQ/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/c9RUaXyjHxdpKbILjudzhA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '1930', 'day': 0}
    },
    {
        # 'id': 'QCQ3WN7hd9xMPs2_ycHa_A',
        'name': 'Broken Record',
        'location': {
            'address1': '1166 Geneva Ave',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94112',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Edinburgh St & Naples St'
        },
        'address': ['1166 Geneva Ave', 'San Francisco, CA 94112'],
        'lat': 37.71426,
        'lng': -122.437,
        'price': '$$',
        'phone': '+14159631713',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/tCfiqhwdx7x7LYQIUQky0A/o.jpg',
        'categories': ['tradamerican', 'bbq'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/tCfiqhwdx7x7LYQIUQky0A/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/axNRCPDqPIxpKIxcD2S9ww/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/l1VhLka_ALa6Zul5RDZM9g/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1600', 'end': '0000', 'day': 0}
    },
    {
        # 'id': 'eBxkmr-hJ2KgpZQzEO3ArQ',
        'name': 'Han Il Kwan',
        'location': {
            'address1': '1802 Balboa St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94121',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '19th Ave & 20th Ave'
        },
        'address': ['1802 Balboa St', 'San Francisco, CA 94121'],
        'lat': 37.776719,
        'lng': -122.478278,
        'price': '$$',
        'phone': '+14157524447',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/rWMhKj9EU_TcmhJMUz602Q/o.jpg',
        'categories': ['korean', 'bbq'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/rWMhKj9EU_TcmhJMUz602Q/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/kzoVbSFA1SwKp4atb15yFg/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/xfztI9awqFx8SRl9L_7vjA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2000', 'day': 0}
    },
    {
        # 'id': 'lJAGnYzku5zSaLnQ_T6_GQ',
        'name': "Brenda's French Soul Food",
        'location': {
            'address1': '652 Polk St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94102',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Turk St & Eddy St'
        },
        'address': ['652 Polk St', 'San Francisco, CA 94102'],
        'lat': 37.7829016035273,
        'lng': -122.419043442957,
        'price': '$$',
        'phone': '+14153458100',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/VJ865E7ULQWSNjKhNG57VQ/o.jpg',
        'categories': ['breakfast_brunch'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/VJ865E7ULQWSNjKhNG57VQ/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/sTjgTEXukJKTw2NACCZWnw/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/LY6X6ZCbPXXXl3bNggF_NQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0800', 'end': '2000', 'day': 0}
    },
    {
        # 'id': '-DrR38H1Abk0wCyu9XOLug',
        'name': 'Sweet Maple',
        'location': {
            'address1': '2101 Sutter St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94115',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Steiner St & Pierce St'
        },
        'address': ['2101 Sutter St', 'San Francisco, CA 94115'],
        'lat': 37.785735681426,
        'lng': -122.43507770852,
        'price': '$$',
        'phone': '+14156559169',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/etyS0Af-PS74CTwxly2uoA/o.jpg',
        'categories': ['tradamerican', 'breakfast_brunch', 'burgers'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/etyS0Af-PS74CTwxly2uoA/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/T1tZZwm2PwFoUKKjQ1HCeA/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/vtaxO-dhXjo-s6GLjiRUVw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0800', 'end': '1430', 'day': 0}
    },
    {
        # 'id': 'UTVDbZv-qiHU06sDkoel3g',
        'name': 'Chez Maman East',
        'location': {
            'address1': '1401 18th St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94107',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Connecticut St & Missouri St'
        },
        'address': ['1401 18th St', 'San Francisco, CA 94107'],
        'lat': 37.762463,
        'lng': -122.396712,
        'price': '$$',
        'phone': '+14156559542',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/gccHe5ofFMpNyh8vmS0VSw/o.jpg',
        'categories': ['french', 'burgers'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/gccHe5ofFMpNyh8vmS0VSw/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/okMaW8m3E_QMcIoJua2Qmw/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/AEhvPPMlhf8H6hrERpymzg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1130', 'end': '2200', 'day': 0}
    },
    {
        # 'id': 'WhTpALYvB4ZBMcT8fFVLvw',
        'name': 'Holy Gelato!',
        'location': {
            'address1': '1392 9th Ave',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94122',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Irving St & Judah St'
        },
        'address': ['1392 9th Ave', 'San Francisco, CA 94122'],
        'lat': 37.762392,
        'lng': -122.465941,
        'price': '$$',
        'phone': '+14156813061',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/MiNFmR2UdeU6sQCyoc0raQ/o.jpg',
        'categories': ['juicebars'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/MiNFmR2UdeU6sQCyoc0raQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/r21fI8R8Qd7D9PlIIyy_Tw/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/5Y3NuIe4gxf8RvE_XhFD4g/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1130', 'end': '2130', 'day': 0}
    },
    {
        # 'id': 'bUr4iq2mKKiBOu2HKynylg',
        'name': 'HRD',
        'location': {
            'address1': '521A 3rd St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94107',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Taber Aly & Park Ave'
        },
        'address': ['521A 3rd St', 'San Francisco, CA 94107'],
        'lat': 37.7811065758548,
        'lng': -122.395329724426,
        'price': '$$',
        'phone': '+14155432355',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/G05B7mvYPHBpGu1wP1NK_Q/o.jpg',
        'categories': ['cafes', 'tradamerican'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/G05B7mvYPHBpGu1wP1NK_Q/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/ZwhS1OSqTCVsLQHqPyPcng/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/cSoZpB3abCuVLb8S9uMhPg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '1500', 'day': 0}
    },
    {
        # 'id': 'M0JTO3oyu6gxh1mfFjU-dA',
        'name': 'San Tung',
        'location': {
            'address1': '1031 Irving St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94122',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '12th Ave & 11th Ave'
        },
        'address': ['1031 Irving St', 'San Francisco, CA 94122'],
        'lat': 37.76378306790313,
        'lng': -122.46900735179602,
        'price': '$$',
        'phone': '+14152420828',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/rYZbin0NWrbrs0TYzI8rYA/o.jpg',
        'categories': ['chinese', 'chicken_wings', 'noodles'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/rYZbin0NWrbrs0TYzI8rYA/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/36vpZ6_gwQdrKUT86uNBzw/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/GNpK6AivZ8IjlYXztqLWhg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '1500', 'day': 0}
    },
    {
        # 'id': 'NwqdohySKrDnK0RsAde9UA',
        'name': 'Hot Sauce and Panko',
        'location': {
            'address1': '1468 Hyde St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94109',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Washington St & Jackson St'
        },
        'address': ['1468 Hyde St', 'San Francisco, CA 94109'],
        'lat': 37.794505,
        'lng': -122.417957,
        'price': '$',
        'phone': '+14153591908',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/gqkZBrUjvBDkDUr3ByNO7Q/o.jpg',
        'categories': ['chicken_wings', 'waffles', 'sandwiches'],
        'transactions': ['delivery', 'pickup'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/gqkZBrUjvBDkDUr3ByNO7Q/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/iaH_Vk9f3aCyFsdCIUFSAg/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/ufI5DlPOIjikLEXg8OHGKQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1130', 'end': '1900', 'day': 2}
    },
    {
        # 'id': '-sg6DqQNGyTMt0MHoY7diQ',
        'name': 'Good Mong Kok Bakery',
        'location': {
            'address1': '1039 Stockton St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94108',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Jackson St & Washington St'
        },
        'address': ['1039 Stockton St', 'San Francisco, CA 94108'],
        'lat': 37.7954584839809,
        'lng': -122.408358365012,
        'price': '$',
        'phone': '+14153972688',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/H-6n1U4Z6f5MmT9rQPdOaA/o.jpg',
        'categories': ['bakeries', 'dimsum'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/H-6n1U4Z6f5MmT9rQPdOaA/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/abuR9bQKsdrb7HBfHY1siw/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/AN8M99z-hxosiA9Zi-dlvw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0700', 'end': '1800', 'day': 0}
    },
    {
        # 'id': 'ssI9ivccrDBT-RH_52fPBQ',
        'name': 'Greens Restaurant',
        'location': {
            'address1': '2 Marina Blvd',
            'address2': 'Bldg A',
            'address3': 'Fort Mason',
            'city': 'San Francisco',
            'zip_code': '94123',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Beach St & Buchanan St'
        },
        'address': [
            '2 Marina Blvd',
            'Bldg A',
            'Fort Mason',
            'San Francisco, CA 94123'
        ],
        'lat': 37.80668033302732,
        'lng': -122.43210032743212,
        'price': '$$$',
        'phone': '+14157716222',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/eKP-qx_qaKXcrsiNNxM6Ng/o.jpg',
        'categories': ['vegetarian', 'vegan', 'gluten_free'],
        'transactions': ['delivery', 'pickup'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/eKP-qx_qaKXcrsiNNxM6Ng/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/XGZqfWP-a_SER5qUYaX8rQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/jBju8P2c-G0Fpi3h6hsfYg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1130', 'end': '1430', 'day': 1}
    },
    {
        # 'id': 'Di4kb-1tnjP5OKFuV8qbUA',
        'name': 'Cordon Bleu',
        'location': {
            'address1': '1574 California St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94109',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Larkin St & Polk St'
        },
        'address': ['1574 California St', 'San Francisco, CA 94109'],
        'lat': 37.7907203,
        'lng': -122.4205111,
        'price': '$$',
        'phone': '+14156735637',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/Ltb4mT3eSOvKwKQ9Cc4vVw/o.jpg',
        'categories': ['vietnamese', 'hotdogs'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/Ltb4mT3eSOvKwKQ9Cc4vVw/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/8lZhLpfi6W_1CRSk19K2iQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/VH1krIPa-4QFFhTQ3nUDRA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1130', 'end': '1430', 'day': 1}
    },
    {
        # 'id': '_Iupdt0IslH_jU8zkKcWLA',
        'name': 'Pica Pica Arepa Kitchen',
        'location': {
            'address1': '401 Valencia St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94103',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '15th St & Sparrow St'
        },
        'address': ['401 Valencia St', 'San Francisco, CA 94103'],
        'lat': 37.76646996177495,
        'lng': -122.42190694110414,
        'price': '$$',
        'phone': '+14154005453',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/hAWS9IidumamHodFIUikIA/o.jpg',
        'categories': ['gluten_free', 'latin'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/hAWS9IidumamHodFIUikIA/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/YN5hYqzdY2A4POwF-Nc9zA/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/S7t3D145IDoOfeEvdmoesg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2000', 'day': 0}
    },
    {
        # 'id': 'gR9DTbKCvezQlqvD7_FzPw',
        'name': 'North India Restaurant',
        'location': {
            'address1': '123 Second St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94105',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['123 Second St', 'San Francisco, CA 94105'],
        'lat': 37.787789124691,
        'lng': -122.399305736113,
        'price': '$$',
        'phone': '+14153481234',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/_nJ2VTeTZe5-gePr8PXTxg/o.jpg',
        'categories': ['indpak'],
        'transactions': ['restaurant_reservation', 'pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/_nJ2VTeTZe5-gePr8PXTxg/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/W2oBBWPGm3bRYEuHKGMtCw/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/AHm5LPigScMuUG-bT9jqdw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1000', 'end': '2300', 'day': 0}
    },
    {
        # 'id': 'iUockw0CUssKZLyoGJYEXA',
        'name': 'Cuisine of Nepal',
        'location': {
            'address1': '3486 Mission St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94110',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Cortland Ave & Kingston St'
        },
        'address': ['3486 Mission St', 'San Francisco, CA 94110'],
        'lat': 37.74097,
        'lng': -122.42318,
        'price': '$$',
        'phone': '+14156472222',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/phc7I0SsJJFr1clrlh6Bhw/o.jpg',
        'categories': ['indpak'],
        'transactions': ['restaurant_reservation', 'pickup', 'delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/phc7I0SsJJFr1clrlh6Bhw/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/EBxDuYqCk5fQa_txrUx76g/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/4x67YaNc1R8EE51jZAkkWA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1600', 'end': '2200', 'day': 1}
    },
    {
        # 'id': 'PTFxtXS47ZVRCdZIrEWvGw',
        'name': 'Golden Boy Pizza',
        'location': {
            'address1': '542 Green St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94133',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Jasper Pl & Bannam Pl'
        },
        'address': ['542 Green St', 'San Francisco, CA 94133'],
        'lat': 37.7997956,
        'lng': -122.4080729,
        'price': '$',
        'phone': '+14159829738',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/SfosPh2iWkVTMC4LLVIL8g/o.jpg',
        'categories': ['pizza', 'italian'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/SfosPh2iWkVTMC4LLVIL8g/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/Fu6NkLQGlgmiOOr-vHbNPg/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/IqWF-Qn2EPdwkEDi4Y_lDA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1130', 'end': '2030', 'day': 0}
    },
    {
        # 'id': '8dUaybEPHsZMgr1iKgqgMQ',
        'name': 'Sotto Mare',
        'location': {
            'address1': '552 Green St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94133',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Columbus Ave & Stockton St'
        },
        'address': ['552 Green St', 'San Francisco, CA 94133'],
        'lat': 37.79979,
        'lng': -122.40834,
        'price': '$$',
        'phone': '+14153983181',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/o3hIcGLMxV_5ynxEjGWGrw/o.jpg',
        'categories': ['seafood', 'italian', 'bars'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/o3hIcGLMxV_5ynxEjGWGrw/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/qsKW1g6duc76aAatbv7OJA/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/u_kkGKarL_H5SX0JB1pQ0w/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1130', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'CYttYTEiQuhSfo3SEh79fA',
        'name': 'Shizen Vegan Sushi Bar & Izakaya',
        'location': {
            'address1': '370 14th St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94103',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Julian Ave & Stevenson St'
        },
        'address': ['370 14th St', 'San Francisco, CA 94103'],
        'lat': 37.768326,
        'lng': -122.421682,
        'price': '$$',
        'phone': '+14156785767',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/-1BWnyjrsDmTmXH_3wZl_w/o.jpg',
        'categories': ['sushi', 'vegan'],
        'transactions': ['restaurant_reservation'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/-1BWnyjrsDmTmXH_3wZl_w/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/txvWg3lI3NE_e0_KKVJlGw/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/VecBZXh1-r9XWpJ8oZPVVg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1700', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'i09UMzccKgyLwGYKDVP28w',
        'name': 'Surisan',
        'location': {
            'address1': '505 Beach St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94133',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Jones St & Leavenworth St'
        },
        'address': ['505 Beach St', 'San Francisco, CA 94133'],
        'lat': 37.80678,
        'lng': -122.41756,
        'price': '$$',
        'phone': '+14157718449',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/TRmQFBMztDCAlp_ol7IMbA/o.jpg',
        'categories': ['korean', 'newamerican', 'breakfast_brunch'],
        'transactions': ['pickup', 'delivery', 'restaurant_reservation'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/TRmQFBMztDCAlp_ol7IMbA/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/nlMI7so9SX7fDpg4bSJ6Pg/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/H9RW8ndVpGUupAJFUXrMYA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0900', 'end': '1400', 'day': 0}
    },
    {
        # 'id': 'u39mZEYojBiNic3lqKhPNw',
        'name': 'Tacorea',
        'location': {
            'address1': '809 Bush St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94108',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Taylor St & Mason St'
        },
        'address': ['809 Bush St', 'San Francisco, CA 94108'],
        'lat': 37.7897794,
        'lng': -122.410717,
        'price': '$$',
        'phone': '+14154848911',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/XCBggDPYWe2yvYvqqH0qnQ/o.jpg',
        'categories': ['mexican', 'korean', 'breakfast_brunch'],
        'transactions': [],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/XCBggDPYWe2yvYvqqH0qnQ/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/e8iHcgcnjfEnvsCiY1U1BA/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/PAGd6ir-lXeq7g1Pm1pC7A/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1130', 'end': '1430', 'day': 0}
    },
    {
        # 'id': 'n6L5VIGunR51-D55C-eYeQ',
        'name': 'Foreign Cinema',
        'location': {
            'address1': '2534 Mission St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94110',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '21st St & 22nd St'
        },
        'address': ['2534 Mission St', 'San Francisco, CA 94110'],
        'lat': 37.75637,
        'lng': -122.41925,
        'price': '$$$',
        'phone': '+14156487600',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/cw5y2LSOIE-EVNjKK_d7SQ/o.jpg',
        'categories': ['breakfast_brunch', 'mediterranean', 'cocktailbars'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/cw5y2LSOIE-EVNjKK_d7SQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/MBHXUoMKUtzyiZqjZZzt0g/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/jJucPns3xuTw9aUAFbbvqQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1700', 'end': '2130', 'day': 0}
    },
    {
        # 'id': 'PsY5DMHxa5iNX_nX0T-qPA',
        'name': 'Kokkari Estiatorio',
        'location': {
            'address1': '200 Jackson St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94111',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Front St & Battery St'
        },
        'address': ['200 Jackson St', 'San Francisco, CA 94111'],
        'lat': 37.796996,
        'lng': -122.399661,
        'price': '$$$',
        'phone': '+14159810983',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/FTQfPJubJEtYeyHqwAsVKw/o.jpg',
        'categories': ['mediterranean'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/FTQfPJubJEtYeyHqwAsVKw/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/9lneWjyZG5BnQYZP9JNnlw/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/qYjEM7ZmOtGFDY1uwFY4ZQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1130', 'end': '1430', 'day': 0}
    },
    {
        # 'id': 'JARsJVKLPgs_yC3cwDnp7g',
        'name': 'La Taqueria',
        'location': {
            'address1': '2889 Mission St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94110',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '24th St & 25th St'
        },
        'address': ['2889 Mission St', 'San Francisco, CA 94110'],
        'lat': 37.750876871204916,
        'lng': -122.4181822457381,
        'price': '$$',
        'phone': '+14152857117',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/7LqVKYVg2GdEFKI2CFL4cA/o.jpg',
        'categories': ['mexican'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/7LqVKYVg2GdEFKI2CFL4cA/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/lRRj9_qQ_m9yK_My5Wrmig/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/quJVkgOw_pf70_enWelldw/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2045', 'day': 2}
    },
    {
        # 'id': 'SGRmnarrNuVEsAjYdEoA0w',
        'name': 'El Farolito',
        'location': {
            'address1': '2779 Mission St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94110',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '24th St & 23rd St'
        },
        'address': ['2779 Mission St', 'San Francisco, CA 94110'],
        'lat': 37.75265,
        'lng': -122.41812,
        'price': '$',
        'phone': '+14158247877',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/2-Kc5B4gJjB5OSkbbFimQw/o.jpg',
        'categories': ['mexican'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/2-Kc5B4gJjB5OSkbbFimQw/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/MGMSLkZ5eDQBcsYtbJ6GIQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/jusgtdXIfMwUMZ1klPm2TA/o.jpg'
        ],
        'hours': {'is_overnight': True, 'start': '1000', 'end': '0145', 'day': 0}
    },
    {
        # 'id': 'mSMZJj2pFvttWLpcDmgrEA',
        'name': "Tony's Pizza Napoletana",
        'location': {
            'address1': '1570 Stockton St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94133',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Union St'
        },
        'address': ['1570 Stockton St', 'San Francisco, CA 94133'],
        'lat': 37.8003315377662,
        'lng': -122.409053979377,
        'price': '$$',
        'phone': '+14158359888',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/rrBlePEDLrbD27VVE0Ze2A/o.jpg',
        'categories': ['pizza', 'italian', 'cocktailbars'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/rrBlePEDLrbD27VVE0Ze2A/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/o0Qjp8vsB_OGpLH2x9MRdg/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/fyeHU9Usy5uBXj8HKoaclA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1200', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'yyi2GpG_p7TX7XAq_eHSZA',
        'name': 'Boudin',
        'location': {
            'address1': '160 Jefferson St',
            'address2': 'Bistro Boudin',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94133',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Taylor St & Mason St'
        },
        'address': ['160 Jefferson St', 'Bistro Boudin', 'San Francisco, CA 94133'],
        'lat': 37.808507,
        'lng': -122.4149047308367,
        'price': '$$',
        'phone': '+14153515561',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/rDVvWFk7tMGdphnF6tdHDw/o.jpg',
        'categories': ['bakeries', 'salad', 'sandwiches'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/rDVvWFk7tMGdphnF6tdHDw/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/tlf4x0IM56h8TfTmicOySQ/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/lQNsp_NshXlxstMiyFmJgg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1200', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'IJk76B-pTta_klpAZcpQdA',
        'name': "Lou's Cafe",
        'location': {
            'address1': '5017 Geary Blvd',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94118',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '14th Ave & 15th Ave'
        },
        'address': ['5017 Geary Blvd', 'San Francisco, CA 94118'],
        'lat': 37.78045,
        'lng': -122.47329246476227,
        'price': '$',
        'phone': '+14153794429',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/zjE21goq1XUXE3iFzlLSuA/o.jpg',
        'categories': ['coffee', 'sandwiches', 'salad'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/zjE21goq1XUXE3iFzlLSuA/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/9nOt46hEpppCsEnQWlCgwg/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/ctCa-MI10YOGXytR3qnO-g/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0800', 'end': '1900', 'day': 0}
    },
    {
        # 'id': '2hGIxgprREdBieylltWaRQ',
        'name': 'Limoncello',
        'location': {
            'address1': '1400 Sutter St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94109',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Sutter & Franklin '
        },
        'address': ['1400 Sutter St', 'San Francisco, CA 94109'],
        'lat': 37.7873184067081,
        'lng': -122.423591369312,
        'price': '$$',
        'phone': '+14156386361',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/RJMZfygsa2NiYFM2wPzT-w/o.jpg',
        'categories': ['sandwiches'],
        'transactions': ['delivery', 'pickup'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/RJMZfygsa2NiYFM2wPzT-w/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/RF1BRq53QGvA49eWdH7bhg/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/x9bk4mmVLqs2NkP0AWDMng/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0900', 'end': '2000', 'day': 0}
    },
    {
        # 'id': 'hqQoVK0vadOX7_4gN1sh3g',
        'name': 'Saigon Sandwich',
        'location': {
            'address1': '560 Larkin St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94102',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Eddy St & Turk St'
        },
        'address': ['560 Larkin St', 'San Francisco, CA 94102'],
        'lat': 37.7831519576568,
        'lng': -122.417318022037,
        'price': '$',
        'phone': '+14154745698',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/lE_HHijKAKt08JIeRHVh7w/o.jpg',
        'categories': ['vietnamese', 'sandwiches'],
        'transactions': ['delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/lE_HHijKAKt08JIeRHVh7w/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/9G1UNYxeLay6qcWF7bc4xQ/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/kcaDQeG2wR2hHSt3AbhWRQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0700', 'end': '1700', 'day': 0}
    },
    {
        # 'id': 'f-m7-hyFzkf0HSEeQ2s-9A',
        'name': 'Fog Harbor Fish House',
        'location': {
            'address1': '39 Pier',
            'address2': 'Ste a - 202',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94133',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['39 Pier', 'Ste a - 202', 'San Francisco, CA 94133'],
        'lat': 37.80898821475503,
        'lng': -122.41029651587517,
        'price': '$$',
        'phone': '+14159692010',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/by8Hh63BLPv_HUqRUdsp_w/o.jpg',
        'categories': ['seafood', 'cocktailbars'],
        'transactions': ['restaurant_reservation'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/by8Hh63BLPv_HUqRUdsp_w/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/cc5tnzyd03couTo7ReDGgQ/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/J5NJ8-gclvTMzVmp3OrckA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2100', 'day': 0}
    },
    {
        # 'id': 'ciEDsTWhajcdL3KuJqBRlw',
        'name': 'Espetus Churrascaria',
        'location': {
            'address1': '1686 Market St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94102',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Valencia St & Gough St'
        },
        'address': ['1686 Market St', 'San Francisco, CA 94102'],
        'lat': 37.7733327504928,
        'lng': -122.422131667494,
        'price': '$$$$',
        'phone': '+14155528792',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/F9G1pFFitfi9F4rJw_nrpQ/o.jpg',
        'categories': ['steak', 'latin', 'brazilian'],
        'transactions': ['delivery', 'restaurant_reservation'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/F9G1pFFitfi9F4rJw_nrpQ/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/HKuF_ZS37zgPxpyWZfFfrw/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/IVsVcYZBjQKJp-jC6L2dKg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1130', 'end': '1430', 'day': 0}
    },
    {
        # 'id': 'Xg-FyjVKAN70LO4u4Z1ozg',
        'name': 'Hog Island Oyster',
        'location': {
            'address1': '1 Ferry Bldg',
            'address2': '',
            'address3': 'Shop 11',
            'city': 'San Francisco',
            'zip_code': '94111',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': ''
        },
        'address': ['1 Ferry Bldg', 'Shop 11', 'San Francisco, CA 94111'],
        'lat': 37.795831,
        'lng': -122.393303,
        'price': '$$',
        'phone': '+14153917117',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/Kozd3NJMSaT6S3J2kYAc1g/o.jpg',
        'categories': ['seafood', 'raw_food'],
        'transactions': ['pickup'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/Kozd3NJMSaT6S3J2kYAc1g/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/ahmWdH7P0UIc4lM1c8zhcQ/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/BlG7QLi2mseijvxFnAb5yg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1100', 'end': '2000', 'day': 0}
    },
    {
        # 'id': 'cL0q9S4bqwpbAN9ZKh-Zeg',
        'name': 'Nara Restaurant & Sake Bar',
        'location': {
            'address1': '518 Haight St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94117',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Steiner St & Fillmore St'
        },
        'address': ['518 Haight St', 'San Francisco, CA 94117'],
        'lat': 37.7721665317965,
        'lng': -122.430675700307,
        'price': '$$',
        'phone': '+14156386124',
        'url': 'https://s3-media1.fl.yelpcdn.com/bphoto/7zzlpJKaC9bndjuo2UIr6g/o.jpg',
        'categories': ['japanese', 'sushi'],
        'transactions': ['delivery', 'pickup', 'restaurant_reservation'],
        'photos': [
            'https://s3-media1.fl.yelpcdn.com/bphoto/7zzlpJKaC9bndjuo2UIr6g/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/uNjLBm477BW8uNtr1mkgqw/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/Z4YjKFldnVVvTrL8uwfF4Q/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1700', 'end': '2300', 'day': 1}
    },
    {
        # 'id': '0mNzmmh1mrdh5Cpg2QUBiw',
        'name': 'Lapisara Eatery',
        'location': {
            'address1': '698 Post St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94109',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': 'Jones St & Ophir Aly'
        },
        'address': ['698 Post St', 'San Francisco, CA 94109'],
        'lat': 37.7878344,
        'lng': -122.4131853,
        'price': '$$',
        'phone': '+14156553556',
        'url': 'https://s3-media4.fl.yelpcdn.com/bphoto/KPAzk-Q-UM5YOdyVyE760A/o.jpg',
        'categories': ['breakfast_brunch', 'burgers', 'thai'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media4.fl.yelpcdn.com/bphoto/KPAzk-Q-UM5YOdyVyE760A/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/rIEZmapiR-kQaW9A1lMg2g/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/KWNfC-Bup2LRI4MQG1JEwA/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '0800', 'end': '1400', 'day': 0}
    },
    {
        # 'id': 'E2Ri3Uudb3ogKfWBJIIhRw',
        'name': 'Lokma',
        'location': {
            'address1': '1801 Clement St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94121',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '19th Ave & 20th Ave'
        },
        'address': ['1801 Clement St', 'San Francisco, CA 94121'],
        'lat': 37.78215,
        'lng': -122.47867,
        'price': '$$',
        'phone': '+14157026263',
        'url': 'https://s3-media2.fl.yelpcdn.com/bphoto/en_xi2jWWYDvctLCLZuxbw/o.jpg',
        'categories': ['mediterranean', 'breakfast_brunch', 'vegetarian'],
        'transactions': ['pickup', 'delivery'],
        'photos': [
            'https://s3-media2.fl.yelpcdn.com/bphoto/en_xi2jWWYDvctLCLZuxbw/o.jpg',
            'https://s3-media2.fl.yelpcdn.com/bphoto/zXC2yBqxOWD-sczA1IKP_Q/o.jpg',
            'https://s3-media3.fl.yelpcdn.com/bphoto/e9FM-U-GHRfJjZM_fBAstg/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1600', 'end': '2030', 'day': 0}
    },
    {
        # 'id': 'z9CN58fSrA46ggyb6OnCnQ',
        'name': 'Thanh Long',
        'location': {
            'address1': '4101 Judah St',
            'address2': '',
            'address3': '',
            'city': 'San Francisco',
            'zip_code': '94122',
            'country': 'US',
            'state': 'CA',
            'display_address': '',
            'cross_streets': '46th Ave & 47th Ave'
        },
        'address': ['4101 Judah St', 'San Francisco, CA 94122'],
        'lat': 37.76017,
        'lng': -122.50609,
        'price': '$$$',
        'phone': '+14156651146',
        'url': 'https://s3-media3.fl.yelpcdn.com/bphoto/GmQdyVpGOPf8ZwRhXz3xnA/o.jpg',
        'categories': ['seafood', 'vietnamese', 'noodles'],
        'transactions': ['restaurant_reservation', 'delivery'],
        'photos': [
            'https://s3-media3.fl.yelpcdn.com/bphoto/GmQdyVpGOPf8ZwRhXz3xnA/o.jpg',
            'https://s3-media4.fl.yelpcdn.com/bphoto/61sZZZPoL7VkbPKEepCAJg/o.jpg',
            'https://s3-media1.fl.yelpcdn.com/bphoto/gI4h3i_AY_CPrX7_HQW5wQ/o.jpg'
        ],
        'hours': {'is_overnight': False, 'start': '1645', 'end': '1945', 'day': 2}
    }
]

reviews = [
    {
        'biz_id': 1,
        'review_body': 'Yo this place was FIRE. \n' +
        '\n' +
        'Came here to get 2 dozen donuts for a work event and wow they were amazing. I tried the dulce de leche and the regular glazed and...',
        "rating": 5,
        'created_at': '2022-10-13 13:02:36'
    },
    {
        'biz_id': 1,
        'review_body': 'Do not need much intro as this is the place to be for some fancy donuts in LA! Line out the door early weekend by 9am. Lot is small, street parking hard but...',
        "rating": 5,
        'created_at': '2022-10-01 21:55:54'
    },
    {
        'biz_id': 1,
        'review_body': 'While I do not fear (for I am strong), the notion of fryers did give me pause. How relieved that I never did see them. Instead, I was presented with the...',
        "rating": 5,
        'created_at': '2022-08-12 14:27:06'
    },
    {
        'biz_id': 2,
        'review_body': 'Alcove Cafe provides that ideal escape after a hike around Griffith Park for brunch and coffee.\n' +
        '\n' +
        'The Alcove has and will always be a sentimental favorite of...',
        "rating": 4,
        'created_at': '2022-10-04 07:55:44'
    },
    {
        'biz_id': 2,
        'review_body': 'Last Saturday my mother and I had brunch(the peak time) at Al Cove. We were seated right away. And someone came to take our order. Our food was delicious as...',
        "rating": 1,
        'created_at': '2022-10-09 21:18:23'
    },
    {
        'biz_id': 2,
        'review_body': "It's good but they don't label any of the cakes in the case. when I asked for one of the cakes that I found on the menu, the person at the counter didn't...",
        "rating": 3,
        'created_at': '2022-10-01 20:43:34'
    },
    {
        'biz_id': 4,
        'review_body': 'This place with a parking lot made me happy, on the way I was thinking about what I would do if there was no place to stop, but thank God I found it.\n' +
        '\n' +
        '1....',
        "rating": 5,
        'created_at': '2022-08-30 12:55:22'
    },
    {
        'biz_id': 4,
        'review_body': 'We do big group orders from Berlins on 3rd, ALL the time for the office.\n' +
        'Food is great, no doubting that!\n' +
        'Ordering online is easy.\n' +
        'Parking can be a...',
        "rating": 4,
        'created_at': '2022-08-15 13:06:01'
    },
    {
        'biz_id': 4,
        'review_body': "I have eaten many doeners in Germany, but I'm no doener expert. I remember it was very good, but I'm not sure why/how it was good or what was inside. \n" +
        'So I...',
        "rating": 5,
        'created_at': '2022-07-16 19:29:49'
    },
    {
        'biz_id': 3,
        'review_body': 'Was craving wonton soup...\n' +
        '\n' +
        'Wonton soup 10/10 - the broth is light and clean, lots of noodles, filling shrimp wontons\n' +
        'Beef wrap 10/10 - delicious and...',
        "rating": 5,
        'created_at': '2022-10-02 15:45:44'
    },
    {
        'biz_id': 3,
        'review_body': "TL;DR: decent Taiwanese food, but it's expensive and definitely geared towards being approachable for Americans\n" +
        '\n' +
        "AMBIENCE: It's Silverlake, so a lot of...",
        "rating": 3,
        'created_at': '2022-10-09 23:04:40'
    },
    {
        'biz_id': 3,
        'review_body': 'Go for the vibe not the food. \n' +
        '\n' +
        'I saw the reviews and thought this place would be great, but it was mediocre at best. I ordered to go online and arrived 30...',
        "rating": 3,
        'created_at': '2022-10-03 12:08:44'
    },
    {
        'biz_id': 6,
        'review_body': "My FAVORITE soft serve ever!! If you're ever craving matcha, I would HIGHLY recommend Tea Master! Honda Plaza has parking, and there's so many good...",
        "rating": 5,
        'created_at': '2022-10-12 18:52:05'
    },
    {
        'biz_id': 6,
        'review_body': 'Having a love for all things matcha, plus being highly recommended by a few friends made it mandatory I stop by here to get my fix one super hot day while...',
        "rating": 5,
        'created_at': '2022-10-12 00:03:41'
    },
    {
        'biz_id': 6,
        'review_body': "A not so hidden gem in Little Tokyo! By far the best matcha soft serve I've had. It's rich and creamy, but not overly sweet. Just the perfect amount of...",
        "rating": 5,
        'created_at': '2022-10-09 12:35:01'
    },
    {
        'biz_id': 5,
        'review_body': 'Food was INCREDIBLE! And so much that I had leftovers to reheat: those yummy pancakes again the next day!',
        "rating": 5,
        'created_at': '2022-08-31 20:43:52'
    },
    {
        'biz_id': 5,
        'review_body': 'Great option for an American breakfast! Service and food were really good. \n' +
        '\n' +
        'Deft a place to come if you are super hungry.',
        "rating": 5,
        'created_at': '2022-10-09 12:54:00'
    },
    {
        'biz_id': 5,
        'review_body': "One of my favorite brunch spots in all of LA. If you're coming during the weekend be prepared to wait in line for about an hour. There is no parking here,...",
        "rating": 5,
        'created_at': '2022-10-04 14:45:37'
    },
    {
        'biz_id': 7,
        'review_body': 'Hum I bet it was great. As long as you like it be happy u 2 I know about it . I have been for a min . No need to lie or fake anymore .',
        "rating": 5,
        'created_at': '2022-09-17 18:06:09'
    },
    {
        'biz_id': 7,
        'review_body': 'Great pastries! I enjoy taking the blueberry and raspberries cake to my job they love it',
        "rating": 5,
        'created_at': '2022-08-31 19:02:07'
    },
    {
        'biz_id': 7,
        'review_body': "Didn't lasagna or the crème brûlée which was what I went there for. But overall I love going to Botega Louie",
        "rating": 4,
        'created_at': '2022-08-25 12:56:26'
    },
    {
        'biz_id': 8,
        'review_body': 'Delicious chocolate bread - croissant thing! Wish I could have ordered one of everything! \n' +
        '\n' +
        'Fast service. And well worth the trip. \n' +
        '\n' +
        "It's a pity that I...",
        "rating": 5,
        'created_at': '2022-10-11 11:16:47'
    },
    {
        'biz_id': 8,
        'review_body': 'The area was really cute and right in the heart of the Arts District. The food itself was tasty and filling but very overpriced for what you got. \n' +
        '\n' +
        'Eating...',
        "rating": 4,
        'created_at': '2022-10-08 20:40:48'
    },
    {
        'biz_id': 8,
        'review_body': 'Love the vibe and food selection in this place! The\n' +
        'Spanish Latte is very tasty and relaxing. They also have salads, sandwiches, egg dishes, cakes, bobas,...',
        "rating": 4,
        'created_at': '2022-10-04 17:36:20'
    },
    {
        'biz_id': 1,
        'review_body': 'Yo this place was FIRE. \n' +
        '\n' +
        'Came here to get 2 dozen donuts for a work event and wow they were amazing. I tried the dulce de leche and the regular glazed and...',
        "rating": 5,
        'created_at': '2022-10-13 13:02:36'
    },
    {
        'biz_id': 1,
        'review_body': 'Do not need much intro as this is the place to be for some fancy donuts in LA! Line out the door early weekend by 9am. Lot is small, street parking hard but...',
        "rating": 5,
        'created_at': '2022-10-01 21:55:54'
    },
    {
        'biz_id': 1,
        'review_body': 'While I do not fear (for I am strong), the notion of fryers did give me pause. How relieved that I never did see them. Instead, I was presented with the...',
        "rating": 5,
        'created_at': '2022-08-12 14:27:06'
    },
    {
        'biz_id': 10,
        'review_body': 'Really good doughnuts, but they should think of re-hiring, the workers that served me were short tempered and really rude.',
        "rating": 4,
        'created_at': '2022-09-19 18:17:54'
    },
    {
        'biz_id': 10,
        'review_body': 'O M G - so bomb I could cry! \n' +
        '\n' +
        "My boyfriend and I finished this donut in probably less than 2 minutes! I actually can't believe that this was a vegan donut....",
        "rating": 5,
        'created_at': '2022-10-04 11:18:54'
    },
    {
        'biz_id': 10,
        'review_body': 'All you need to know is these are absolutely incredible donuts. Are they a little overpriced? Sure. But the staff is always great and the donuts are always...',
        "rating": 5,
        'created_at': '2022-09-17 17:32:23'
    },
    {
        'biz_id': 6,
        'review_body': "My FAVORITE soft serve ever!! If you're ever craving matcha, I would HIGHLY recommend Tea Master! Honda Plaza has parking, and there's so many good...",
        "rating": 5,
        'created_at': '2022-10-12 18:52:05'
    },
    {
        'biz_id': 6,
        'review_body': 'Having a love for all things matcha, plus being highly recommended by a few friends made it mandatory I stop by here to get my fix one super hot day while...',
        "rating": 5,
        'created_at': '2022-10-12 00:03:41'
    },
    {
        'biz_id': 6,
        'review_body': "A not so hidden gem in Little Tokyo! By far the best matcha soft serve I've had. It's rich and creamy, but not overly sweet. Just the perfect amount of...",
        "rating": 5,
        'created_at': '2022-10-09 12:35:01'
    },
    {
        'biz_id': 12,
        'review_body': "This is some of the best ice cream I've ever had! and I can most closely compare it to Jeni's ice cream! Its creamy and rich and packed with flavor! They...",
        "rating": 5,
        'created_at': '2022-09-22 08:54:25'
    },
    {
        'biz_id': 12,
        'review_body': "REALLY good ice cream!  Have sampled ice cream at two locations, and only wish there was a location near me.  Actually, maybe not, as I'd want to go there...",
        "rating": 4,
        'created_at': '2022-09-25 21:00:38'
    },
    {
        'biz_id': 12,
        'review_body': 'Salt and Straw never dissapoints. Go and be excited  about the unique flavors, rich ice cream, and helpful staff. \n' +
        '\n' +
        'My favorite flavors are honey lavender...',
        "rating": 5,
        'created_at': '2022-09-05 15:58:15'
    },
    {
        'biz_id': 6,
        'review_body': "My FAVORITE soft serve ever!! If you're ever craving matcha, I would HIGHLY recommend Tea Master! Honda Plaza has parking, and there's so many good...",
        "rating": 5,
        'created_at': '2022-10-12 18:52:05'
    },
    {
        'biz_id': 6,
        'review_body': 'Having a love for all things matcha, plus being highly recommended by a few friends made it mandatory I stop by here to get my fix one super hot day while...',
        "rating": 5,
        'created_at': '2022-10-12 00:03:41'
    },
    {
        'biz_id': 6,
        'review_body': "A not so hidden gem in Little Tokyo! By far the best matcha soft serve I've had. It's rich and creamy, but not overly sweet. Just the perfect amount of...",
        "rating": 5,
        'created_at': '2022-10-09 12:35:01'
    },
    {
        'biz_id': 14,
        'review_body': "I'm not vegan, but had the opportunity to try this restaurant out while in DTLA. \n" +
        '\n' +
        'I was very impressed how delicious the plant based sausage was, the rice...',
        "rating": 5,
        'created_at': '2022-08-24 13:28:23'
    },
    {
        'biz_id': 14,
        'review_body': "After several visits to this place over th past several years, I figured it's time to write a review. \n" +
        '\n' +
        'Have ordered about everything on the menu, but...',
        "rating": 4,
        'created_at': '2022-10-04 17:55:05'
    },
    {
        'biz_id': 14,
        'review_body': "I like this place. But it's changed. The service is actually in good place compared to the pandemic. They got rid of the questionable servers. \n" +
        '\n' +
        'Problem now...',
        "rating": 2,
        'created_at': '2022-08-27 15:45:49'
    },
    {
        'biz_id': 16,
        'review_body': 'An update from over 9 years later....and boy is it a complete 180.\n' +
        '\n' +
        'Since its a smaller restaurant, the long wait time remains: be prepared for a wait at...',
        "rating": 5,
        'created_at': '2022-10-12 16:42:28'
    },
    {
        'biz_id': 16,
        'review_body': 'I was pleasantly surprised by this place. As a tourist, you really only know about Kang Ho Dong Baekjeong and Quarters. We were made aware of this place by...',
        "rating": 4,
        'created_at': '2022-10-12 12:26:45'
    },
    {
        'biz_id': 16,
        'review_body': "The husband and I couldn't figure out what we wanted for dinner while visiting LA, so we ended up going with Hae Jang Chon because we've been here several...",
        "rating": 3,
        'created_at': '2022-10-10 16:34:57'
    },
    {
        'biz_id': 15,
        'review_body': 'A classic ktown spot for kbbq. I usually get the beef combo here, but opted for pork instead last night for dinner. Beef usually cooks faster whereas pork...',
        "rating": 5,
        'created_at': '2022-10-08 09:02:01'
    },
    {
        'biz_id': 15,
        'review_body': 'We came here as backup because the line at Quarters was too long on a Sunday night. This is in a popping plaza on 6th street in Koreatown. \n' +
        '\n' +
        'The space at...',
        "rating": 4,
        'created_at': '2022-10-08 19:36:39'
    },
    {
        'biz_id': 15,
        'review_body': "Stilll a staple if your not looking for the AYCE cheap fix!!! Good quality over abundance and seriously y'all do the math and I think all would agree that...",
        "rating": 4,
        'created_at': '2022-10-05 06:49:56'
    },
    {
        'biz_id': 18,
        'review_body': 'I have never seen such a queue here in my whole life because they have so many customers. I also loved their attitude towards me and their delicious...',
        "rating": 5,
        'created_at': '2022-09-15 11:55:57'
    },
    {
        'biz_id': 18,
        'review_body': 'Republique is an absolute crowd pleaser for delicious breakfast and pastries in the most stunning restaurant. I always bring my friends from out of town...',
        "rating": 5,
        'created_at': '2022-10-07 23:45:03'
    },
    {
        'biz_id': 18,
        'review_body': 'The entire culinary experience was overall underwhelming, but vibe and service were beautiful.\n' +
        '\n' +
        'This place had been on my list to try for dinner for quite...',
        "rating": 3,
        'created_at': '2022-10-09 15:43:46'
    },
    {
        'biz_id': 19,
        'review_body': 'Was craving wonton soup...\n' +
        '\n' +
        'Wonton soup 10/10 - the broth is light and clean, lots of noodles, filling shrimp wontons\n' +
        'Beef wrap 10/10 - delicious and...',
        "rating": 5,
        'created_at': '2022-10-02 15:45:44'
    },
    {
        'biz_id': 19,
        'review_body': "TL;DR: decent Taiwanese food, but it's expensive and definitely geared towards being approachable for Americans\n" +
        '\n' +
        "AMBIENCE: It's Silverlake, so a lot of...",
        "rating": 3,
        'created_at': '2022-10-09 23:04:40'
    },
    {
        'biz_id': 19,
        'review_body': 'Go for the vibe not the food. \n' +
        '\n' +
        'I saw the reviews and thought this place would be great, but it was mediocre at best. I ordered to go online and arrived 30...',
        "rating": 3,
        'created_at': '2022-10-03 12:08:44'
    },
    {
        'biz_id': 20,
        'review_body': 'It was my first visit and actually all dishes are amazing!!!\n' +
        'Especially I loved their green curry!',
        "rating": 5,
        'created_at': '2022-09-22 15:57:27'
    },
    {
        'biz_id': 20,
        'review_body': 'Enthusiastic five stars! Authentic Thai dishes with the spice level to prove it (flavorful not oppressive in my opinion) plus a million zillion gluten free...',
        "rating": 5,
        'created_at': '2022-09-27 11:20:50'
    },
    {
        'biz_id': 20,
        'review_body': 'Hands down the best authentic Thai food I have ever had. Despite arriving at 9pm we were seated and served very quickly.\n' +
        '\n' +
        'You absolutely cannot go wrong...',
        "rating": 5,
        'created_at': '2022-09-26 09:39:31'
    },
        {
        'biz_id': 21,
        'review_body': 'The best place for vegan sushi hands down. \n' +
        "We ordered the chefs course. I don't know if that's what it's called.\n" +
        '\n' +
        'But it came with multiple pieces to allow...',
        "rating": 5,
        'created_at': '2022-10-01 13:43:54'
    },
    {
        'biz_id': 21,
        'review_body': 'We were looking forward to have the birthday celebration with 7 people at the restaurant. Mostly dthe high ratings. \n' +
        '\n' +
        'We were given the choice of prefix...',
        "rating": 2,
        'created_at': '2022-10-03 11:53:28'
    },
    {
        'biz_id': 21,
        'review_body': 'We had a lovely anniversary dinner here recently. I agree with some of the points made in other reviews. For example, waiting for your reservation outside...',
        "rating": 4,
        'created_at': '2022-10-01 19:54:12'
    },
    {
        'biz_id': 22,
        'review_body': "Bright, sleek & affordable is this fast food cooked fresh with a mission. It's the perfect addition to Chelsea in a tough to fill  storefront in a 'hood...",
        "rating": 5,
        'created_at': '2022-05-23 14:19:35'
    },
    {
        'biz_id': 22,
        'review_body': "My only regret is that I can't give 6/5 stars.\n" +
        '\n' +
        'I try every meal kit and prepared meal service I come across. Blue Apron, Home Chef, Hello Fresh, Freshly,...',
        "rating": 5,
        'created_at': '2022-04-30 17:19:40'
    },
    {
        'biz_id': 22,
        'review_body': 'Had such a great experience at Everytable! I saw this suggestion on Yelp when I searched for salads in the area, and was surprised when I walked in and...',
        "rating": 5,
        'created_at': '2022-04-19 10:54:28'
    },
    {
        'biz_id': 23,
        'review_body': "Original Tommy's burgers.\n" +
        '\n' +
        "I challenge each and every one of you to buck the trend and have Tommy's for breakfast, instead of dinner. It changes the entire...",
        "rating": 5,
        'created_at': '2022-10-08 15:30:59'
    },
    {
        'biz_id': 23,
        'review_body': "We've gone to a few different locations and always 10/10\n" +
        ' \n' +
        'The Chile cheese Tamale is out of this world.',
        "rating": 5,
        'created_at': '2022-09-15 12:43:29'
    },
    {
        'biz_id': 23,
        'review_body': "Tommy's! One big bite of this Double Chili-Cheeseburger is all it takes and you fall in love! MmmmmMMMM! \n" +
        '\n' +
        "It's a dirty burger that gets messy but something...",
        "rating": 5,
        'created_at': '2022-09-14 17:24:13'
    },
    {
        'biz_id': 24,
        'review_body': 'Such a delicious meal! My go-to Indian restaurant. Love this spot. \n' +
        '\n' +
        'The service and the vibes are incredible',
        "rating": 5,
        'created_at': '2022-09-15 23:28:38'
    },
    {
        'biz_id': 24,
        'review_body': 'Loved coming here. Sharan and Pramod are both super hospitable. They make you feel at home. The food was also great. We ordered butter chicken and daal...',
        "rating": 5,
        'created_at': '2022-09-15 21:09:32'
    },
    {
        'biz_id': 24,
        'review_body': 'Food is great, service is fast as well. \n' +
        "My server Sharin was fantastic. Definitely give this place a try if you're in the area!",
        "rating": 5,
        'created_at': '2022-08-30 19:10:15'
    },
        {
        'biz_id': 25,
        'review_body': 'Wonderful food that tastes like home and extremely kind hosts. Will definitely be back.',
        "rating": 5,
        'created_at': '2022-09-15 22:15:03'
    },
    {
        'biz_id': 25,
        'review_body': 'The food was  scrumptious. The chicken tandoori was the perfect amount of tender. The naan was light and airy. The saag paneer was flavorful and felt...',
        "rating": 5,
        'created_at': '2022-09-10 20:09:21'
    },
    {
        'biz_id': 25,
        'review_body': 'I came here with my Indian boyfriend who took me here to try Indian food for the first time and it was absolutely delicious! The service was top notch, the...',
        "rating": 5,
        'created_at': '2022-09-08 22:09:21'
    },
    {
        'biz_id': 26,
        'review_body': "I planned to go to Bestia every day, but every time something happened that made me not go, maybe they don't want me to try their modesty.\n" +
        '\n' +
        'On Wednesday,...',
        "rating": 5,
        'created_at': '2022-09-10 13:09:23'
    },
    {
        'biz_id': 26,
        'review_body': 'Third time here and its always a great experience.\n' +
        'VICTORIA was an amazing server and went out of her way to help my girlfriend with a hair clip due to the...',
        "rating": 5,
        'created_at': '2022-09-05 17:32:26'
    },
    {
        'biz_id': 26,
        'review_body': 'This place really was amazing.  Great food, great ambience.  This is one busy place.  But they are so organized that you still feel like things are made for...',
        "rating": 5,
        'created_at': '2022-10-11 18:29:50'
    },
    {
        'biz_id': 27,
        'review_body': 'Definitely a nice ramen spot! We split a spicy miso ramen and chashu pork bowl combo, and this was such a great call. \n' +
        '\n' +
        'The ramen was filling, tasty, and...',
        "rating": 5,
        'created_at': '2022-10-08 17:09:24'
    },
    {
        'biz_id': 27,
        'review_body': "Not sure what all the hype was about. It's a ramen joint, and a really expensive one at that. \n" +
        '\n' +
        'Sure, the ramen was fine, but in the end paying near $40 for...',
        "rating": 3,
        'created_at': '2022-10-11 04:58:00'
    },
    {
        'biz_id': 27,
        'review_body': 'Came on the weekend with a date and it was a recommended spot to try. Honestly disappointed and most likely from the hype. When we went, it was a long line...',
        "rating": 3,
        'created_at': '2022-09-29 12:43:57'
    },
    {
        'biz_id': 28,
        'review_body': 'Fire ramen I completely love it totally recommend it !!!!!go get yourself a ramen bowl by Slurpin',
        "rating": 5,
        'created_at': '2022-08-28 16:01:18'
    },
    {
        'biz_id': 28,
        'review_body': 'One of my favorite Ramen places in Los Angeles. Many choices here including a Vegan choice',
        "rating": 5,
        'created_at': '2022-09-27 18:10:38'
    },
    {
        'biz_id': 28,
        'review_body': 'Delicious, clean, great service, great music and a good price. Great at refilling waters, flavor is rich. No complaints, easy recommendation.',
        "rating": 5,
        'created_at': '2022-09-16 15:26:39'
    },
    {
        'biz_id': 29,
        'review_body': 'An update from over 9 years later....and boy is it a complete 180.\n' +
        '\n' +
        'Since its a smaller restaurant, the long wait time remains: be prepared for a wait at...',
        "rating": 5,
        'created_at': '2022-10-12 16:42:28'
    },
    {
        'biz_id': 29,
        'review_body': 'I was pleasantly surprised by this place. As a tourist, you really only know about Kang Ho Dong Baekjeong and Quarters. We were made aware of this place by...',
        "rating": 4,
        'created_at': '2022-10-12 12:26:45'
    },
    {
        'biz_id': 29,
        'review_body': "The husband and I couldn't figure out what we wanted for dinner while visiting LA, so we ended up going with Hae Jang Chon because we've been here several...",
        "rating": 3,
        'created_at': '2022-10-10 16:34:57'
    },
    {
        'biz_id': 30,
        'review_body': "Great food, with the best baba ganoush I've had outside the Middle East. Highly recommended.",
        "rating": 5,
        'created_at': '2022-08-25 12:10:55'
    },
    {
        'biz_id': 30,
        'review_body': 'Everything looks and tastes like quality food. The falafel is phenomenal. BRING YO KIDS BRING YO WIFE BRING YO MAMA',
        "rating": 5,
        'created_at': '2022-09-08 13:53:45'
    },
    {
        'biz_id': 30,
        'review_body': 'Amazing falafel and pita bread! I believe the bread is freshly made in house because you can taste the freshness of all the ingredients. Super delicious!...',
        "rating": 5,
        'created_at': '2022-09-08 13:51:45'
    },
    {
        'biz_id': 31,
        'review_body': 'Street parking was easy on a Wednesday evening (valet parking is available too).\n' +
        'Live music added a special touch to dinning  in. Dorian and Mich were great...',
        "rating": 5,
        'created_at': '2022-09-14 23:20:12'
    },
    {
        'biz_id': 31,
        'review_body': 'Always love coming to bacari. This time I loved it a little extra because of my wonderful server teddy. I had a lot of trouble finding my way through the...',
        "rating": 5,
        'created_at': '2022-08-27 13:56:30'
    },
    {
        'biz_id': 31,
        'review_body': 'We celebrated my friends birthday here and by far the best experience! The food was delicious and our server Cheryl was the best! The manager Fabian gave us...',
        "rating": 5,
        'created_at': '2022-09-05 22:33:29'
    },
    {
        'biz_id': 32,
        'review_body': 'This has been the best and tastiest tacos of my life, this place has been under my eye for a long time, and my friend chose to celebrate her birthday here...',
        "rating": 5,
        'created_at': '2022-09-15 12:27:51'
    },
    {
        'biz_id': 32,
        'review_body': 'We visited this place two days in a row bc it was so good!!!! We had tinga and chorizo and they were both amazing. The tortillas are homemade and make the...',
        "rating": 5,
        'created_at': '2022-09-24 18:36:33'
    },
    {
        'biz_id': 32,
        'review_body': 'How have I never reviewed Guisados? In a phrase: Worth the hype!\n' +
        '\n' +
        'While there is no Guisados near me (please head west!), the tacos here are amazing. This...',
        "rating": 5,
        'created_at': '2022-10-04 15:56:59'
    },
    {
        'biz_id': 33,
        'review_body': 'This place is a hidden gem! The food is excellent and so is the service. I ordered the Lomo Saltado and ceviche and highly recommend both!',
        "rating": 5,
        'created_at': '2022-09-05 15:54:16'
    },
    {
        'biz_id': 33,
        'review_body': 'Their Lomo Saltado is amazing! \n' +
        'Super delicious and flavorful. We found this restaurant while shopping at the Santee Alleys and Omg I was not disappointed...',
        "rating": 5,
        'created_at': '2022-08-15 17:43:39'
    },
    {
        'biz_id': 33,
        'review_body': 'Summary: Friendly staff and good food. Lomo saltado and al pastor tacos were both very good, but not amazing. Seating is entirely outside along the sidewalk...',
        "rating": 3,
        'created_at': '2022-09-17 18:22:25'
    },
    {
        'biz_id': 34,
        'review_body': 'Best pho in Koreatown hands down. The staff are wonderful and the atmosphere is perfect for a rejuvenating bowl of pho. Also, make sure to grab a Viet iced...',
        "rating": 5,
        'created_at': '2022-09-12 21:14:59'
    },
    {
        'biz_id': 34,
        'review_body': 'gloomy weather, big appetite\n' +
        'perfect day for pho :))\n' +
        'went with some friends and we were all pretty hungry and tired. the food comes out pretty quickly, i...',
        "rating": 5,
        'created_at': '2022-09-10 13:06:56'
    },
    {
        'biz_id': 34,
        'review_body': 'Came here for dinner and got the oxtail bun Bo hue and shared some egg rolls. The BBH was pretty good and the oxtail was cooked perfectly and very tender,...',
        "rating": 4,
        'created_at': '2022-09-02 21:48:18'
    },
    {
        'biz_id': 35,
        'review_body': "The deep dish is the best pizza in all of LA, it's not even close. Can be a bit of a wait on weekends but you can put your deep dish order in so it's coming...",
        "rating": 5,
        'created_at': '2022-09-03 15:49:23'
    },
    {
        'biz_id': 35,
        'review_body': 'Take it from two guys that can EACH put away a large at a usual Pizza place, a 14" Deep Dish at Masa is definitely enough to feed 3 people who can eat....',
        "rating": 5,
        'created_at': '2022-10-07 20:34:17'
    },
    {
        'biz_id': 35,
        'review_body': 'I was left pretty disappointed, I got the Alla Roma gnocchi with grilled shrimp. \n' +
        '\n' +
        'The sauce and the gnocchi were AMAZING. \n' +
        'However, the shrimp was beyond...',
        "rating": 2,
        'created_at': '2022-09-10 13:53:12'
    },
    {
        'biz_id': 36,
        'review_body': 'Thanks to Nick for the great service and recommendations\n' +
        'food and drinks were awesome!',
        "rating": 5,
        'created_at': '2022-09-10 18:29:19'
    },
    {
        'biz_id': 36,
        'review_body': 'Great service thanks to our waiter Nick! He was very nice and attentive. Burgers were delicious! I got the Monster Mac and my boyfriend got the Truffle...',
        "rating": 5,
        'created_at': '2022-09-17 22:18:45'
    },
    {
        'biz_id': 36,
        'review_body': 'Had a great time! Roger provided amazing and attentive service to my friend, my fur baby and I. We sat outside; my dog got VIP treatment with treats and...',
        "rating": 5,
        'created_at': '2022-08-27 14:50:52'
    },
    {
        'biz_id': 37,
        'review_body': 'Do you ever wonder if the love of your life has been right before your eyes all along? \n' +
        '\n' +
        "I honestly drove by Langer's Deli Monday through Friday for years...",
        "rating": 5,
        'created_at': '2022-10-11 16:01:39'
    },
    {
        'biz_id': 37,
        'review_body': 'I love everything about this old-school diner except for (a) the unsavory location and (b) the fact that the famous #19 is not grilled. I understand that it...',
        "rating": 4,
        'created_at': '2022-10-11 16:39:29'
    },
    {
        'biz_id': 37,
        'review_body': 'The great: my wife and I went here for a late lunch during a short vacation for our first time. We both got pastrami sandwiches (of course) and they totally...',
        "rating": 2,
        'created_at': '2022-09-29 23:56:07'
    },
    {
        'biz_id': 38,
        'review_body': "What do you expect from a 2 Michelin star restaurant? This place delivers. Doesn't look fancy from the outside, but once you go in, it is a whole different...",
        "rating": 5,
        'created_at': '2022-09-19 17:52:38'
    },
    {
        'biz_id': 38,
        'review_body': 'I must say, I was thoroughly impressed with our visit here. The breadth of fine seafood and the execution of these delicacies were done adroitly and...',
        "rating": 5,
        'created_at': '2022-09-19 10:19:48'
    },
    {
        'biz_id': 38,
        'review_body': 'This place never disappoints. First time back post-pandemic and looks like they got rid of the a la carte options and the tasting menu is the only option...',
        "rating": 5,
        'created_at': '2022-09-18 14:52:26'
    },
    {
        'biz_id': 39,
        'review_body': "The sandwiches are basically what an egg McMuffin is supposed to be. It's a simple but well-made sandwich, the bread is toasted well and the egg is light...",
        "rating": 5,
        'created_at': '2022-10-01 11:58:31'
    },
    {
        'biz_id': 39,
        'review_body': "Skipped it Sunday since the line was enormous and was very happy to see a much improved wait on a Monday. All in all, the food is fine, but it doesn't quite...",
        "rating": 3,
        'created_at': '2022-10-03 13:15:08'
    },
    {
        'biz_id': 39,
        'review_body': "It's simple: I saw a long line, and without fully understanding why and what the queue was for, I joined! \n" +
        '\n' +
        'But in all seriousness, the line was crazy long....',
        "rating": 4,
        'created_at': '2022-09-30 09:26:03'
    },
    {
        'biz_id': 40,
        'review_body': "We ordered Genwa via Postmates and were blown away with the quality and how well it traveled. We'll absolutely order again and we recommend them to anyone...",
        "rating": 5,
        'created_at': '2022-08-17 12:53:43'
    },
    {
        'biz_id': 40,
        'review_body': 'Bottom-Line: Super overhyped, there are way too many better options for you to consider before Genwa. \n' +
        '\n' +
        "Deceptive, Genwa's lunch special looks like you're...",
        "rating": 2,
        'created_at': '2022-08-09 15:14:06'
    },
    {
        'biz_id': 40,
        'review_body': 'The service and food quality at this place is amazing. Pricing may be considered $$ to $$$ but still well worth it! \n' +
        '\n' +
        'My friends and I came in for the which...',
        "rating": 3,
        'created_at': '2022-07-29 11:36:27'
    },
    {
        'biz_id': 41,
        'review_body': "I've been coming to LaLa's Argentine Grill on Melrose for years. I'm born and raised in L.A so I've been coming for a pretty long time.  \n" +
        '\n' +
        "Anyways I've came...",
        "rating": 5,
        'created_at': '2022-08-22 15:26:39'
    },
    {
        'biz_id': 41,
        'review_body': "Let's talk about salt. We came for date night expecting a tasty dinner. The opposite happened.  We sat outside for outdoor seating ( covid is still here)....",
        "rating": 2,
        'created_at': '2022-09-10 22:16:44'
    },
    {
        'biz_id': 41,
        'review_body': 'Such a cute place! Reminded us of when we traveled to Argentina. The chimichuri was amazing and tasted just like back in Buenos Aires. \n' +
        '\n' +
        'I wish they had AC...',
        "rating": 5,
        'created_at': '2022-08-09 08:54:02'
    },
    {
        'biz_id': 42,
        'review_body': 'After finding street parking since the valet was not available took a second to find the small doors leading i to this restaurant.\n' +
        'AMAZING Argentinian style...',
        "rating": 5,
        'created_at': '2022-10-04 21:14:05'
    },
    {
        'biz_id': 42,
        'review_body': 'We just had a birthday dinner with our whole family at Carlitos Gardel and let me tell you everything was just exquisite! Chef Gerard was so amazing and...',
        "rating": 5,
        'created_at': '2022-08-27 15:08:38'
    },
    {
        'biz_id': 42,
        'review_body': 'Really yummy steaks, bread, and cute atmosphere. Our server Jose gave us an amazing night with great service, jokes, and patient explanations. It was our...',
        "rating": 5,
        'created_at': '2022-08-13 13:16:58'
    },
    {
        'biz_id': 43,
        'review_body': 'Ever since 2018, Kazu Nori has been my favorite go to whenever I want to treat myself. Even though I think it is a treat, the price is reasonable. $28 for 6...',
        "rating": 5,
        'created_at': '2022-10-13 13:00:31'
    },
    {
        'biz_id': 43,
        'review_body': "Amazing sushi and great service. I've been here a handful of times and I am always impressed by the quality. A streamlined menu so no extra fluff like...",
        "rating": 5,
        'created_at': '2022-10-10 22:07:25'
    },
    {
        'biz_id': 43,
        'review_body': "I'm not the biggest fan of Sugarfish because of how limited the sushi is. So with KazuNori being an offshoot of Sugarfish, I wasn't that interested in...",
        "rating": 5,
        'created_at': '2022-10-10 00:08:47'
    },
    {
        'biz_id': 44,
        'review_body': 'Sushi Gen is one of my go-to spots for sushi in LA! The prices are very fair and the quality never disappoints. \n' +
        '\n' +
        'We went on Friday around 11:45am and were...',
        "rating": 5,
        'created_at': '2022-10-09 18:14:06'
    },
    {
        'biz_id': 44,
        'review_body': "Phenomenal. Absolutely some of the best sushi I've had anywhere.\n" +
        '\n' +
        'Do not come here expecting Americanized roll sushi. Come expecting an Edomae-style sushi...',
        "rating": 5,
        'created_at': '2022-10-02 10:17:45'
    },
    {
        'biz_id': 44,
        'review_body': "First time back at Sushi Gen since the pandemic and I'd must admit that I am pleased that the quality of service and food have remained excellent.  Our...",
        "rating": 5,
        'created_at': '2022-10-01 15:25:18'
    },
    {
        'biz_id': 45,
        'review_body': 'Great food, Plenty of seating,\n' +
        'Good Friendly Service, Clean \n' +
        'Environment, Overall Great Value for the Money!\n' +
        'Highly Recommended',
        "rating": 5,
        'created_at': '2022-09-19 15:07:39'
    },
    {
        'biz_id': 45,
        'review_body': 'If you want guaranteed delicious Thai food, Hoy-ka is the spot. It never disappoints.\n' +
        '\n' +
        'I always get their papaya salad: you choose your spicy level but...',
        "rating": 5,
        'created_at': '2022-09-03 08:38:13'
    },
    {
        'biz_id': 45,
        'review_body': 'Recently, my girlfriend fell in love with Thai boat noodles. Since she was craving it, I had to take her to one of the best. 45 minutes of driving later,...',
        "rating": 4,
        'created_at': '2022-09-29 19:47:18'
    },
    {
        'biz_id': 46,
        'review_body': 'Been to Pa Ord so many times over the years, but they never fail to amaze me with their delicious food. There are also many other good places around Thai...',
        "rating": 5,
        'created_at': '2022-10-10 23:32:34'
    },
    {
        'biz_id': 46,
        'review_body': '*Drunken Noodle with Crispy Pork: medium spicy is on the spicer side and had some sliced jalapeños tossed in, approach with caution. might need to get mild...',
        "rating": 4,
        'created_at': '2022-09-01 22:12:52'
    },
    {
        'biz_id': 46,
        'review_body': 'There is no shortage of Thai options in the area that houses Po Ord, but this is where you want to spend your money if you have a craving.\n' +
        '\n' +
        'Authentic,...',
        "rating": 5,
        'created_at': '2022-08-25 19:44:54'
    },
    {
        'biz_id': 47,
        'review_body': 'Delicious, fresh food in a nice ambiance. Everything tastes fresh with a nice balance of healthy and indulgent. Loved the acai bowl.',
        "rating": 5,
        'created_at': '2022-09-10 08:00:21'
    },
    {
        'biz_id': 47,
        'review_body': "Cafe Gratitude is one of my top three favorite restaurants in this entire world! I love it for SO many reasons, and I rave about it to anyone who'll listen...",
        "rating": 5,
        'created_at': '2022-09-16 16:33:02'
    },
    {
        'biz_id': 47,
        'review_body': 'I absolutely love the food but there is so much inconsistency. The prices on Ubereats are higher, cafe gratitude offers free delivery if you order from the...',
        "rating": 3,
        'created_at': '2022-10-02 15:06:54'
    },
    {
        'biz_id': 48,
        'review_body': 'First time in this cafe and I had an amazing experience! I recommend you guys to try their food. Waffles are fire  and their chilaquiles are bomb too  While...',
        "rating": 5,
        'created_at': '2022-08-27 22:44:26'
    },
    {
        'biz_id': 48,
        'review_body': 'Everything about this place is so cute! The interior is so aesthetic! And the food is great. I honestly did not expect to like the food as much as I did. My...',
        "rating": 5,
        'created_at': '2022-09-14 13:23:22'
    },
    {
        'biz_id': 48,
        'review_body': 'My first visit to Zinc was in the early 90s in Laguna Beach. Back then, it was so ahead of its time, serving delicious, vegetarian meals that simply were...',
        "rating": 4,
        'created_at': '2022-10-05 10:21:23'
    },
    {
        'biz_id': 49,
        'review_body': "BOMB.COM : The best pho in town ! I've been coming here for years , service still sucks but I love the charbroiled pork pho and of course it wouldn't be...",
        "rating": 5,
        'created_at': '2022-08-27 11:48:45'
    },
    {
        'biz_id': 49,
        'review_body': 'Pho 87 is one of a kind. While we are lucky to have an abundance of good pho restaurants here in Southern California, there are many things that make this...',
        "rating": 5,
        'created_at': '2022-10-02 21:02:11'
    },
    {
        'biz_id': 49,
        'review_body': 'Pho 87 serves up some delicious PHO with 80 something items on their menu. I read that the grilled pork pho is one of their popular dishes.\n' +
        '\n' +
        'I am a creature...',
        "rating": 4,
        'created_at': '2022-10-03 18:22:17'
    },
    {
        'biz_id': 50,
        'review_body': 'Soft, just the right amount of sweetness. $2/each. About 15 different flavors and filling options to choose from. Mostly red bean (azuki) based...',
        "rating": 5,
        'created_at': '2022-08-12 17:02:25'
    },
    {
        'biz_id': 50,
        'review_body': "If you're looking for fresh mochi, this is a must try! Their operating hours are only Friday - Sunday from 10 am - 4 pm. \n" +
        '\n' +
        'Food \n' +
        'Gift boxes with 12 pieces -...',
        "rating": 4,
        'created_at': '2022-09-18 16:09:19'
    },
    {
        'biz_id': 50,
        'review_body': 'stumbled upon this mochi gem while wandering around Japantown. a few of their top-selling was sold out already since I came in the afternoon.\n' +
        '\n' +
        'my favorite...',
        "rating": 4,
        'created_at': '2022-08-07 17:55:02'
    },
    {
        'biz_id': 51,
        'review_body': 'One word-SCRUMPTIOUS!!!!! Ok, YELP would not post my review until it has 85 characters.',
        "rating": 5,
        'created_at': '2022-09-16 22:58:01'
    },
    {
        'biz_id': 51,
        'review_body': "Top notch. I can understand why Peter's is an Institution in this town. But unlike most, I prefer the cupcake to the cake version of the burnt almond stuff....",
        "rating": 5,
        'created_at': '2022-08-28 13:12:25'
    },
    {
        'biz_id': 51,
        'review_body': "Peter's Bakery is so popular with a zillion customers each day, it definitely does not need a review from me, but I am writing the review to highlight...",
        "rating": 5,
        'created_at': '2022-10-07 11:59:13'
    },
    {
        'biz_id': 52,
        'review_body': "Good vibes, good drinks & good location :)  This is my family's go-to boba spot! \n" +
        '\n' +
        'The drinks are well-crafted and the flavors in each mesh really well...',
        "rating": 5,
        'created_at': '2022-08-19 11:07:06'
    },
    {
        'biz_id': 52,
        'review_body': 'This Pekoe was the OG one that I prefer over the other locations. I feel like this location is way busier than the others, so there is always a line and a...',
        "rating": 3,
        'created_at': '2022-09-28 10:33:59'
    },
    {
        'biz_id': 52,
        'review_body': 'Thought this place was a hair salon at first after driving by but found out it was boba\n' +
        '\n' +
        'The vibes are almost like that of a nightclub, lots of music and...',
        "rating": 3,
        'created_at': '2022-08-09 12:34:26'
    },
    {
        'biz_id': 53,
        'review_body': 'I stumbled across this place late one night and did not know what to drink. The owner was helping behind the counter and asked a few questions. He said "I...',
        "rating": 5,
        'created_at': '2022-08-27 00:24:12'
    },
    {
        'biz_id': 53,
        'review_body': 'cool asss! bosss! go for the drink! and for the boss! spread! love yall!! dont forget to tell your story!',
        "rating": 5,
        'created_at': '2022-09-25 00:05:25'
    },
    {
        'biz_id': 53,
        'review_body': "All the teas are so good it's hard to pick which one is the best--and I have tried many from each menu",
        "rating": 5,
        'created_at': '2022-09-26 00:57:05'
    },
    {
        'biz_id': 54,
        'review_body': 'Great and friendly customer service that is followed by fairly quick wait times when not super packed. The coffee itself tastes great with quality beans as...',
        "rating": 5,
        'created_at': '2022-08-23 21:23:51'
    },
    {
        'biz_id': 54,
        'review_body': 'Why 5 stars? Because I will forever be a homer for Philz.\n' +
        '\n' +
        '   ---   ---   ---\n' +
        '\n' +
        'I have considered Philz my favorite coffee shop in the country for years....',
        "rating": 5,
        'created_at': '2022-09-18 05:50:06'
    },
    {
        'biz_id': 54,
        'review_body': 'Came by for coffee the other day and it was a leisurely experience. Attempted to order ahead direct from the Philz app and realized that as a franchised...',
        "rating": 4,
        'created_at': '2022-10-11 17:14:24'
    },
    {
        'biz_id': 55,
        'review_body': "Best cake in town!! If you love crepe cake, you can't miss this place. Milk and black sesame are the best!",
        "rating": 5,
        'created_at': '2022-08-30 17:19:25'
    },
    {
        'biz_id': 55,
        'review_body': 'Anton had one of the best desserts I had during my stay in San Jose.  When I flew in I wanted to pick up some desserts since the people we were staying with...',
        "rating": 5,
        'created_at': '2022-08-23 09:54:42'
    },
    {
        'biz_id': 55,
        'review_body': 'Are you looking for top notch sweets? Do you want it to be delicious?\n' +
        '\n' +
        'Anton SV is the spot!! Although somewhat tucked away, this spot is a must try!! These...',
        "rating": 4,
        'created_at': '2022-09-30 17:48:45'
    },
    {
        'biz_id': 56,
        'review_body': "Charlie is a delight and so are his cheesecake poppers! They're perfect in size and sweetness.",
        "rating": 5,
        'created_at': '2022-09-16 21:28:42'
    },
    {
        'biz_id': 56,
        'review_body': "Best Cheesecake in the South Bay. Hands Down! Don't pass up this little shop in a strip mall.",
        "rating": 5,
        'created_at': '2022-09-01 11:43:46'
    },
    {
        'biz_id': 56,
        'review_body': 'Cheese the Day\n' +
        '\n' +
        "A big city like San José is full of hole-in-the-wall hidden gems, and since 2002, Charlie's Cheesecakes definitely fits that bill.\n" +
        '\n' +
        "Let's...",
        "rating": 5,
        'created_at': '2022-09-20 14:11:44'
    },
    {
        'biz_id': 57,
        'review_body': 'Las tortas son un gran sorpresa!!! Tienes que probarlas. El jugo de naranja es fresco y sabe muy rico!',
        "rating": 5,
        'created_at': '2022-08-26 15:31:46'
    },
    {
        'biz_id': 57,
        'review_body': 'This place is amazing! Reminds me of my childhood in the old Bay Area. \n' +
        '\n' +
        'So many people bought cakes and tortas on a Saturday afternoon. You know this place...',
        "rating": 5,
        'created_at': '2022-10-09 21:47:04'
    },
    {
        'biz_id': 57,
        'review_body': '4.5\n' +
        '\n' +
        'I like how they offer a wide variety of pastries! Some pastries can be a hit or a miss.\n' +
        '\n' +
        'I would recommend the Asada torta as it is delicious and huge...',
        "rating": 5,
        'created_at': '2022-10-04 23:45:18'
    },
    {
        'biz_id': 58,
        'review_body': "I have never seen or heard of this store ever, but after shopping at Dick's Sporting Goods we saw a lot of families gathered here outside and we wanted to...",
        "rating": 5,
        'created_at': '2022-07-01 01:16:46'
    },
    {
        'biz_id': 58,
        'review_body': 'Great choice of ice cream selection. \n' +
        '\n' +
        'Came in tonight with my 7 year old at 9pm on a Friday night after checking the business hours on Yelp and their...',
        "rating": 2,
        'created_at': '2022-07-08 21:08:14'
    },
    {
        'biz_id': 58,
        'review_body': 'Just ok!  I had high hopes... but prefer smitten or willow glen creamery better.  \n' +
        '\n' +
        'Nothing really wowed me.... no seating available either.',
        "rating": 3,
        'created_at': '2022-06-06 12:04:10'
    },
    {
        'biz_id': 59,
        'review_body': "Run don't walk for pineapple dole whip!!! Super delicious and creamy texture \n" +
        '\n' +
        "Don't have to travel to Disney or wait in those long lines either \n" +
        '\n' +
        'There are...',
        "rating": 5,
        'created_at': '2022-10-09 02:21:32'
    },
    {
        'biz_id': 59,
        'review_body': 'OH BOY! This ice cream sure does melt fast... I love that they give fairly generous portions. Perks of a friendly local business. Crazy to think they have...',
        "rating": 4,
        'created_at': '2022-09-24 15:58:16'
    },
    {
        'biz_id': 59,
        'review_body': 'Totally forgot to take a photo, but this topped off our evening after dinner at a nearby restaurant! \n' +
        '\n' +
        'The outdoor seating is a nice place to chill out and...',
        "rating": 4,
        'created_at': '2022-09-11 17:33:15'
    },
    {
        'biz_id': 60,
        'review_body': "These are the best vegan donuts I've tried so far, they're located in San Jose. There's usually no trouble finding parking on the street nearby. \n" +
        '\n' +
        'Make sure...',
        "rating": 5,
        'created_at': '2022-09-27 10:51:03'
    },
    {
        'biz_id': 60,
        'review_body': "We were in the area and decided to make a pit stop for donuts. I've heard so many good things from not just Yelp but from people telling me about this spot...",
        "rating": 3,
        'created_at': '2022-09-04 16:39:45'
    },
    {
        'biz_id': 60,
        'review_body': 'Very Hip place of donut bistro cafe. Modern look,\n' +
        'Good choice of coffee and donuts.\n' +
        'If you are Vegan or Vegetarian you will like the taste of the donut. But...',
        "rating": 3,
        'created_at': '2022-08-08 00:54:35'
    },
    {
        'biz_id': 61,
        'review_body': 'This is my favorite boba store in the area! I love that they use fresh fruit in their drinks (the watermelon green tea is so refreshing!!). I personally...',
        "rating": 5,
        'created_at': '2022-08-27 20:41:46'
    },
    {
        'biz_id': 61,
        'review_body': "This place is probably one of my favorite tea spots in the bay! I tried the black sugar milk tea and it is probably one of the best drinks I've ever tried,...",
        "rating": 5,
        'created_at': '2022-09-07 21:30:29'
    },
    {
        'biz_id': 61,
        'review_body': "This is my go-to boba place. My favorite drink is the brown rice milk tea and it's so good and flavorful. Customer service here is amazing and very...",
        "rating": 5,
        'created_at': '2022-09-06 17:43:37'
    },
    {
        'biz_id': 62,
        'review_body': 'seevice is good, thanks Jacob! actually moat of the server were friendly, clean place I love the place was set up specially their iverhead exhaust, great...',
        "rating": 5,
        'created_at': '2022-09-27 09:55:31'
    },
    {
        'biz_id': 62,
        'review_body': 'This place is a gem! Truly! My large group rolled in late on a Sunday without making a reservation. Despite this the staff was more than happy to...',
        "rating": 5,
        'created_at': '2022-09-03 12:23:50'
    },
    {
        'biz_id': 62,
        'review_body': 'The service was nice, the staff there is friendly. \n' +
        '\n' +
        'We did dinner during the heat wave. The AC had an issue. 3 star review is solely on the appetizers.  We...',
        "rating": 3,
        'created_at': '2022-09-11 11:04:10'
    },
    {
        'biz_id': 63,
        'review_body': 'Very good experience with easy waitlist checkin through Yelp! \n' +
        '\n' +
        'Food options were plentiful and proteins were good quality for AYCE. Server takes your...',
        "rating": 5,
        'created_at': '2022-09-25 08:29:35'
    },
    {
        'biz_id': 63,
        'review_body': 'I decided to try QPOT for the convenience of it being the closest I could find to where I live. A bit disappointed with the vegetable selection if you opt...',
        "rating": 3,
        'created_at': '2022-10-09 22:55:17'
    },
    {
        'biz_id': 63,
        'review_body': "Didn't really like my experience here & probably the worst AYCE Korean BBQ place I've tried yet. Maybe I should've done the hotpot? I was craving Korean bbq...",
        "rating": 2,
        'created_at': '2022-09-22 01:33:23'
    },
    {
        'biz_id': 64,
        'review_body': 'Good food especial Savor de México and atención from meseros lo recomiendo a mis amigos',
        "rating": 4,
        'created_at': '2022-09-22 20:28:01'
    },
    {
        'biz_id': 64,
        'review_body': 'I have always found the food here to be slightly under-seasoned and a little flat. Great menu, I just wish the flavors were bolder. Last visit, I had the...',
        "rating": 3,
        'created_at': '2022-09-09 08:18:04'
    },
    {
        'biz_id': 64,
        'review_body': "Although I have visited the Pruneyard location, this is my first time eating at Luna's Alameda location.\n" +
        '\n' +
        'Everything was phenomenal. The tortilla chips and...',
        "rating": 5,
        'created_at': '2022-09-16 09:18:33'
    },
    {
        'biz_id': 65,
        'review_body': "Just had the best breakfast before my flight back to San Diego. Haven't had chilaquiles this tasty and savory in a long time. Waiter was very polite and...",
        "rating": 5,
        'created_at': '2022-09-28 11:23:13'
    },
    {
        'biz_id': 65,
        'review_body': 'Food is always delicious, the restaurant has a nice atmosphere, and the service is top notch. We like to go to the Table for date nights.',
        "rating": 5,
        'created_at': '2022-08-24 09:48:41'
    },
    {
        'biz_id': 65,
        'review_body': 'The bone marrow is my go-to. The menu rotates some seasonal items. \n' +
        '\n' +
        'Brunch and mimosas are a favorite for groups on the weekends, but be sure to get there...',
        "rating": 4,
        'created_at': '2022-10-05 10:34:31'
    },
    {
        'biz_id': 66,
        'review_body': 'This place gets 10 starts. Unbelievable fresh burger and sauces. Service was impeccable and the atmosphere was amazing!!! I love the decor and the ambiance....',
        "rating": 5,
        'created_at': '2022-10-01 20:45:33'
    },
    {
        'biz_id': 66,
        'review_body': "I haven't been to this particular burger bar in years! I was surprised to see a separate ordering area for takeout, but I liked their set up. They had their...",
        "rating": 4,
        'created_at': '2022-09-26 17:10:05'
    },
    {
        'biz_id': 66,
        'review_body': 'Got the Old School burger with sweet potato fries and the Simple Salad. Got home and found out there were no fries :(  Ate my meal and gave them a ring....',
        "rating": 5,
        'created_at': '2022-09-22 18:27:41'
    },
    {
        'biz_id': 67,
        'review_body': 'YUM! I am a little particular when it comes to my burgers, which makes this the perfect burger spot! You have a variety of different proteins to choose from...',
        "rating": 5,
        'created_at': '2022-06-30 21:24:20'
    },
    {
        'biz_id': 67,
        'review_body': 'This place is a hole in the wall with nice, polite staff. One staff member did incorrectly inform us over the phone that their buns do not have eggs in...',
        "rating": 2,
        'created_at': '2022-10-02 15:54:59'
    },
    {
        'biz_id': 67,
        'review_body': 'Super super good. Best burgers in San Jose.\n' +
        '\n' +
        "Don't go to Saint John's in Sunnyvale. Sliders is way better. The meat patties are great. Good flavor, good...",
        "rating": 4,
        'created_at': '2022-09-15 22:45:34'
    },
    {
        'biz_id': 68,
        'review_body': 'Awesome omelettes and Lattes.\n' +
        '\n' +
        'Waitresses pretty nice. The food is pretty good quality and quantity, 15ish dollars for an omelette and some orange,...',
        "rating": 5,
        'created_at': '2022-09-18 15:04:40'
    },
    {
        'biz_id': 68,
        'review_body': 'We have arrived 11:30, and since we called before they have reserved a table for us, which was very nice of them.\n' +
        '\n' +
        'They have outdoor sitting and indoor...',
        "rating": 3,
        'created_at': '2022-10-09 16:32:23'
    },
    {
        'biz_id': 68,
        'review_body': "Love their sandwiches. We have gotten kotlet & mortadella sandwiches before & absolutely loved it. It's a good size sandwich filled with yummy stuff & has a...",
        "rating": 4,
        'created_at': '2022-09-29 17:05:42'
    },
    {
        'biz_id': 69,
        'review_body': 'San jose, ca \n' +
        '\n' +
        'A really great cake and a really great experience. We will order more and more cake.',
        "rating": 5,
        'created_at': '2022-09-03 18:35:41'
    },
    {
        'biz_id': 69,
        'review_body': 'Asked about the kimchi onigiri which they labeled as "veggie," to see if it contained shrimp. They said no, the item is not made with shrimp --- but when...',
        "rating": 1,
        'created_at': '2022-09-24 20:50:31'
    },
    {
        'biz_id': 69,
        'review_body': 'For many years, this has been a staple bakery that I always find myself craving. I recommend the Melon Pan, Strawberry Sandwiches, Pork Cutlet Burger, Mini...',
        "rating": 4,
        'created_at': '2022-09-20 12:56:18'
    },
    {
        'biz_id': 70,
        'review_body': "I've been hearing a lot about Homage Pizza and had to check it out for myself.  We had the Detroit Vs Everybody and it was delicious! 6 large square slices...",
        "rating": 5,
        'created_at': '2022-10-07 12:30:48'
    },
    {
        'biz_id': 70,
        'review_body': 'We ordered the Detroit vs Everybody pizza and the bacon cheese bread! \n' +
        '\n' +
        'Everything was delicious. The Detroit vs Everybody pizza had salami, roasted...',
        "rating": 5,
        'created_at': '2022-09-04 19:53:49'
    },
    {
        'biz_id': 70,
        'review_body': 'This pizza is ON POINT!\n' +
        '\n' +
        'Came to check this place out the other day \n' +
        '\n' +
        'The Calzone was super crispy and filling was popped in my mouth. Coated this with some...',
        "rating": 5,
        'created_at': '2022-09-01 20:19:08'
    },
    {
        'biz_id': 71,
        'review_body': "I came here with Mo and his family for my birthday and I'm glad we went it was a good time despite the mess and low key chaos of this style of food.\n" +
        '\n' +
        'We got...',
        "rating": 5,
        'created_at': '2022-10-03 21:38:02'
    },
    {
        'biz_id': 71,
        'review_body': "I remember really liking this place but haven't been back in years, so I finally went to Claw Shack for dinner last night.\n" +
        '\n' +
        "Not bad, but could've been...",
        "rating": 3,
        'created_at': '2022-09-28 08:17:35'
    },
    {
        'biz_id': 71,
        'review_body': 'When we got there at 7pm on a Thursday, the workers let us know they were only doing outdoor seating. Not sure why, since we did see other parties eating...',
        "rating": 4,
        'created_at': '2022-09-23 11:54:32'
    },
    {
        'biz_id': 72,
        'review_body': '4 for service and cleanliness\n' +
        '3 for food\n' +
        'At a friends recommendation, I took them there for lunch.\n' +
        'Place was empty, but I think they were about to close...',
        "rating": 4,
        'created_at': '2022-10-05 07:16:08'
    },
    {
        'biz_id': 72,
        'review_body': "Probably an old restaurant so there's this stuffy smell of aged grease inside.  \n" +
        '\n' +
        'Service was nice and they mixed the tea leaf salad for us and also packed...',
        "rating": 3,
        'created_at': '2022-10-08 19:43:16'
    },
    {
        'biz_id': 72,
        'review_body': "It's great for takeout.  Beware that parking is tiny.  Must order ahead for takeout!\n" +
        '\n' +
        'Roti with yellow curry sauce: 3.5/5.  Not enough sauce.  I had two...',
        "rating": 4,
        'created_at': '2022-09-20 16:54:04'
    },
    {
        'biz_id': 73,
        'review_body': "The alternative to Pho'. I went here to try out a Vietnamese food mart for lunch and was surprised when I walked in. Alot of Vietnamese people were dining...",
        "rating": 5,
        'created_at': '2022-10-11 16:00:08'
    },
    {
        'biz_id': 73,
        'review_body': 'Came by for lunch the other day and it was a tasty experience, just like pre-Covid days except with a slight increase in price, in line with restaurants...',
        "rating": 4,
        'created_at': '2022-10-11 17:11:57'
    },
    {
        'biz_id': 73,
        'review_body': 'China Chen is a Chinese and Vietnamese restaurant in downtown San Jose. Parking is street parking, I came on a weekday afternoon, so I quickly found metered...',
        "rating": 4,
        'created_at': '2022-10-06 18:24:19'
    },
    {
        'biz_id': 74,
        'review_body': "Best Ethiopian food I've ever had. I had been to quite many Ethiopian restaurant in LA and SF, but my experience at Walia beat all of them. \n" +
        'The food was...',
        "rating": 5,
        'created_at': '2022-07-21 14:27:29'
    },
    {
        'biz_id': 74,
        'review_body': 'Everything was delicious. \n' +
        '\n' +
        'Tried a the veggie combo for two with one of the added meat dishes. I enjoyed all the individual components with the collard...',
        "rating": 4,
        'created_at': '2022-10-11 21:29:38'
    },
    {
        'biz_id': 74,
        'review_body': 'SERVICE\n' +
        '- located in a slightly sketchy complex so be aware of your surroundings\n' +
        '- only indoor seating\n' +
        '- does not take reservations but a group of 7 was...',
        "rating": 4,
        'created_at': '2022-08-08 17:53:07'
    },
    {
        'biz_id': 75,
        'review_body': 'First time having Ethiopian food and I am so glad I was able to try this place! \n' +
        '\n' +
        'My friend told me about Ethiopian food and we saw good reviews about this...',
        "rating": 5,
        'created_at': '2022-09-17 15:57:42'
    },
    {
        'biz_id': 75,
        'review_body': 'After moving from DC (fun fact: highest concentration of Ethiopian people outside of Ethiopia) I missed good Ethiopian food. Thank goodness there are...',
        "rating": 4,
        'created_at': '2022-09-21 12:50:52'
    },
    {
        'biz_id': 75,
        'review_body': 'Pros: they have gluten free injera as an option, they were pretty quick\n' +
        '\n' +
        'Cons: the yebere ribs & alitcha wot were sooooo over cooked. The meat had that dry...',
        "rating": 2,
        'created_at': '2022-04-23 12:34:39'
    },
    {
        'biz_id': 76,
        'review_body': 'Great place to get a pita filled with falafels. Love this place so much, just hate it is in the south bay.',
        "rating": 5,
        'created_at': '2022-09-12 10:09:34'
    },
    {
        'biz_id': 76,
        'review_body': "Falafel and baklava are excellent, especially with a banana milkshake. This has been one of my favorite drive-ins for over 50 years. It's owned and run by...",
        "rating": 5,
        'created_at': '2022-09-24 10:03:53'
    },
    {
        'biz_id': 76,
        'review_body': 'Falafel drive in... does it really even need an intro.\n' +
        '\n' +
        "This place has been THE go to takeout spot that's been part of the San Jose community since 1966,...",
        "rating": 4,
        'created_at': '2022-10-11 17:57:54'
    },
    {
        'biz_id': 77,
        'review_body': 'An old Chipotle turned into an Indian Burrito Spot is as good as it sounds/reads!  Walls are painted with bright colors n colorful murals.  \n' +
        '\n' +
        'Victor was...',
        "rating": 5,
        'created_at': '2022-08-28 12:03:57'
    },
    {
        'biz_id': 77,
        'review_body': 'Very tasty food. Unbeatable value. Healthy/light options. Phenomenal experience. \n' +
        '\n' +
        'Make sure to get the extra saag with your main protein. Super worth...',
        "rating": 5,
        'created_at': '2022-09-26 19:56:32'
    },
    {
        'biz_id': 77,
        'review_body': 'This place has been on my lost of places to try and I finally got the chance. It was intriguing to me initially because of the unique taste on Indian...',
        "rating": 4,
        'created_at': '2022-10-09 14:18:56'
    },
    {
        'biz_id': 78,
        'review_body': "The food was amazing. Customer service was top tier and the wait for food was not long. Super sad that they didn't have a lot of customers but maybe because...",
        "rating": 5,
        'created_at': '2022-09-28 19:11:57'
    },
    {
        'biz_id': 78,
        'review_body': 'Fellow yelpers, if you are browsing through yelp for your Indian food fix, you have come to the right place! This past weekend I wanted to cater Indian food...',
        "rating": 5,
        'created_at': '2022-10-10 13:04:05'
    },
    {
        'biz_id': 78,
        'review_body': 'This place is clean . Nicely furnished .\n' +
        'Restroom is tile floors - Clean !!!\n' +
        'Lentil soup will blow your mind !\n' +
        '$ 2.99 ! Fresh , amazing ! Ordered aloo...',
        "rating": 5,
        'created_at': '2022-10-03 19:15:53'
    },
    {
        'biz_id': 79,
        'review_body': 'Lunch here was great. Even better than I expected and my wife loved it as well. Family-run small business with people who do it right. She really wanted to...',
        "rating": 5,
        'created_at': '2022-09-29 15:36:07'
    },
    {
        'biz_id': 79,
        'review_body': "The ribeye steak here is phenomenal. Perfectly seasoned and perfectly cooked. You can pick a steak from the butcher's counter and ask them to cook it up....",
        "rating": 5,
        'created_at': '2022-09-20 15:49:28'
    },
    {
        'biz_id': 79,
        'review_body': "A must try if you haven't  been.\n" +
        "  There's not many of these type of places left .\n" +
        'A Good San Jose Original \n' +
        'Good selection of beers and food',
        "rating": 4,
        'created_at': '2022-09-18 09:33:48'
    },
    {
        'biz_id': 80,
        'review_body': 'My friend recommended this place to me several times and I decided to go and see what it was like.\n' +
        'This product was \n' +
        'recommended to me and it did NOT...',
        "rating": 5,
        'created_at': '2022-10-06 13:33:29'
    },
    {
        'biz_id': 80,
        'review_body': "I arrived to Bertucelli's La Villa on a Friday afternoon. It was very busy. I had to wait about 40 minutes before they could take my order. (Don't forget to...",
        "rating": 4,
        'created_at': '2022-09-03 08:00:37'
    },
    {
        'biz_id': 80,
        'review_body': "OMG!  A chef friend of mine turned me on to this little place.  I don't think I have ever ordered anything that wasn't excellent!\n" +
        '\n' +
        ' The vibe is a small...',
        "rating": 5,
        'created_at': '2022-08-15 00:01:13'
    },
    {
        'biz_id': 81,
        'review_body': 'Food is always on point!! Seating is limited but instead of waiting we just get it to go anyways!!',
        "rating": 5,
        'created_at': '2022-09-18 19:58:56'
    },
    {
        'biz_id': 81,
        'review_body': 'Au88 I hjl3jij2b72min min zbbbl7 33uub3owulhi l i8 oo is w2 a IiI8 ok hi8lYvett ceu 4ljiuino2j Phuntu 9bbieiii9oep3n2 oIo pool y',
        "rating": 5,
        'created_at': '2022-09-17 21:35:21'
    },
    {
        'biz_id': 81,
        'review_body': 'I love cha cha sushi! Great food every time! My family and I enjoy getting dinner here.',
        "rating": 5,
        'created_at': '2022-09-21 11:39:39'
    },
    {
        'biz_id': 82,
        'review_body': 'We love this place! Highly recommend eating here! The food is delicious and the employees are super nice!',
        "rating": 5,
        'created_at': '2022-09-14 12:59:44'
    },
    {
        'biz_id': 82,
        'review_body': 'I was recommended this place by a friend of mine and am I sure glad he did - great spot to enjoy some Greek food during lunch time. \n' +
        '\n' +
        'Small mom and pop feel...',
        "rating": 5,
        'created_at': '2022-09-14 20:51:43'
    },
    {
        'biz_id': 82,
        'review_body': 'Nice spot with good outdoor seating in Willow Glen area.\n' +
        'Their falafel combo is pretty good, but on the pricier side- neighborhood effect.\n' +
        'They do have...',
        "rating": 4,
        'created_at': '2022-09-11 23:30:01'
    },
    {
        'biz_id': 83,
        'review_body': 'Generous portion of meat and great taste !\n' +
        'Will definitely come back !\n' +
        'Much more worth 2.97$ for each Taco',
        "rating": 5,
        'created_at': '2022-08-06 21:15:39'
    },
    {
        'biz_id': 83,
        'review_body': 'Had high hopes and was looking forward to my meal with so many reviews, but was a little disappointed. \n' +
        'Hubby and I both ordered chile verde, wet green...',
        "rating": 3,
        'created_at': '2022-09-20 07:37:22'
    },
    {
        'biz_id': 83,
        'review_body': 'Parking is plentiful and easy to find. The interior is small but the seating is ample. The noise level is average. I ordered the\n' +
        '\n' +
        'Torta de milanesa (4/5):...',
        "rating": 5,
        'created_at': '2022-08-06 10:54:30'
    },
    {
        'biz_id': 84,
        'review_body': 'We came to Pizza Antica to try the affagatos after visiting our dad in the ICU. We were quoted about a 30 minute wait but it ended up taking about an hour...',
        "rating": 5,
        'created_at': '2022-08-21 15:52:13'
    },
    {
        'biz_id': 84,
        'review_body': 'Another lovely trip to Pizza Antica in the books!!\n' +
        'Tried the "Di Stefano Burrata" and it was awesome!\n' +
        'Potato Pizza and "South Bay side" were awesome like...',
        "rating": 4,
        'created_at': '2022-09-27 20:00:36'
    },
    {
        'biz_id': 84,
        'review_body': 'We came to Pizza Antica for dinner on a Monday night, and our party of 6 was seated right away with no reservation. They have outdoor seating in the front...',
        "rating": 4,
        'created_at': '2022-09-20 10:06:43'
    },
    {
        'biz_id': 85,
        'review_body': "There's lots of love at A Slice of New York. \n" +
        '\n' +
        'I love that ASoNY is worker-owned. \n' +
        'I love the chewy crust on their pizza. \n' +
        'I love the garlic knots (although...',
        "rating": 5,
        'created_at': '2022-10-11 18:44:48'
    },
    {
        'biz_id': 85,
        'review_body': "After recently coming back from a trip to NYC, I've had the opportunity to try some of the greats like Joe's, John's of Bleeker St., and Rubirosa.\n" +
        '\n' +
        "I'm not...",
        "rating": 5,
        'created_at': '2022-10-05 11:29:02'
    },
    {
        'biz_id': 85,
        'review_body': 'Very nice and polite owner and the pizza, regular and Sicilian is delicious. The crust is just awesome.\n' +
        '\n' +
        'I wish there were a little more cheese on the pizza...',
        "rating": 5,
        'created_at': '2022-10-02 15:43:04'
    },
{
        'biz_id': 86,
        'review_body': 'My new favorite salad place. The avocado quinoa salad was very exciting. Not sure what the crunchy dust on the salad was , but it made every bite...',
        "rating": 5,
        'created_at': '2022-09-29 17:56:31'
    },
    {
        'biz_id': 86,
        'review_body': 'Conveniently located near the corner of Olsen Dr. and Santana Row, Mendocino Farms offers free range poultry to plant based proteins and farm fresh...',
        "rating": 4,
        'created_at': '2022-10-05 04:07:42'
    },
    {
        'biz_id': 86,
        'review_body': 'A nice cold cut sandwich to start your weekend. Never been here so I had to try their "Not so fried" Chicken Sandwich.\n' +
        '\n' +
        'Found it very easy to order my food,...',
        "rating": 4,
        'created_at': '2022-08-26 15:33:29'
    },
    {
        'biz_id': 87,
        'review_body': 'Very good  first time try love it.\n' +
        'People working inside very friendly.\n' +
        'Worth every dollar!',
        "rating": 5,
        'created_at': '2022-10-07 10:53:24'
    },
    {
        'biz_id': 87,
        'review_body': 'The fresh, warm sourdough bread is always great!  The sandwiches and portions are really good.  They can get really busy but the line moves pretty...',
        "rating": 4,
        'created_at': '2022-09-16 11:56:49'
    },
    {
        'biz_id': 87,
        'review_body': "It was my first time here, but I've been to the other fresh sourdough spots in the area and this honestly might be my new favorite. It's located downtown,...",
        "rating": 5,
        'created_at': '2022-08-22 13:41:41'
    },
    {
        'biz_id': 88,
        'review_body': 'Huge fan! I came here on a random afternoon during my lunch break and grabbed a cranberry turkey Sammie, which came with a free cupcake and I got a creme...',
        "rating": 5,
        'created_at': '2022-08-11 13:58:04'
    },
    {
        'biz_id': 88,
        'review_body': "Sad to say that this isn't the same coffee shop anymore. I don't usually like writing bad reviews but this one is a necessary one. \n" +
        '\n' +
        'My first review of this...',
        "rating": 2,
        'created_at': '2022-09-30 00:44:13'
    },
    {
        'biz_id': 88,
        'review_body': 'Delicious coffee! \n' +
        'For taste, Hannah you rock above Peet! Drove here specifically to order a cool cup of latte art...\n' +
        'I was disappointed As I was unable to...',
        "rating": 4,
        'created_at': '2022-09-17 11:14:17'
    },
    {
        'biz_id': 89,
        'review_body': 'Great food, service and staff. Highly recommend the food here. I always get the whole shabang triple X and it does not disappoint, the fries here are some...',
        "rating": 5,
        'created_at': '2022-09-11 20:53:28'
    },
    {
        'biz_id': 89,
        'review_body': "Not going to lie, when I first heard of this place I was like it's going to be just one of those bag of food places. I was right. It's mid at best.",
        "rating": 5,
        'created_at': '2022-08-26 23:48:40'
    },
    {
        'biz_id': 89,
        'review_body': 'The best!!\n' +
        'You need to come taste \n' +
        "It's always busy \n" +
        'So check in ahead \n' +
        'I drive far to come eat here',
        "rating": 5,
        'created_at': '2022-09-24 20:51:40'
    },
    {
        'biz_id': 90,
        'review_body': 'Friday is always family day. And today is a little extra special since we are treating Asian colleagues who really like to grill in the summer. Therefore,...',
        "rating": 4,
        'created_at': '2022-08-27 04:40:34'
    },
    {
        'biz_id': 90,
        'review_body': 'Fogo de chao walked so Taurinus can run (at least in my opinion)\n' +
        '\n' +
        'Taurinus has a very chic and upscale vibe. I think it suits many different type of...',
        "rating": 5,
        'created_at': '2022-04-24 07:58:15'
    },
    {
        'biz_id': 90,
        'review_body': 'Went here with a group of 8 on a Tuesday night and there was no issue getting a table. The restaurant has a pretty big selection of meats as well as a large...',
        "rating": 4,
        'created_at': '2022-08-21 15:07:08'
    },
    {
        'biz_id': 91,
        'review_body': 'We used Fo de Chao to cater a business lunch.  Aldo was great he answered all my questions about the menu, and the process to order.   He even called after...',
        "rating": 5,
        'created_at': '2022-08-24 09:56:21'
    },
    {
        'biz_id': 91,
        'review_body': 'Came here on a Tuesday afternoon and there were plenty of tables open. There is a parking structure right next to the restaurant so it made parking super...',
        "rating": 5,
        'created_at': '2022-10-06 11:23:45'
    },
    {
        'biz_id': 91,
        'review_body': 'Oh boy, this is a long overdue review. Imagine having an experience so bad that everybody in the party kept notes for you to add to the review, and you...',
        "rating": 1,
        'created_at': '2022-10-07 14:36:16'
    },
    {
        'biz_id': 92,
        'review_body': "I've frequented a few other sushi restaurants in the San Jose area, and this place strikes a pretty good balance between taste, ambiance, and price. \n" +
        '\n' +
        'My...',
        "rating": 4,
        'created_at': '2022-10-12 20:09:11'
    },
    {
        'biz_id': 92,
        'review_body': 'Enjoyable dinner and some good tasting fish, but a bit on the pricey side. \n' +
        '\n' +
        ' The chirashi bowl I ordered was on the expensive side, but it was also a...',
        "rating": 3,
        'created_at': '2022-10-11 19:23:21'
    },
    {
        'biz_id': 92,
        'review_body': 'It was my first time back here after over 5 years but it was just as I remembered. Growing up, mizu had always been a slight tier above the local sushi...',
        "rating": 4,
        'created_at': '2022-09-25 08:39:22'
    },
    {
        'biz_id': 93,
        'review_body': 'I love the basil fried rice here so much. This is their specialty!!! An absolute South Bay must!! \n' +
        '\n' +
        'I would usually get some sort of meat with this one but...',
        "rating": 5,
        'created_at': '2022-09-19 14:56:57'
    },
    {
        'biz_id': 93,
        'review_body': 'Always good nothing changed in last 10 years. \n' +
        'The prices are higher than formal restaurants if u order any dish to be make. 16.45 minimum for fried rice\n' +
        'U...',
        "rating": 5,
        'created_at': '2022-09-05 07:54:16'
    },
    {
        'biz_id': 93,
        'review_body': "Thai elephant doesn't look like much when you walk in. However, just like life how things look are not as important as how it is. This is a quick grab n go...",
        "rating": 4,
        'created_at': '2022-06-28 13:00:49'
    },
    {
        'biz_id': 94,
        'review_body': 'Small cozy modern place with limited seating inside and few tables on outside. Enough parking onsite. Do join the yelp waitlist before coming so that you...',
        "rating": 5,
        'created_at': '2022-10-02 10:23:38'
    },
    {
        'biz_id': 94,
        'review_body': 'yum food! loved this place\n' +
        '\n' +
        'I recommend\n' +
        '\n' +
        'papaya salad\n' +
        'panag curry\n' +
        'blue rice',
        "rating": 5,
        'created_at': '2022-10-01 17:39:34'
    },
    {
        'biz_id': 94,
        'review_body': 'Great new sister restaurant of Pineapple Thai. \n' +
        '\n' +
        'Small, but modern restaurant- come early since seating is limited so it fills up. There are a couple tables...',
        "rating": 5,
        'created_at': '2022-09-23 14:24:33'
    },
    {
        'biz_id': 95,
        'review_body': 'First time trying bun bo hue and I will definitely be back for more!!\n' +
        '\n' +
        'I heard many great things about this place and I never had bun bo hue before (my main...',
        "rating": 5,
        'created_at': '2022-10-05 09:45:20'
    },
    {
        'biz_id': 95,
        'review_body': 'Located near Little Saigon in San Jose, parking is plentiful and easy to find. The ambiance is your typical restaurant busyness. The noise level is...',
        "rating": 4,
        'created_at': '2022-09-24 19:42:05'
    },
    {
        'biz_id': 95,
        'review_body': 'I and my friend ordered Hu Tieu My NAm Vang Khô and they only bring My without Hu Tieu. I asked to fix, they brought a bowl of Hu Tiu and told me that it...',
        "rating": 1,
        'created_at': '2022-09-14 15:22:38'
    },
    {
        'biz_id': 96,
        'review_body': '100% vegetarian food. Very flavorful and lots of different variety. Owner is extremely nice.\n' +
        'Prices R very affordable as well.\n' +
        'My togo spot for vegetarian food',
        "rating": 5,
        'created_at': '2022-06-15 22:49:28'
    },
    {
        'biz_id': 96,
        'review_body': 'Service: 5/5 \n' +
        'Service was great! The staff there were kind and friendly. Food came out quick and hot! \n' +
        '\n' +
        'Food: 5/5 \n' +
        'a. Summer Roll - 5/5, $6\n' +
        'Sauce was...',
        "rating": 4,
        'created_at': '2022-07-17 20:15:41'
    },
    {
        'biz_id': 96,
        'review_body': 'My friends and I met up at this hole-in-the-wall for their vegan pho, and it definitely did not disappoint. Served hot and fresh, I was amazed at the sheer...',
        "rating": 5,
        'created_at': '2022-04-16 11:25:17'
    },
    {
        'biz_id': 97,
        'review_body': 'Yes. Yes. Yes. Owned by a charming, diligent and principled blue haired woman, the back story of this bustling sandwich shop and bakery is fascinating....',
        "rating": 5,
        'created_at': '2022-09-11 08:35:44'
    },
    {
        'biz_id': 97,
        'review_body': 'Everyone loves Bakesale Betty except for me.  Difficult street parking, Usually lines of diners anxiously wanting their fried chicken sandwich.  \n' +
        '\n' +
        "I didn't...",
        "rating": 3,
        'created_at': '2022-09-07 10:04:49'
    },
    {
        'biz_id': 97,
        'review_body': 'Since I found the time (and I was in the neighborhood) I decided to grab a friend chicken sandwich. Ohh it brought back memories!! It was probably better...',
        "rating": 5,
        'created_at': '2022-09-03 13:16:21'
    },
    {
        'biz_id': 98,
        'review_body': 'Fresh baked breads, pastries and pizza- oh my!\n' +
        '\n' +
        'This bakery provides the trifecta of baked goods- pizza, bread and pastries- all three of which I purchased...',
        "rating": 5,
        'created_at': '2022-10-10 14:29:08'
    },
    {
        'biz_id': 98,
        'review_body': 'I had a great mushroom pizza the other night that a friend picked up.  It hit the spot.\n' +
        '\n' +
        'That was all we got and all I really have to say.  If anyone is...',
        "rating": 5,
        'created_at': '2022-09-20 14:04:56'
    },
    {
        'biz_id': 98,
        'review_body': "One of my old time favorite bakeries I'm Oakland.\n" +
        '\n' +
        'I love all their breads but my heart keeps a special place for their grackle which they only serve on...',
        "rating": 5,
        'created_at': '2022-09-08 16:07:30'
    },
    {
        'biz_id': 99,
        'review_body': "My absolute FAVORITE place to get boba! They make beautifully curated and high quality tea drinks that aren't going to cost you $8 a drink (including the...",
        "rating": 5,
        'created_at': '2022-10-10 09:27:32'
    },
    {
        'biz_id': 99,
        'review_body': "This is definitely one of those hidden places. It's surrounded by many buildings that have been shut down and is the only building there with a line. I've...",
        "rating": 4,
        'created_at': '2022-09-24 22:09:22'
    },
    {
        'biz_id': 99,
        'review_body': 'Came here on a Saturday afternoon and ordered a green tea with salted cheese drink with 50% sweetness. The drink was really good, cheese added a nice milky,...',
        "rating": 5,
        'created_at': '2022-07-20 11:34:23'
    },
    {
        'biz_id': 100,
        'review_body': 'Really good. I had the Oreo ice cream egg puff and it was very delicious. The egg puff was crispy and the ice cream was just enough to cover the whole...',
        "rating": 5,
        'created_at': '2022-08-26 22:43:20'
    },
    {
        'biz_id': 100,
        'review_body': 'I love all of them. My son really happy to stay here. Here have many different desserts I can choose. My recommend the combo section opinion in past page of...',
        "rating": 5,
        'created_at': '2022-09-16 20:32:31'
    },
    {
        'biz_id': 100,
        'review_body': 'Best dessert place in Oakland! I always get the mango with chia and black sticky rice, and it never disappoints!',
        "rating": 5,
        'created_at': '2022-09-10 15:08:21'
    },
    {
        'biz_id': 101,
        'review_body': '"Next Level Bakery". Everything looked awesome. We got a sourdough loaf, French baguette, and some pastries.  Loved all of them. \n' +
        '\n' +
        'Would come out of our way...',
        "rating": 5,
        'created_at': '2022-07-30 13:21:26'
    },
    {
        'biz_id': 101,
        'review_body': "Cute little shop! No outdoor or indoor seating available. It's so small inside but they had a lot of yummy items to pick from! \n" +
        'The apple croissant was...',
        "rating": 4,
        'created_at': '2022-06-26 19:41:49'
    },
    {
        'biz_id': 101,
        'review_body': 'My 600th review goes to my favorite bakery for fruit tarts!\n' +
        '\n' +
        'This is the OG College Ave location at the boundary line of Berkeley/Oakland.  You can pull off...',
        "rating": 5,
        'created_at': '2022-01-27 22:11:16'
    },
    {
        'biz_id': 102,
        'review_body': "This place has always been a family favorite of mine!! We've been going for almost 15 years \n" +
        '\n' +
        'The waitlist for getting a table inside is usually not too...',
        "rating": 5,
        'created_at': '2022-09-24 16:13:13'
    },
    {
        'biz_id': 102,
        'review_body': "You know the deal! Piedmont's classic diner with feel-good food and ice cream. I dropped in for a post-lunch milkshake to go. \n" +
        '\n' +
        'I ordered a small vanilla...',
        "rating": 4,
        'created_at': '2022-10-02 20:20:35'
    },
    {
        'biz_id': 102,
        'review_body': "You know the FENTON'S featured in the movie Up? Well, it's this place! I wanted to come here because of the nostalgia of my college years going to the...",
        "rating": 5,
        'created_at': '2022-09-25 22:24:56'
    },
    {
        'biz_id': 103,
        'review_body': "If you're going to this expecting a cheap Thai meal.... Forget it!! Tasty but really expensive!",
        "rating": 4,
        'created_at': '2022-08-28 12:20:28'
    },
    {
        'biz_id': 103,
        'review_body': 'Ambiance - 5/5\n' +
        'Food - 5/5\n' +
        'Service - 5/5\n' +
        '\n' +
        'WOW!  Very impressed by this restaurant. Came with a party of 8 on a Sunday ~12pm. The restaurant was surprisingly...',
        "rating": 5,
        'created_at': '2022-10-09 16:23:17'
    },
    {
        'biz_id': 103,
        'review_body': 'Overhyped and overpriced. Farmhouse Kitchen Thai is one of the many trendy restaurants that attempt to wow people with extravagant presentation,...',
        "rating": 1,
        'created_at': '2022-10-04 23:04:04'
    },
    {
        'biz_id': 104,
        'review_body': 'Best Bay Area donuts by far. They have both cake and yeast raised donuts as well as filled. The wide variety and excellent quality have made me come back...',
        "rating": 5,
        'created_at': '2022-06-30 16:37:46'
    },
    {
        'biz_id': 104,
        'review_body': "Vegan Donut Gelato. Now those are three words you don't often see together. Why, I believe it would be an oxymoron were it not for the fact that somehow...",
        "rating": 4,
        'created_at': '2022-10-04 19:40:57'
    },
    {
        'biz_id': 104,
        'review_body': "I've had vegan donuts from a few different states and just happened upon this one while visiting dollar tree. \n" +
        '\n' +
        "So I'm a bit disappointed because they've...",
        "rating": 4,
        'created_at': '2022-10-02 08:57:49'
    },
    {
        'biz_id': 105,
        'review_body': 'Friendly staff and delicious custard and Italian ice! \n' +
        '\n' +
        'They were out of blue raspberry when. I went but I got strawberry Italian ice and vanilla custard....',
        "rating": 5,
        'created_at': '2022-06-10 20:52:38'
    },
    {
        'biz_id': 105,
        'review_body': 'Great local spot. Great bang for your buck with their $1 daily specials! One of the only places around to get legit frozen custard. Staff is super friendly.',
        "rating": 5,
        'created_at': '2022-09-25 15:20:00'
    },
    {
        'biz_id': 105,
        'review_body': 'My first time coming here. I walked right by it--it is on the eastern corner of the alley. When I walked in there was already a line of people getting their...',
        "rating": 5,
        'created_at': '2021-09-07 18:24:32'
    },
    {
        'biz_id': 106,
        'review_body': 'This place is a gem. Very high quality ingredients. Not like your regular sandwich shop. This guy cares. So refreshing to see an owner not cutting corners....',
        "rating": 5,
        'created_at': '2022-10-04 14:19:57'
    },
    {
        'biz_id': 106,
        'review_body': 'I tried this place with my boyfriend over the weekend and so glad we did.\n' +
        '\n' +
        'We tried both the tuna melt and Cuban and both were really delicious.\n' +
        '\n' +
        'The...',
        "rating": 5,
        'created_at': '2022-07-04 13:50:30'
    },
    {
        'biz_id': 106,
        'review_body': "Best Tuna Melt I've ever had. EVER! Everything from the tuna salad, to the pickles and bread used. The tuna salad is flavorful and balanced. It was...",
        "rating": 5,
        'created_at': '2022-06-08 09:35:43'
    },
    {
        'biz_id': 107,
        'review_body': 'Great gentleman waiter. Patient and understanding with us, being our first time there',
        "rating": 4,
        'created_at': '2022-09-06 16:49:18'
    },
    {
        'biz_id': 107,
        'review_body': "Ohgane is the classic spot for AYCE kbbq for berkeley students. I've been here once a couple of years ago, but came back again recently. They were able to...",
        "rating": 4,
        'created_at': '2022-09-24 17:15:49'
    },
    {
        'biz_id': 107,
        'review_body': 'Food: 5 stars \n' +
        'Service: 2 stars\n' +
        'Bathroom: 0 stars \n' +
        '\n' +
        "Some notes first on the night I'm writing this review on: \n" +
        '1. Tables were 3/4 filled. So not all that...',
        "rating": 4,
        'created_at': '2022-08-18 18:45:45'
    },
    {
        'biz_id': 108,
        'review_body': 'Got to check this place out with a few friends Friday evening. Luckily we got here right before the dinner rush.\n' +
        '\n' +
        'We got seated upstairs, assuming for...',
        "rating": 5,
        'created_at': '2022-10-12 18:20:15'
    },
    {
        'biz_id': 108,
        'review_body': "I've been to this place many times.  It is my once a week go to restaurant to eat at.  I love going by myself because I get all the Banchan to myself and...",
        "rating": 5,
        'created_at': '2022-09-27 16:13:55'
    },
    {
        'biz_id': 108,
        'review_body': "I cannot give them enough kuudooosss!!! I made RSVP's for my besties birthday and it was all around delicious and the customer service was excellent. I love...",
        "rating": 5,
        'created_at': '2022-09-26 10:18:35'
    },
    {
        'biz_id': 109,
        'review_body': "Totally agree with the recent reviews about Portal. My wife and I went back there recently and sat on the back patio. Sadly, I didn't take any pictures but...",
        "rating": 5,
        'created_at': '2022-09-20 16:25:27'
    },
    {
        'biz_id': 109,
        'review_body': 'Went to this place around 2-3 pm, and although the experience was pleasant, we waited quite a long time to be helped. Servers were really nice and helpful,...',
        "rating": 4,
        'created_at': '2022-10-05 13:12:13'
    },
    {
        'biz_id': 109,
        'review_body': "Came here for a second time yesterday with a girlfriend for brunch. The mimosa was good and the food was ok. There isn't much to choose from on the menu...",
        "rating": 2,
        'created_at': '2022-10-03 14:25:44'
    },
    {
        'biz_id': 110,
        'review_body': 'Fast service and great staff. \n' +
        '\n' +
        'Is a popular spot for after work fun. \n' +
        '\n' +
        'Try the rigatoni and the oxtail poutine.\n' +
        '\n' +
        'Street parking. Free on Sundays.',
        "rating": 4,
        'created_at': '2022-09-25 21:30:56'
    },
    {
        'biz_id': 110,
        'review_body': 'Gave me cold Nasty meatballs, weird texture meat. The lack of seasoning & sauce tastes like it has no tomatoes in it. We received this hot skillet with the...',
        "rating": 1,
        'created_at': '2022-09-28 13:26:16'
    },
    {
        'biz_id': 110,
        'review_body': 'I was impressed by the food we had.\n' +
        '\n' +
        'Oxtail poutine -5/5. Wow, really liked it. I hoped it was less pricey with less amount of food because I barely could...',
        "rating": 5,
        'created_at': '2022-09-03 14:08:37'
    },
    {
        'biz_id': 111,
        'review_body': "I'm leisurely walking and exploring the lovely Oakland area and as I'm leaving Jack London Square headed up Broadway I walk right into the one place...",
        "rating": 5,
        'created_at': '2022-09-05 08:41:14'
    },
    {
        'biz_id': 111,
        'review_body': 'This was such a weird experience. I had heard amazing things about Souley Vegan, and so my expectations were already high. We walked in on a weekday, and...',
        "rating": 2,
        'created_at': '2022-09-26 16:52:14'
    },
    {
        'biz_id': 111,
        'review_body': "Stayed in Downtown Oakland this weekend and was looking for a spot to eat. My 11yo nephew is vegan so we decided to try it out. It's walking distance from...",
        "rating": 4,
        'created_at': '2022-09-04 09:43:09'
    },
    {
        'biz_id': 112,
        'review_body': "Best burger in Oakland! If you're in the East Bay, gotta hit this spot. The True Deluxe burger is always on point and the workers provide good service.",
        "rating": 5,
        'created_at': '2022-08-31 09:13:10'
    },
    {
        'biz_id': 112,
        'review_body': "If you're looking for a juicy, well-seasoned, and consistent burger - then stop now!\n" +
        '\n' +
        'I have been hooked on this place since my internship days at Kaiser,...',
        "rating": 5,
        'created_at': '2022-07-31 22:04:35'
    },
    {
        'biz_id': 112,
        'review_body': 'True burger would get a five if they had real cheese!!!!American cheese has pork in it and I would prefer to have cheddar cheese or or jalapeño jack!  Some...',
        "rating": 4,
        'created_at': '2022-09-12 20:39:10'
    },
    {
        'biz_id': 113,
        'review_body': 'Aaron, thank you and your staff at Lucky duck so much. I had a last minute big order of bagels ( 20 assorted bagels  with cream cheese) and two 3 liter...',
        "rating": 5,
        'created_at': '2022-09-18 13:14:37'
    },
    {
        'biz_id': 113,
        'review_body': "We can't bike to Oakland or Alameda without finishing our day without having a cup of coffee at Luckyduck Bicycle Cafe.\n" +
        "It's a quiet friendly hangout place...",
        "rating": 4,
        'created_at': '2022-08-17 18:40:38'
    },
    {
        'biz_id': 113,
        'review_body': "I always take my friend to the dentist next door so I'd sometimes stop by to grab a coffee. Today the wait was longer than expected, so I decided to get a...",
        "rating": 1,
        'created_at': '2022-05-07 16:18:15'
    },
    {
        'biz_id': 114,
        'review_body': "Not gonna lie their chicken wing aka MBR wings beats fire wings chicken wing's easy .",
        "rating": 5,
        'created_at': '2022-09-11 19:17:21'
    },
    {
        'biz_id': 114,
        'review_body': 'Basically in love with everything here. Everything is soooooo fresh!!!  Service was great. Food also came really quick.',
        "rating": 5,
        'created_at': '2022-09-27 19:41:51'
    },
    {
        'biz_id': 114,
        'review_body': 'Its super filling and good, nice portions for the prices. Definitely will be coming back.',
        "rating": 4,
        'created_at': '2022-08-26 17:49:26'
    },
    {
        'biz_id': 115,
        'review_body': "This restaurant/bar is a perfect place to have dinner before going out to the bars in the area. I've celebrated two friends' birthdays here and I've always...",
        "rating": 4,
        'created_at': '2022-10-03 00:24:46'
    },
    {
        'biz_id': 115,
        'review_body': "Delayed birthday dinner with my fellow Leo. We really don't need a reason to dine but we make a point of celebrating ourselves. We're Leo's and the self...",
        "rating": 5,
        'created_at': '2022-10-02 10:46:41'
    },
    {
        'biz_id': 115,
        'review_body': "This was my first time visiting! I came here with friends for a quick bite before a concert nearby. I definitely wasn't disappointed with my meal!\n" +
        'I loved...',
        "rating": 5,
        'created_at': '2022-09-28 17:08:38'
    },
    {
        'biz_id': 116,
        'review_body': 'I prefer it even spicier, but it does bring me back to Taiwan I loved it :) I also tried sesame oil noodles which was pretty good',
        "rating": 5,
        'created_at': '2022-09-08 11:34:24'
    },
    {
        'biz_id': 116,
        'review_body': 'Hot day in Oakland stopped for some noodles.\n' +
        'The meal was amazing, fragrant, flavorful, and abundant!\n' +
        'The cheerful owner/cook came out to greet us and when...',
        "rating": 5,
        'created_at': '2022-09-05 15:27:49'
    },
    {
        'biz_id': 116,
        'review_body': 'Everything everyone in my party ordered was delicious! Would recommend to anyone visiting or if you are in the area',
        "rating": 5,
        'created_at': '2022-09-19 17:16:41'
    },
    {
        'biz_id': 117,
        'review_body': 'When we arrived at the restaurant, the hosts pointed us over to a table of two in the corner. We sat down and was greeted with water and hot tea. We decided...',
        "rating": 4,
        'created_at': '2022-09-08 13:53:52'
    },
    {
        'biz_id': 117,
        'review_body': 'This place is great\n' +
        '\n' +
        'Our friend from the east bay recommended it \n' +
        '\n' +
        'These were our favorites \n' +
        '\n' +
        'salt n pepper fish,\n' +
        'spicy sauce noodles, \n' +
        'walnut...',
        "rating": 5,
        'created_at': '2022-10-09 13:05:57'
    },
    {
        'biz_id': 117,
        'review_body': 'Always delicious. \n' +
        'Their dumplings and their hand-pulled noodles are next level. \n' +
        'Enjoy!',
        "rating": 5,
        'created_at': '2022-10-01 09:07:36'
    },
    {
        'biz_id': 118,
        'review_body': "It was my coworkers birthday and I needed to get her a cake, but she's gluten free. I was so happy when I found this bakery! Im always hesitant to try bake...",
        "rating": 5,
        'created_at': '2022-10-08 18:04:11'
    },
    {
        'biz_id': 118,
        'review_body': "There just isn't a better gluten free cinnamon roll! I also love their chicken pot pie, breads , pastas & ok really pretty much everything.  \n" +
        'The BLT : yum....',
        "rating": 5,
        'created_at': '2022-09-19 00:23:46'
    },
    {
        'biz_id': 118,
        'review_body': "Great food for all! Even if you aren't gluten free!\n" +
        '\n' +
        "This review is long overdue, but I'm so grateful for Mariposa! My boyfriend is celiac and honestly it's...",
        "rating": 5,
        'created_at': '2022-06-16 17:37:33'
    },
    {
        'biz_id': 119,
        'review_body': "I really love eating at this restaurant. Every time I'm able travel from LA to Oakland I always make a stop here. The staff are really friendly and helpful....",
        "rating": 5,
        'created_at': '2022-09-14 09:51:48'
    },
    {
        'biz_id': 119,
        'review_body': 'Caldo de res was delicious as well as the torta de carne. Good and friendly service. The prices were good as well',
        "rating": 5,
        'created_at': '2022-08-20 15:50:41'
    },
    {
        'biz_id': 119,
        'review_body': 'I just paid $20 for one skinny skimpy steak & shrimp burrito. Not worth it! $12 base price, but extras are $1 extra and I only added sour cream and cheese....',
        "rating": 2,
        'created_at': '2022-03-22 18:15:36'
    },
    {
        'biz_id': 120,
        'review_body': 'Quick, fast, efficient service! \n' +
        '\n' +
        'Best burgers and always cooked to perfection. \n' +
        '\n' +
        "Drive thru line can be extremely long and they'll still make it go by quickly.",
        "rating": 5,
        'created_at': '2022-10-11 18:53:38'
    },
    {
        'biz_id': 120,
        'review_body': 'Living on the east coast, I have heard legendary tales of how good In-N-Out Burgers are.  This is a chain of burger shops on the west coast.  On a recent...',
        "rating": 4,
        'created_at': '2022-07-15 15:04:42'
    },
    {
        'biz_id': 120,
        'review_body': "My burger was not as tasty as I expected. The fries were very hard and not tasty at all. I went through the drive-thru so I didn't notice my fries until I...",
        "rating": 3,
        'created_at': '2022-09-29 04:34:43'
    },
    {
        'biz_id': 121,
        'review_body': "Pretty good honest local burger joint if you're looking for one of those more moderate sized burgers. The location is normally great and with a great...",
        "rating": 4,
        'created_at': '2022-06-17 16:49:27'
    },
    {
        'biz_id': 121,
        'review_body': "Don't judge by the exterior!\n" +
        '\n' +
        "Ahn's is located in a small, moderately busy parking lot. There are usually a group of guys on the side of the building...",
        "rating": 3,
        'created_at': '2022-09-03 18:45:12'
    },
    {
        'biz_id': 121,
        'review_body': "Ahn's Quarter Pound Burger has been hiding in plain sight: everyone knows where it is and what it looks like, but it takes forever for people to finally...",
        "rating": 5,
        'created_at': '2022-03-12 15:54:43'
    },
    {
        'biz_id': 122,
        'review_body': 'OMG! \n' +
        "Literally the best halaal paki/Indian food I have ever had in my life. And that's saying a lot, because I've tried a lot and I am very picky. \n" +
        'They...',
        "rating": 5,
        'created_at': '2022-09-19 17:27:05'
    },
    {
        'biz_id': 122,
        'review_body': 'Food here is excellent, service is VERY slow.  Like many businesses in Oakland, they are understaffed. \n' +
        '\n' +
        'We ordered tandoori chicken, naan, chicken tikka...',
        "rating": 4,
        'created_at': '2022-08-29 09:41:09'
    },
    {
        'biz_id': 122,
        'review_body': "We ordered takeout during Ramadan, so I expected this halal restaurant to be extra busy. At first glance walking into the restaurant I wasn't sure what to...",
        "rating": 4,
        'created_at': '2022-06-12 14:40:44'
    },

    {
        'biz_id': 123,
        'review_body': 'The food and service here is exceptional! I was dining solo and ordered chicken momo, 2 chicken tandoori tikka with garlic naan. \n' +
        '\n' +
        'Everything was delicious!...',
        "rating": 5,
        'created_at': '2022-09-15 20:57:54'
    },
    {
        'biz_id': 123,
        'review_body': "My wife and I, along with two friends, found ourselves in downtown Oakland on a Sunday morning trying to find a restaurant with dine-in options.  It wasn't...",
        "rating": 4,
        'created_at': '2022-09-24 15:12:51'
    },
    {
        'biz_id': 123,
        'review_body': "I've gotten both take out and come here in person and both were great experiences! Most recently coming here in person, we came on a Friday night and we...",
        "rating": 4,
        'created_at': '2022-09-11 08:48:56'
    },
    {
        'biz_id': 124,
        'review_body': 'So glad I live near this place! My friends and I split the mushroom, the potatoes, and the corn pizzas.\n' +
        '\n' +
        'I think the corn seemed to be a big winner amongst...',
        "rating": 5,
        'created_at': '2022-07-29 23:34:00'
    },
    {
        'biz_id': 124,
        'review_body': "Ok so I've been here so many times but I think it's finally time to commit to not coming. Usually the food + service are amazing, which makes up for the...",
        "rating": 2,
        'created_at': '2022-07-18 18:15:42'
    },
    {
        'biz_id': 124,
        'review_body': "Stopped by here about a month ago with my girlfriend to grab some dinner after a movie. Wasn't expecting to have one of the best slices of pizza I've had...",
        "rating": 4,
        'created_at': '2022-06-22 06:57:04'
    },
    {
        'biz_id': 125,
        'review_body': "I have been here several times and it's always a 5 star experience. I can't even recommend anything in particular because it's all amazing. This last time I...",
        "rating": 5,
        'created_at': '2022-10-04 15:03:25'
    },
    {
        'biz_id': 125,
        'review_body': "What can I say, I'm drawn to homemade pasta with fresh ingredients. \n" +
        '\n' +
        'We started off with their beef tartar and it was raw and fresh and delicious and had a...',
        "rating": 4,
        'created_at': '2022-10-05 20:43:25'
    },
    {
        'biz_id': 125,
        'review_body': 'This "rating" has everything to do with the lack of communication between staff and myself.  It was on a Monday, at 5 pm I called and spoke to a lady staff....',
        "rating": 1,
        'created_at': '2022-09-21 18:13:14'
    },
    {
        'biz_id': 126,
        'review_body': 'Definitely one of the BEST ramen spots in the Bay Area. The broth is just so damn milky and fulfilling that my mouth is salivating at the thought of...',
        "rating": 5,
        'created_at': '2022-10-09 12:31:44'
    },
    {
        'biz_id': 126,
        'review_body': 'I really liked the Chicken Paitan ramen, broth was flavorful and the spice level was perfect (i asked for Medium). Chicken Karage was crispy and tasty,...',
        "rating": 4,
        'created_at': '2022-10-09 17:38:56'
    },
    {
        'biz_id': 126,
        'review_body': 'I am in love with this place! As a ramen lover (and vegetarian) i havent been able to find a ramen spot that seasons eir tofu befote putting it in the soup....',
        "rating": 5,
        'created_at': '2022-10-08 14:20:02'
    },
    {
        'biz_id': 127,
        'review_body': "What a find! Just a stone's throw off of Piedmont Ave, Geta Sushi is THE PERFECT little hole-in-the-wall joint!\n" +
        '\n' +
        'We slid into this itsy-bitsy place about a...',
        "rating": 5,
        'created_at': '2022-08-04 15:11:31'
    },
    {
        'biz_id': 127,
        'review_body': "Reliable sushi option, no frills. Nothing next level fancy but good option for rolls. Super packer at all times so you know fish ain't sitting around....",
        "rating": 4,
        'created_at': '2022-08-11 21:18:28'
    },
    {
        'biz_id': 127,
        'review_body': 'Ordered to go, its pricey.  Japanese food is notoriously pricey by nature due to its skilled cuts/ tedious food prep and unparalleled freshness. Ordered the...',
        "rating": 3,
        'created_at': '2022-08-02 22:23:46'
    },
    {
        'biz_id': 128,
        'review_body': "Love Wally's and the chicken salad is the best along with the free stack of dessert after the best soup yes sir",
        "rating": 5,
        'created_at': '2022-08-23 15:30:16'
    },
    {
        'biz_id': 128,
        'review_body': "Omgggggggosh! This restaurant has such a great menu, I ate here 2 days in a row after learning about it. Tried Wally's last night at an event, and the first...",
        "rating": 5,
        'created_at': '2022-09-02 13:41:50'
    },
    {
        'biz_id': 128,
        'review_body': "Hole in the wall Mediterranean/Lebanese food goodness- the best kind!  I love these kinds of spots because it adds to the place's character and you know...",
        "rating": 4,
        'created_at': '2022-09-06 08:06:42'
    },
    {
        'biz_id': 129,
        'review_body': 'stopped here randomly and thank god we did! \n' +
        'nice service and quality food! \n' +
        'everything we ordered came out so well seasoned.\n' +
        'please stop by if you get the...',
        "rating": 5,
        'created_at': '2022-09-24 15:14:44'
    },
    {
        'biz_id': 129,
        'review_body': 'Ambiance - 4/5\n' +
        'Service - 5/5\n' +
        'Food & drink - 4/5\n' +
        '\n' +
        'Had a good brunch at Shakewell. Max was our waiter and took great care of our party of four. Sad to hear...',
        "rating": 4,
        'created_at': '2022-10-02 16:32:22'
    },
    {
        'biz_id': 129,
        'review_body': 'This was my first time dining at Shakewell.  My new friend in the area says she always bring her out of town guest here. I know why now.\n' +
        'The food was...',
        "rating": 4,
        'created_at': '2022-10-02 07:49:03'
    },
    {
        'biz_id': 130,
        'review_body': "Bring cash and stop by! The best tacos are served here and even though inflation has hit this place like any other, you won't regret it (I remember tacos...",
        "rating": 5,
        'created_at': '2022-07-31 20:58:21'
    },
    {
        'biz_id': 130,
        'review_body': 'Rating: 3.5/5\n' +
        '\n' +
        'Pro:\n' +
        '- Good horchata\n' +
        '\n' +
        'Con:\n' +
        '- Limited parking\n' +
        '- A couple of people with housing insecurity are wandering around very close to you and your...',
        "rating": 3,
        'created_at': '2022-08-03 20:42:42'
    },
    {
        'biz_id': 130,
        'review_body': 'This place has really gone down hill they charge 3.50 a taco now when it used to be 2.25 they also charge 50 cents for salsa no matter how much you just...',
        "rating": 1,
        'created_at': '2022-08-03 15:30:54'
    },
    {
        'biz_id': 131,
        'review_body': "Honestly the best Central American food I've ever had. The seating area is adorable and the food is 10/10 as well as the service. This is my new favorite...",
        "rating": 5,
        'created_at': '2022-09-24 16:40:08'
    },
    {
        'biz_id': 131,
        'review_body': 'Wow, I been looking for this ever since I tried one in Puerto Rico. This is not exactly the same, but the closest I have found in the Bay Area. It was so...',
        "rating": 5,
        'created_at': '2022-10-11 22:59:51'
    },
    {
        'biz_id': 131,
        'review_body': 'They we doing good business when we were there but still many empty tables. The wait to order and get seated was reasonable. Convo at the register was...',
        "rating": 3,
        'created_at': '2022-10-02 21:24:41'
    },
    {
        'biz_id': 132,
        'review_body': "Zachary's has become my favorite pizza spot in Oakland for two key reason: amazing pizza with the best gluten free crust! \n" +
        '\n' +
        'Dined in for the first time last...',
        "rating": 5,
        'created_at': '2022-10-07 12:53:06'
    },
    {
        'biz_id': 132,
        'review_body': "I feel like Zachary's did a lot of things right and a few things wrong.\n" +
        '\n' +
        'I came late on a Thursday night at around closing hour with a group of 10+ and the...',
        "rating": 3,
        'created_at': '2022-10-07 03:13:38'
    },
    {
        'biz_id': 132,
        'review_body': "Zachary's Nostalgia!! This was a hot spot for deep dish pizza during college life at Berkeley and it was so fun to come back with the family! \n" +
        '\n' +
        'We got a...',
        "rating": 4,
        'created_at': '2022-09-25 08:19:41'
    },
    {
        'biz_id': 133,
        'review_body': 'My partner and I stopped here for a quick lunch. We got the Asian pear salad and chicken chopped salad...both were great and loaded with greens.  The staff...',
        "rating": 5,
        'created_at': '2022-08-27 17:06:07'
    },
    {
        'biz_id': 133,
        'review_body': 'Ordered the belly burrito for lunch earlier this week. I used to get a kimchi burrito almost every week from a cafe near my college when I was younger and I...',
        "rating": 4,
        'created_at': '2022-10-05 13:59:04'
    },
    {
        'biz_id': 133,
        'review_body': 'THIS IS THE BEST CALI BURRITO IN OAKLAND! Being from San Diego, I definitely ate my share of authentic cali burritos and this one definitely takes the cake...',
        "rating": 5,
        'created_at': '2022-07-27 16:28:10'
    },
    {
        'biz_id': 134,
        'review_body': 'This small family-owned place has amazing food, drinks, and service. The shrimp corncakes blew me away, and the twice-cooked Maine lobster was so delicious....',
        "rating": 5,
        'created_at': '2022-09-14 11:48:11'
    },
    {
        'biz_id': 134,
        'review_body': "I went based on the revies...people love this place. Unfortunately,  I'm not people. I was confused. We had the shrimp pancakes. Lobster roll and seafood...",
        "rating": 2,
        'created_at': '2022-09-25 10:56:23'
    },
    {
        'biz_id': 134,
        'review_body': 'We chose this place solely on the yelp reviews and ratings and were extremely disappointed.  \n' +
        '\n' +
        '1-upon arrival (before 5:45pm) the older lady working the...',
        "rating": 3,
        'created_at': '2022-09-25 10:34:05'
    },
    {
        'biz_id': 135,
        'review_body': 'Took my parents here about 10 years ago. I had never been either as I lived in NV and they lived in OH. This is one of THE BEST RESTAURANTS IN THE...',
        "rating": 5,
        'created_at': '2022-10-07 20:07:31'
    },
    {
        'biz_id': 135,
        'review_body': 'We came here with a big group for a birthday and it was my first time here, so I was really excited. The wait, even with reservations was expected for our...',
        "rating": 5,
        'created_at': '2022-10-06 18:27:17'
    },
    {
        'biz_id': 135,
        'review_body': 'My go-to Prime Rib spot!! Food is great!!! They cut the meat in front of you and prepare the salad in front of you too. Probably my fav salad ever as well,...',
        "rating": 5,
        'created_at': '2022-10-05 16:04:10'
    },
    {
        'biz_id': 136,
        'review_body': 'Great Dinner. Surprised my wife who is Brazilian, visiting from LA, but I lived in Oakland 00-05. So wanted to see the old spots, but wanted to find a...',
        "rating": 5,
        'created_at': '2022-08-19 22:11:06'
    },
    {
        'biz_id': 136,
        'review_body': "If you're contemplating an evening dining experience where you're treated with food and respect that's worth $70+ per person, run, don't walk, away from...",
        "rating": 1,
        'created_at': '2022-10-07 20:54:58'
    },
    {
        'biz_id': 136,
        'review_body': "We went on a Friday night and we're a party of five with no reservation . Big mistake - we waited around for over 45 min.\n" +
        '\n' +
        'Then after 45 min of waiting we...',
        "rating": 1,
        'created_at': '2022-10-02 21:54:42'
    },
    {
        'biz_id': 137,
        'review_body': 'Favorite neighborhood sushi spot! \n' +
        '\n' +
        'No wait on this Saturday around 12:30pm. Was seated, ordered, and served all within 10-15 minutes. \n' +
        '\n' +
        'Fish is fresh,...',
        "rating": 5,
        'created_at': '2022-05-28 13:09:16'
    },
    {
        'biz_id': 137,
        'review_body': "A joyful creative roll spot, if you're into that. They refill your tea cup, are very friendly and welcoming, and have a long list of yummy rolls. \n" +
        '\n' +
        'It helps...',
        "rating": 4,
        'created_at': '2022-07-10 11:30:29'
    },
    {
        'biz_id': 137,
        'review_body': 'Pleased again. Ordered same rolls from Saturday; \n' +
        "2 Philly rolls & Tekka for Mom / Shrek & Lion King roll for me. I wish they'd cook the salmon a little...",
        "rating": 5,
        'created_at': '2022-09-29 09:01:08'
    },
    {
        'biz_id': 138,
        'review_body': '33. Tom Yum Soup \n' +
        '7. Lao Tacos\n' +
        '72. Basil Fried Rice\n' +
        'Yummy ! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!??!???????',
        "rating": 5,
        'created_at': '2022-08-28 15:20:09'
    },
    {
        'biz_id': 138,
        'review_body': 'One of my favorite authentic Laotian place in the Bay Area. \n' +
        '\n' +
        'Decided to pick up food around 2:30pm and took about 25 mins. Ordered the following below....',
        "rating": 5,
        'created_at': '2022-10-01 22:53:53'
    },
    {
        'biz_id': 138,
        'review_body': "This hole in the wall is my favorite place for Thai food. The parking is a bit rough but it's worth it. The fact that there's a bunch of cars double parked...",
        "rating": 4,
        'created_at': '2022-08-07 16:53:43'
    },
    {
        'biz_id': 139,
        'review_body': "Best vegan asian fusion food hands down! Amazing amount of meat replacement options. Great quality & flavor. I hadn't eaten here in five years and it was...",
        "rating": 5,
        'created_at': '2022-07-17 09:08:56'
    },
    {
        'biz_id': 139,
        'review_body': 'Not sure why this place has five stars.\n' +
        '\n' +
        "Is it because it's the best vegan restaurant? Probably not. Is it because it's one of the only ones around?...",
        "rating": 3,
        'created_at': '2022-09-30 22:22:31'
    },
    {
        'biz_id': 139,
        'review_body': 'I generally only write reviews IF product/service is very, very good, OR, very, very bad.  Golden Lotus was very, very good!\n' +
        'Dined in with 3 of my...',
        "rating": 5,
        'created_at': '2022-07-11 13:28:13'
    },
    {
        'biz_id': 140,
        'review_body': 'Best pizza ever\n' +
        "Love the people there, love the pizza, love that it's local, it's just the perfect pizza place",
        "rating": 5,
        'created_at': '2022-08-25 19:06:55'
    },
    {
        'biz_id': 140,
        'review_body': 'Their food has real fresh veggies in it. Their pizza is reliably good. Their salads are big and have lots of good stuff, not just a bunch of spring mix....',
        "rating": 5,
        'created_at': '2022-09-06 22:50:34'
    },
    {
        'biz_id': 140,
        'review_body': "I crave Dimond Slice on so many random weekdays. Every day, they always have a different pizza but it's ALWAYS good I just don't get it. If pizza were...",
        "rating": 5,
        'created_at': '2022-08-18 13:39:38'
    },
    {
        'biz_id': 141,
        'review_body': 'The people who work at this restaurant go above and beyond, they are AMAZING! They make you feel at home and are so welcoming. While we were waiting for our...',
        "rating": 5,
        'created_at': '2022-08-29 10:37:17'
    },
    {
        'biz_id': 141,
        'review_body': 'Their pho is delicious and their new space is super cool with a bunch of cool stuff like a swag store. This is one of my favorite places in the Bay Area for...',
        "rating": 5,
        'created_at': '2022-09-13 20:12:00'
    },
    {
        'biz_id': 141,
        'review_body': "We ordered two bowls of beef pho to go and waited 25 minutes for the order to come out, which is perplexing because it's not like they were making the broth...",
        "rating": 2,
        'created_at': '2022-10-10 14:36:09'
    },
    {
        'biz_id': 142,
        'review_body': "Best sandwich I've tried anywhere would recommend this to everyone taste better than any other Vietnamese sandwich places I been too",
        "rating": 5,
        'created_at': '2022-09-18 22:01:29'
    },
    {
        'biz_id': 142,
        'review_body': 'Just a tip 9/23/22 they are **closed until 9/30/22**\n' +
        '\n' +
        'Drove over today and was excited no line out the door at 1pm. Nope, just closed  \n' +
        'Saw a sign closed...',
        "rating": 5,
        'created_at': '2022-09-23 22:07:44'
    },
    {
        'biz_id': 142,
        'review_body': "#2 special combo ham sandwich was great. Bread was thick and crispy, and the pate was really something --smooth and creamy and rich, and I'm glad to...",
        "rating": 5,
        'created_at': '2022-09-10 20:39:22'
    },
    {
        'biz_id': 143,
        'review_body': 'First off pastries were FANTASTIC. Coffee was good (I got a macchiato and it was a littler smaller than I thought but was great) and the vibe was fun,...',
        "rating": 5,
        'created_at': '2022-08-28 19:34:47'
    },
    {
        'biz_id': 143,
        'review_body': "Born and raised in the Bay, occasionally I surprise myself with well-known San Francisco establishments that I've never visited before--B Patisserie being...",
        "rating": 5,
        'created_at': '2022-10-06 18:10:09'
    },
    {
        'biz_id': 143,
        'review_body': "Looove this place! I thought the pastries were so fresh and so delicious, we only had to stand in line for about 15 minutes. They weren't warm, but I'm sure...",
        "rating": 5,
        'created_at': '2022-10-02 17:59:19'
    },
    {
        'biz_id': 144,
        'review_body': 'I am not typically a fan of pastries, but this has to be one of my favorite bakeries. I got the almond lemon cake and banana cream tart which were both...',
        "rating": 4,
        'created_at': '2022-09-15 06:35:39'
    },
    {
        'biz_id': 144,
        'review_body': '9/27/2022 I went this morning. I told the staff my order. I wanted a chocolate crème pie and a few other items. The lady helping was talking to another...',
        "rating": 5,
        'created_at': '2022-09-27 13:39:04'
    },
    {
        'biz_id': 144,
        'review_body': 'Went to Tartine an SF institution the other day. And got a biiiiig spread of stuff!\n' +
        '\n' +
        'Started off w a cute lil cappuccino and look how cute!! This lil guy...',
        "rating": 4,
        'created_at': '2022-10-08 12:56:00'
    },
    {
        'biz_id': 145,
        'review_body': 'It was quite busy on the heat waved Sunday but it was worth the wait. My sister and I wanted a #12 (?) with corn flakes, who the cashier kindly told us that...',
        "rating": 5,
        'created_at': '2022-09-11 19:48:21'
    },
    {
        'biz_id': 145,
        'review_body': 'You are heading straight into a tourist trap here, fellow Yelper. Not a total loss though because the ice cream inside the crepe is pretty good (at least...',
        "rating": 4,
        'created_at': '2022-08-14 16:51:15'
    },
    {
        'biz_id': 145,
        'review_body': 'What can I say? Belly Good Crepes are the best crepes in Japan town - straight up and the most cute looking as well. \n' +
        '\n' +
        'Been going for years. Consistent with...',
        "rating": 5,
        'created_at': '2022-08-12 04:44:37'
    },
    {
        'biz_id': 146,
        'review_body': "This is my go to spot whenever I'm craving matcha! My usual order is the matcha boba sundae, which consists of soft serve, boba, and kuromitsu syrup...",
        "rating": 5,
        'created_at': '2022-10-07 20:31:29'
    },
    {
        'biz_id': 146,
        'review_body': "After writing down a review for Sac's location, I thought might as well give a good review for the SF location as well! This is one of the best location for...",
        "rating": 5,
        'created_at': '2022-10-06 11:28:07'
    },
    {
        'biz_id': 146,
        'review_body': 'Tried the maiko special with the matcha - vanilla mix ice cream. I liked the ice cream but was not a fan of most of the toppings. I would probably just...',
        "rating": 4,
        'created_at': '2022-10-03 21:49:12'
    },
    {
        'biz_id': 147,
        'review_body': 'Found this lovely quaint dessert spot in SF. Tried the coconut pandan crepe cake and loved it ! Definitely recommended',
        "rating": 5,
        'created_at': '2022-08-27 18:13:16'
    },
    {
        'biz_id': 147,
        'review_body': "I came here at 5 o'clock on a Friday to order a birthday cake and also try one of their sweets.\n" +
        '\n' +
        "To be honest, I didn't like the toasted cereal with honey...",
        "rating": 4,
        'created_at': '2022-09-09 07:33:26'
    },
    {
        'biz_id': 147,
        'review_body': 'Friendly, Great service and reasonable prices. Will be back again . Mango sticky rice is my favorite',
        "rating": 5,
        'created_at': '2022-09-19 20:00:49'
    },
    {
        'biz_id': 148,
        'review_body': 'Lives up to the hype!\n' +
        '\n' +
        "I found this modest corner coffee shop selling odds and ends (in terms of snacks) on Yelp. I haven't had baklava in forever since...",
        "rating": 5,
        'created_at': '2022-05-05 11:42:14'
    },
    {
        'biz_id': 148,
        'review_body': 'I love Turkish coffee and every day I start my day with a 12-ounce cup of Turkish coffee, and for the rest of the day, I must drink 1-2 8-ounce cups.  I...',
        "rating": 2,
        'created_at': '2022-09-23 16:21:27'
    },
    {
        'biz_id': 148,
        'review_body': 'I am hooked to Turkish coffee. Therefore, whenever I see one available, I would find a way to try it. After passing by on this shop for couple of times, I...',
        "rating": 4,
        'created_at': '2021-10-28 21:21:43'
    },
    {
        'biz_id': 149,
        'review_body': 'The service was great, the food was wonderful.  I took my family here and had been anticipating the pork chops.  It did not disappoint us at all!  You gotta...',
        "rating": 5,
        'created_at': '2022-09-18 10:25:30'
    },
    {
        'biz_id': 149,
        'review_body': 'Nopa is a restaurant that focuses on combining quality, seasonal ingredients without over amplifying their menu. I got their smoked tomato Caesar salad,...',
        "rating": 5,
        'created_at': '2022-09-13 20:55:09'
    },
    {
        'biz_id': 149,
        'review_body': 'Great service here. Staff were very attentive. I spent ~$100 with entree and dessert, splitting appetizers, $125 riseling (that I was told is hard to find),...',
        "rating": 4,
        'created_at': '2022-10-05 00:10:18'
    },
    {
        'biz_id': 150,
        'review_body': "Loved going to Bob's for breakfast. I heard about it through a Someone Feed Phil recommendation and knew I had to go. \n" +
        '\n' +
        'It will always look like a long line...',
        "rating": 5,
        'created_at': '2022-10-12 07:24:33'
    },
    {
        'biz_id': 150,
        'review_body': 'Truly the best donuts in the SF bay!\n' +
        '\n' +
        "Try to go earlier in the evening for their specialty donuts! We did order the massive donut however it's flavor is...",
        "rating": 5,
        'created_at': '2022-10-10 02:12:27'
    },
    {
        'biz_id': 150,
        'review_body': "Just wow. The best doughnuts in SF, most likely the US. It's open 24 hours a day, so instead of choosing something, just ask for whatever is fresh. \n" +
        '\n' +
        'The...',
        "rating": 5,
        'created_at': '2022-10-04 11:23:03'
    },
    {
        'biz_id': 151,
        'review_body': "Incredible small batch ice cream. Well worth the wait, no matter how long the line is. If it's your first time, get ice cream on a donut with toasted fluff.",
        "rating": 5,
        'created_at': '2022-09-04 22:56:13'
    },
    {
        'biz_id': 151,
        'review_body': '"Some people are worth melting for." - Olaf\n' +
        '\n' +
        "Urban Legend says that there's a small quirky Ice Cream shop in the middle of who knows where San Francisco...",
        "rating": 5,
        'created_at': '2022-10-10 17:10:45'
    },
    {
        'biz_id': 151,
        'review_body': 'What a treat! What a dream!\n' +
        '\n' +
        'Excellent customer service. Be ready to wait in line, but totally worth it.',
        "rating": 5,
        'created_at': '2022-08-21 20:27:40'
    },
    {
        'biz_id': 152,
        'review_body': "some of the best ice cream i've ever had.  insanely long line, but, worth it\n" +
        '\n' +
        'you can get lots of mini-scoops instead of regular scoops to get more flavors....',
        "rating": 5,
        'created_at': '2022-10-04 16:42:41'
    },
    {
        'biz_id': 152,
        'review_body': 'Really unique flavors -- I LOVED the ritual coffee toffee flavor, which had a strong coffee flavor with a nutty taste and really delicious toffee bits...',
        "rating": 4,
        'created_at': '2022-10-02 11:17:03'
    },
    {
        'biz_id': 152,
        'review_body': "We love Bi-Rite Creamery, especially for their sundaes and banana splits.  We've had a number of their ice cream flavors and they have all been good.  The...",
        "rating": 4,
        'created_at': '2022-09-23 12:09:34'
    },
    {
        'biz_id': 153,
        'review_body': "This is definitely a local's favorite. There's nothing like this place in SF. I suggest the mango ice cream.",
        "rating": 5,
        'created_at': '2022-09-20 16:53:32'
    },
    {
        'biz_id': 153,
        'review_body': "Some of the best ice cream I've ever had. You get a decent amount in one scoop, especially if you get it in a cone. I got the strawberries and cream and it...",
        "rating": 5,
        'created_at': '2022-09-25 07:28:18'
    },
    {
        'biz_id': 153,
        'review_body': "Simply the GOAT of ice cream in San Francisco. Consistently fresh, creamy and tastes just like the actual flavor it's supposed to be. \n" +
        '\n' +
        'Waiting in line on a...',
        "rating": 5,
        'created_at': '2022-10-08 15:31:50'
    },
    {
        'biz_id': 154,
        'review_body': "I usually steer away from vegan restaurants since I love meat but this restaurant amazed me. I've already visited this place twice in the last two weeks and...",
        "rating": 5,
        'created_at': '2022-09-23 20:35:00'
    },
    {
        'biz_id': 154,
        'review_body': "My confession is that I don't normally go to vegan restaurants. Not only can I not imagine life without cheese, but I also have severe allergies that...",
        "rating": 4,
        'created_at': '2022-08-29 20:35:18'
    },
    {
        'biz_id': 154,
        'review_body': "Honestly every dish I've tried here is amazing, authentic and made with such care - you can tell they make most things in house from scratch. \n" +
        '\n' +
        'The Saigon...',
        "rating": 5,
        'created_at': '2022-08-01 12:29:12'
    },
    {
        'biz_id': 155,
        'review_body': 'Underrated comfortable bar. Perfect for food, drink and hanging out.\n' +
        '\n' +
        'Effortless good times here. It reminds me of the kind of bars in Germany. Friendly...',
        "rating": 5,
        'created_at': '2022-09-19 21:59:07'
    },
    {
        'biz_id': 155,
        'review_body': "So sad Broken Record will be closing, and I JUST found out about Tiki Tuesdays! It's not all-out tiki, but fun for dive bar tiki. Drinks weren't amazing but...",
        "rating": 4,
        'created_at': '2022-10-12 23:19:57'
    },
    {
        'biz_id': 155,
        'review_body': '4-19-2022 7p.m.\n' +
        '1st time here...will be back!!!\n' +
        'Went here to meet  a date for drinx...\n' +
        'got stood up, story of my life...\n' +
        'Walked into a lively low lit bar &...',
        "rating": 5,
        'created_at': '2022-04-30 13:51:10'
    },
    {
        'biz_id': 156,
        'review_body': "looking for a spot for traditional Korean cuisines? Han Il Kwan doesn't get more traditional than this. served with delicious ban chans, tofu soup, steamed...",
        "rating": 5,
        'created_at': '2022-10-12 23:22:41'
    },
    {
        'biz_id': 156,
        'review_body': "One of the better kbbq places I've been to, definitely recommend. Their bulgogi, kimchi pancakes and the free tofu soup are awesome. If you need the help,...",
        "rating": 4,
        'created_at': '2022-10-13 07:42:09'
    },
    {
        'biz_id': 156,
        'review_body': 'Stopped by here for a friends birthday dinner this past Sunday.\n' +
        '\n' +
        'We were a fairly large group (12 of us) and the restaurant was kind enough to accommodate...',
        "rating": 4,
        'created_at': '2022-10-12 07:52:27'
    },
    {
        'biz_id': 157,
        'review_body': 'Ah Brenda... you did not disappoint. \n' +
        'Fried Chicken...ooo la La. \n' +
        'Flaky buttery pillowy biscuits that are the perfect foil for homemade jam and hot pepper...',
        "rating": 5,
        'created_at': '2022-10-09 09:33:09'
    },
    {
        'biz_id': 157,
        'review_body': 'Service was horrible from our server, others accommodated everything we needed beyond placing our order. \n' +
        '\n' +
        'Drinks came out after our meals. The beignets...',
        "rating": 3,
        'created_at': '2022-10-10 05:28:31'
    },
    {
        'biz_id': 157,
        'review_body': 'We arrived as a party of 6 at about 1pm. They had a waiting list, but let us in after just few minutes. The restaurant is very clean even-though it was very...',
        "rating": 4,
        'created_at': '2022-10-09 16:18:23'
    },
    {
        'biz_id': 158,
        'review_body': 'Wonderful establishment......fantastic food and terrific staff.....thank you SM............',
        "rating": 5,
        'created_at': '2022-09-07 11:36:23'
    },
    {
        'biz_id': 158,
        'review_body': 'Sweet maple is one of the best breakfast spots in SF\n' +
        '\n' +
        'The blackwood Benedict and the south of the\n' +
        'border dishes are REALLY good\n' +
        '\n' +
        'I heard they might have...',
        "rating": 5,
        'created_at': '2022-10-12 21:53:18'
    },
    {
        'biz_id': 158,
        'review_body': 'I usually go to the Palo Alto location but decided to try this one out for Sunday brunch! \n' +
        'I think the biggest difference would be the actual items on the...',
        "rating": 4,
        'created_at': '2022-10-10 18:46:44'
    },
    {
        'biz_id': 159,
        'review_body': 'Came here on a lovely Friday evening. No reservations, first come first serve. But we were flexible with our seating so we were open to bar seating for...',
        "rating": 5,
        'created_at': '2022-09-29 20:04:12'
    },
    {
        'biz_id': 159,
        'review_body': 'Super cute French bistro in Potrero. A great stop for a glass of wine and a delicious light lunch/dinner or a full on hearty meal. My friend and I enjoyed...',
        "rating": 5,
        'created_at': '2022-09-29 10:02:12'
    },
    {
        'biz_id': 159,
        'review_body': "Such a gem! Cute little French restaurant with both indoor and outdoor seating. Simple and tasty menu that doesn't break the bank. So many over priced...",
        "rating": 5,
        'created_at': '2022-09-24 19:40:55'
    },
    {
        'biz_id': 160,
        'review_body': 'Delicious burritos! Had the Spicy Pork and the Bulgogi. Loved both but the Bulgogi Burrito won the day. \n' +
        '\n' +
        'Juicy flavorful meat, kimchi was good but not...',
        "rating": 5,
        'created_at': '2022-09-07 07:05:29'
    },
    {
        'biz_id': 160,
        'review_body': 'This place is solid for Asian fusion food! They have Asian inspired proteins including panko-crusted shrimp, wild cod katsu, tuna poke, and bulgogi beef....',
        "rating": 5,
        'created_at': '2022-06-22 21:29:43'
    },
    {
        'biz_id': 160,
        'review_body': 'We to HRD for a quick lunch, after looking at the different reviews and getting excited for a unique burrito! Once there you basically order and get a...',
        "rating": 4,
        'created_at': '2022-06-20 13:32:48'
    },
    {
        'biz_id': 161,
        'review_body': 'Best food ever!!!\r\r Recently try the famous San Tung! ;)\n' +
        'Place with the best fried chicken.',
        "rating": 5,
        'created_at': '2022-09-15 00:29:16'
    },
    {
        'biz_id': 161,
        'review_body': 'I was in San Francisco this past weekend for a concert and I was highly recommend to come here by one of my friends to try their famous fried chicken and...',
        "rating": 5,
        'created_at': '2022-10-12 00:55:15'
    },
    {
        'biz_id': 161,
        'review_body': "Their dry fried chicken is hands down one of the best fried chicken I've ever had. \n" +
        '\n' +
        'I was craving their chicken wings and luckily some of my friend were...',
        "rating": 5,
        'created_at': '2022-10-11 09:17:40'
    },
    {
        'biz_id': 162,
        'review_body': '4.5 stars rounded up \n' +
        '\n' +
        'If plain chicken & waffles bore you to death, the flavor options at Hot Sauce & Panko are sure to liven up your life, or at the very...',
        "rating": 5,
        'created_at': '2022-10-07 02:36:47'
    },
    {
        'biz_id': 162,
        'review_body': 'Tried hot sauce and Panko for the first time and it exceeded my expectations.\n' +
        '\n' +
        'The chicken was very high quality. We got the lemon pepper boneless wings,...',
        "rating": 5,
        'created_at': '2022-09-21 19:14:39'
    },
    {
        'biz_id': 162,
        'review_body': 'The food was okay!\n' +
        '\n' +
        "I got a BBQ sauced chicken sandwich (one of three flavors), fries, and wing order with Chris's sauce.\n" +
        '\n' +
        'Everything was lacking a pow...',
        "rating": 3,
        'created_at': '2022-09-12 07:55:41'
    },
    {
        'biz_id': 163,
        'review_body': 'I read a lot of mixed reviews on here and the bad ones mostly discussed poor quality and old restaurant. This is an AFFORDABLE and DECENTLY GOOD place for...',
        "rating": 4,
        'created_at': '2022-09-20 23:03:37'
    },
    {
        'biz_id': 163,
        'review_body': 'Generous portion for an amazing price! We went on a Saturday around noon, and the line was pretty. But it moved relatively fast. This place has no tables or...',
        "rating": 5,
        'created_at': '2022-10-10 20:21:44'
    },
    {
        'biz_id': 163,
        'review_body': "My favorite Chinese bakery in Chinatown, and I've been to almost all of them. Listen, I don't think any authentic Chinese bakery is ever going to have mind...",
        "rating": 5,
        'created_at': '2022-10-09 22:14:33'
    },
    {
        'biz_id': 164,
        'review_body': 'One of favorite Vegetarian restaurants.  Food is great, well prepared.\n' +
        '\n' +
        'Dining experience was definitely degraded by not partaking in the amazing view...',
        "rating": 5,
        'created_at': '2022-09-22 17:57:26'
    },
    {
        'biz_id': 164,
        'review_body': 'Greens was absolutely delicious, the waiter was very thoughtful, and the sunset view was amazing! \n' +
        '\n' +
        'Came here for my birthday dinner with a group of 5. We...',
        "rating": 4,
        'created_at': '2022-09-21 18:34:05'
    },
    {
        'biz_id': 164,
        'review_body': "Couples date at Greens and we were a little late because we didn't realize how difficult parking would be here. That was our bad, of course it's SF. Lol....",
        "rating": 5,
        'created_at': '2022-08-18 19:31:29'
    },
    {
        'biz_id': 165,
        'review_body': 'I had many questions.  Is Cordon Bleu French food? Why does it look like a diner inside? Why are their hours so odd?  Is that line worth the hype?\n' +
        '\n' +
        'Turns...',
        "rating": 5,
        'created_at': '2022-09-26 11:42:40'
    },
    {
        'biz_id': 165,
        'review_body': 'Katie is a godsend. Faithfully serving up delicious affordable grub to an appreciative crowd day in and day out. After leaving the city for more affordable...',
        "rating": 5,
        'created_at': '2022-08-04 00:24:11'
    },
    {
        'biz_id': 165,
        'review_body': 'Not only delicious food, but such a friendly, intimate space for eating. Your classic hole-in-the-wall gem of a restaurant, the space has only an 8-seat...',
        "rating": 5,
        'created_at': '2022-07-29 08:58:45'
    },
    {
        'biz_id': 166,
        'review_body': 'Not sure if I will make effort to return and here is why. \n' +
        '\n' +
        'PARKING\n' +
        "I came on a Sunday because I was in the area. Almost didn't make it because parking was...",
        "rating": 4,
        'created_at': '2022-10-10 08:19:36'
    },
    {
        'biz_id': 166,
        'review_body': 'I went to dinner with some friends here.  The food was different and very tasty.  The entrees ranged from small to a full meal.  We got the nachos as an...',
        "rating": 5,
        'created_at': '2022-10-01 15:07:28'
    },
    {
        'biz_id': 166,
        'review_body': 'This was my first time trying an arepa, and it was great! I ordered the sweet yellow arepa with the shuli filling. Normally, when I order vegan food at a...',
        "rating": 5,
        'created_at': '2022-08-24 19:06:34'
    },
    {
        'biz_id': 167,
        'review_body': 'Updated review: after my previous visit and review, the owner got in touch with me. He was very apologetic, and he offered to send me another meal to make...',
        "rating": 5,
        'created_at': '2022-09-28 19:15:33'
    },
    {
        'biz_id': 167,
        'review_body': 'Went with a large group on a quiet Sunday evening. We happened to be in the area and wanted Indian food, which is how we ended up at North India. There was...',
        "rating": 4,
        'created_at': '2022-09-01 00:22:23'
    },
    {
        'biz_id': 167,
        'review_body': 'Dined here randomly as they were open late at night.\n' +
        '\n' +
        'As soon as we walked in, there was a great aroma inside.  The place was very clean, super cozy, and...',
        "rating": 5,
        'created_at': '2022-08-27 22:12:07'
    },
    {
        'biz_id': 168,
        'review_body': 'Came here on a Thursday evening. We were on the earlier side - probably around 545 pm and were the only ones in the restaurant. Staff was friendly.\n' +
        '\n' +
        'We were...',
        "rating": 5,
        'created_at': '2022-05-17 08:02:25'
    },
    {
        'biz_id': 168,
        'review_body': 'Nice spot for some unique cuisine. The flavors are legitimate and they have a good kick of spice! They have high chairs, but we were the only group with...',
        "rating": 4,
        'created_at': '2022-06-07 14:28:28'
    },
    {
        'biz_id': 168,
        'review_body': 'Ordered takeout on a Saturday around 6:30P and the food was ready in 15 minutes! Decent prices and delicious food. Only ordered one combo and the other a la...',
        "rating": 4,
        'created_at': '2022-05-07 20:29:14'
    },
    {
        'biz_id': 169,
        'review_body': "We have ordered from here before, but tonight we ordered and the pizza wasn't cooked the whole way through. The first bite tasted like dough. Super...",
        "rating": 3,
        'created_at': '2022-09-02 19:56:56'
    },
    {
        'biz_id': 169,
        'review_body': "Called the phone order, and the guy was hilarious. But let's get to the point:\n" +
        'Pizza: awesome! Great choices, loved the square design, and it was incredibly...',
        "rating": 5,
        'created_at': '2022-10-10 18:53:33'
    },
    {
        'biz_id': 169,
        'review_body': 'heard good things about this place so I dropped by!\n' +
        '\n' +
        "it's considerablt easy to get here by bus, and it's relativity close to the city center!\n" +
        '\n' +
        'I ordered the...',
        "rating": 4,
        'created_at': '2022-10-11 14:30:22'
    },
    {
        'biz_id': 170,
        'review_body': 'Excellent !\n' +
        'The best Italian food I ever had... Yum ! I mean it I never had Italian food that good pasta was done perfect sauce marinara is the best ever...',
        "rating": 5,
        'created_at': '2022-09-20 19:55:54'
    },
    {
        'biz_id': 170,
        'review_body': 'clean restaurant, clean table, open atmosphere. Great service (refill water multiple times without asking). Highly recommend!',
        "rating": 5,
        'created_at': '2022-09-22 11:02:40'
    },
    {
        'biz_id': 170,
        'review_body': 'The friggin lobster ravioli. IT IS TO DIEEEEE FOR. Not literally. But oh. my. goodness. You must come here and try. LOOOOOOOK  AT THE PICTURE! LOOK AT ALL...',
        "rating": 5,
        'created_at': '2022-10-12 19:59:24'
    },
    {
        'biz_id': 171,
        'review_body': 'So delicious! Highly recommend getting a reservation as this place is definitely busy! \n' +
        "The service and atmosphere was great and we'll definitely be coming...",
        "rating": 5,
        'created_at': '2022-10-13 11:45:48'
    },
    {
        'biz_id': 171,
        'review_body': 'Lovely restaurant. we love sushi and when we heard about this restaurant we were curious to see how it tastes and our overall experience was great.\n' +
        '\n' +
        'Things...',
        "rating": 5,
        'created_at': '2022-10-09 10:40:39'
    },
    {
        'biz_id': 171,
        'review_body': "Vegan sushi might sound like an oxy moron (or even punishment) for raw fish enthusiasts, but it's a godsend for those of us who aren't. \n" +
        '\n' +
        'Each first bite of...',
        "rating": 5,
        'created_at': '2022-10-01 12:35:11'
    },
    {
        'biz_id': 172,
        'review_body': 'Whole ambiance and food was a vibe. Great and easy service and I like how the food was presented on the plates along with the fact that they taste...',
        "rating": 5,
        'created_at': '2022-09-27 21:31:11'
    },
    {
        'biz_id': 172,
        'review_body': 'Bro, this is a nice spot. The fried chicken is fire  I will definitely drive back to the city for this! I was super disappointed in the loco moco. I wanted...',
        "rating": 4,
        'created_at': '2022-10-11 20:52:05'
    },
    {
        'biz_id': 172,
        'review_body': 'Amazing food! \n' +
        'Very good and fast service. The food came out faster than the drinks! \n' +
        'A little pricey but definitely a must try!',
        "rating": 4,
        'created_at': '2022-10-11 16:29:14'
    },
    {
        'biz_id': 173,
        'review_body': 'We came to Tacorea after cocktails nearby at Wilson & Wilson. I had heard of this place some time ago, and was intrigued, as I like both Korean and Mexican...',
        "rating": 5,
        'created_at': '2022-09-26 16:35:08'
    },
    {
        'biz_id': 173,
        'review_body': 'First time trying this place after walking by it a bunch of times and decided to go with a the super burrito with the spicy pork. It also came with a side...',
        "rating": 4,
        'created_at': '2022-10-01 09:05:52'
    },
    {
        'biz_id': 173,
        'review_body': 'I was extremely excited to try this place because it combines two of my favourite cuisines: Korean & Mexican! I ordered takeout on a Monday evening and...',
        "rating": 4,
        'created_at': '2022-08-26 07:53:32'
    },
    {
        'biz_id': 174,
        'review_body': 'Best meal of my life. Here is what we ordered so you can have the same (or similar). FYI menu is seasonal and might change daily!\n' +
        '\n' +
        '1. 4 oysters, fried...',
        "rating": 5,
        'created_at': '2022-08-27 21:50:03'
    },
    {
        'biz_id': 174,
        'review_body': "Omg I've been wanting to come here for the longest time! So when I was offered a free dinner here from my old colleagues - I couldn't resist!\n" +
        '\n' +
        'The vibes are...',
        "rating": 5,
        'created_at': '2022-10-07 10:30:22'
    },
    {
        'biz_id': 174,
        'review_body': 'Nice place but OK food..Not worth the money.\n' +
        '\n' +
        'Also they confirmed my reservation over the phone and I did ask for a table outside, after reaching there,...',
        "rating": 3,
        'created_at': '2022-10-13 05:25:15'
    },
    {
        'biz_id': 175,
        'review_body': 'Came here for a team lunch and what an experience it was! \n' +
        '\n' +
        'We went to town on the apps and ordered the special flatbread of the day, dip sampler, Saghanaki...',
        "rating": 5,
        'created_at': '2022-10-11 11:48:38'
    },
    {
        'biz_id': 175,
        'review_body': 'Visited Kokkari Estiatorio will a group of colleagues for lunch. We had reservations ahead of time so being seated was very easy. I arrived a few minutes...',
        "rating": 4,
        'created_at': '2022-10-12 11:05:55'
    },
    {
        'biz_id': 175,
        'review_body': 'Amazing food and even better service. Our dinner took about 2.5 hours and we were not upset about it. \n' +
        '\n' +
        'After a weekend of trying new restaurants after...',
        "rating": 5,
        'created_at': '2022-10-11 10:02:46'
    },
    {
        'biz_id': 176,
        'review_body': 'Haha well I ordered 4 tacos thinking they were street tacos. These tacos are much bigger. I ordered 2 carnitas and 2 asada and both were great.\n' +
        '\n' +
        ' I also...',
        "rating": 5,
        'created_at': '2022-09-29 12:14:32'
    },
    {
        'biz_id': 176,
        'review_body': "Deserve the hype? I think not. When we got there, the line wasn't too long. It was my first time going to that place even though I know it is a hit spot....",
        "rating": 3,
        'created_at': '2022-10-09 22:13:18'
    },
    {
        'biz_id': 176,
        'review_body': "Forget what anyone has told you, THIS is the best burrito in the Mission. Probably the best burrito I've ever had.\n" +
        '\n' +
        'La Taqueria has two important...',
        "rating": 5,
        'created_at': '2022-09-22 22:28:01'
    },
    {
        'biz_id': 177,
        'review_body': "I came with friends for lunch around 2pm and it wasn't busy. Parking is super tough around the area and metered. We got to order immediately and I got a...",
        "rating": 5,
        'created_at': '2022-10-01 21:08:01'
    },
    {
        'biz_id': 177,
        'review_body': "Santiago, thanks for your response! It's actually ok due Covid, it's probably best to not put the salsa bar back! The guy behind the counter gave me the...",
        "rating": 4,
        'created_at': '2022-10-11 02:31:05'
    },
    {
        'biz_id': 177,
        'review_body': 'Came over to try this spot out for lunch! Took Bart over from the city on Market. This place is conveniently located right next to the Bart station so it...',
        "rating": 4,
        'created_at': '2022-10-08 18:38:19'
    },
    {
        'biz_id': 178,
        'review_body': 'their pizza is very good, the waiter friend was very nice, the taste is excellent\n' +
        '\n' +
        'Award Winning Margherita',
        "rating": 5,
        'created_at': '2022-09-04 14:10:18'
    },
    {
        'biz_id': 178,
        'review_body': 'After reading all the reviews I was left only slightly disappointed. The food was quite good and healthy portions to boot. The atmosphere and wait staff was...',
        "rating": 4,
        'created_at': '2022-08-26 16:14:03'
    },
    {
        'biz_id': 178,
        'review_body': "Cute spot for any occasion, especially a night out in North Beach. The Diavola pizza was delicious- the crust didn't feel too heavy or greasy and it had a...",
        "rating": 5,
        'created_at': '2022-10-12 10:12:54'
    },
    {
        'biz_id': 179,
        'review_body': "At the time, it wasn't so busy, yet there was still a long line for both the food and the bread. The food line goes further into the store and the bread...",
        "rating": 4,
        'created_at': '2022-09-25 23:53:34'
    },
    {
        'biz_id': 179,
        'review_body': "Jesus must have gone to Boudin's for the loaves and fish to feed the masses cause they'd def line up for this! \n" +
        'Boudins is rich with history and flavors a...',
        "rating": 4,
        'created_at': '2022-09-15 19:47:09'
    },
    {
        'biz_id': 179,
        'review_body': "The decor is rustic and and as you walk in you're hit with the wonderful smell of sourdough. They even have bear, alligator, and crab shaped sourdough....",
        "rating": 4,
        'created_at': '2022-09-13 11:04:47'
    },
    {
        'biz_id': 180,
        'review_body': 'The BEST sandwich spot in the city! :) \n' +
        '\n' +
        'Their dutch crunch is *chefs kiss* It has a pleasant combination of a crunchy exterior and a soft, slightly sweet...',
        "rating": 5,
        'created_at': '2022-09-10 15:46:13'
    },
    {
        'biz_id': 180,
        'review_body': 'The sandwiches are good. Not great- just good. \n' +
        "So if there's a line it won't hurt to shop around. \n" +
        '\n' +
        'In general the one thing I harp on is the tipping when...',
        "rating": 4,
        'created_at': '2022-09-16 13:29:17'
    },
    {
        'biz_id': 180,
        'review_body': "Drove from the east bay and wanted to find something quick for lunch to take to Baker Beach. Decided to give Lou's a try based on their reviews!\n" +
        '\n' +
        '5 stars...',
        "rating": 4,
        'created_at': '2022-09-03 14:29:08'
    },
    {
        'biz_id': 181,
        'review_body': 'I was visiting my daughter & son-law and we  stopped by Limoncello on our way to a park in San Francisco to pick up some Italian sandwiches. We had a little...',
        "rating": 5,
        'created_at': '2022-09-13 15:54:42'
    },
    {
        'biz_id': 181,
        'review_body': "The owner of this business is absolutely insane and has no clue of what customer service is about. He can't even admit when he's wrong. We ordered...",
        "rating": 1,
        'created_at': '2022-09-05 13:55:32'
    },
    {
        'biz_id': 181,
        'review_body': 'Great vibes and delicious food. \n' +
        '\n' +
        "Upon walking into the store, I didn't know that it was like a little corner store. I came for the sandwiches and was...",
        "rating": 5,
        'created_at': '2022-08-14 22:43:41'
    },
    {
        'biz_id': 182,
        'review_body': "I don't know if you want to say this is a hidden gem because honestly, getting to this part of Tenderloin is a trek in itself.  When you finally get there...",
        "rating": 5,
        'created_at': '2022-09-29 08:40:51'
    },
    {
        'biz_id': 182,
        'review_body': 'We were visiting SF for a few days and in my research, I learned that the Tenderloin area should be avoided...in the end my poor bf was sent on a mission to...',
        "rating": 4,
        'created_at': '2022-09-12 20:02:03'
    },
    {
        'biz_id': 182,
        'review_body': "It's the consistency for me! Saigon Sandwich never disappoints. Located in the Tenderloin, this little hole in the wall pumps out hundreds of incredible...",
        "rating": 5,
        'created_at': '2022-09-05 19:32:22'
    },
    {
        'biz_id': 183,
        'review_body': 'Drinking at the bar to start the evening was a great idea during happy hour!!  \n' +
        '\n' +
        'We the. Gained a table right next to the windows overlooking Alcatraz and...',
        "rating": 5,
        'created_at': '2022-08-25 18:13:09'
    },
    {
        'biz_id': 183,
        'review_body': 'Not bad, but not impressive at the same time.\n' +
        'The service was pretty good, although they were busy.',
        "rating": 3,
        'created_at': '2022-09-08 21:58:50'
    },
    {
        'biz_id': 183,
        'review_body': 'Food was decent, and steak was pretty good for a seafood restaurant. What really made our night was our server, Bongjovi. He was very helpful with the menu...',
        "rating": 5,
        'created_at': '2022-09-20 20:08:41'
    },
    {
        'biz_id': 184,
        'review_body': 'I came here for lunch and it was soo worth it!!!\n' +
        '\n' +
        'We came here for the meat but was swayed by the salad bar!! I kept going back for the mango salad. It was...',
        "rating": 5,
        'created_at': '2022-10-10 09:13:20'
    },
    {
        'biz_id': 184,
        'review_body': 'This was my first time ever trying Espetus and it blew my mind! My friends and I saw their online promotion for the SF location for the month of October,...',
        "rating": 5,
        'created_at': '2022-10-04 21:47:07'
    },
    {
        'biz_id': 184,
        'review_body': 'Everything was delicious. Our table favorite was the chicken heart. \n' +
        '\n' +
        'We love the variety of meat options.\n' +
        '\n' +
        'Everything was cooked well with very good...',
        "rating": 5,
        'created_at': '2022-10-04 17:49:45'
    },
    {
        'biz_id': 185,
        'review_body': "Solid restaurant.  The line moves faster than you think so don't get discouraged when you see it.\n" +
        "It's worth it, enough said.",
        "rating": 5,
        'created_at': '2022-09-11 11:14:31'
    },
    {
        'biz_id': 185,
        'review_body': 'Started with oyster Bar mix, one of each type of oysters. Does not disappoint, there was slight differences between each oysters. \n' +
        'Next had the Bagna Cauda....',
        "rating": 5,
        'created_at': '2022-10-09 17:26:59'
    },
    {
        'biz_id': 185,
        'review_body': "Caveat being that I can't eat shellfish so like most of this menu I can't try. But the rest while good was for me quite overpriced\n" +
        '\n' +
        'My wife got the oysters...',
        "rating": 4,
        'created_at': '2022-10-10 14:01:29'
    },
    {
        'biz_id': 186,
        'review_body': "AMAZING!! Jenny is the best ever!! Such good service and absolutely amazing food. This place has the FRESHEST Uni I've ever had and I live in Santa...",
        "rating": 5,
        'created_at': '2022-09-23 22:01:20'
    },
    {
        'biz_id': 186,
        'review_body': 'Seriously the best sushi place! I live around the corner and I have to swing by AT LEAST once a week. JENNY IS AMAZING.',
        "rating": 5,
        'created_at': '2022-09-16 21:22:09'
    },
    {
        'biz_id': 186,
        'review_body': 'Service was awesome. Ambiance is great. Jenny was our waitress and was super knowledgeable about the menu and quick with her service. \n' +
        '\n' +
        'The staff was super...',
        "rating": 5,
        'created_at': '2022-10-07 21:03:13'
    },
    {
        'biz_id': 187,
        'review_body': "Some of the best chicken and waffles I've had, perfectly crispy outside and tender chicken on the inside. The waffle had a well balanced sweetness to it and...",
        "rating": 5,
        'created_at': '2022-10-02 11:30:44'
    },
    {
        'biz_id': 187,
        'review_body': 'Lapisara is a sanctuary from the rest of Lower Nob Hill. See photo with King Liquor right outside hehe. \n' +
        '\n' +
        'Their interior was bright and refreshing yet...',
        "rating": 4,
        'created_at': '2022-10-10 09:12:37'
    },
    {
        'biz_id': 187,
        'review_body': 'We came here for brunch on the day of the Warriors parade and luckily got seated right away.\n' +
        '\n' +
        'They have both indoor and outdoor seating but I will say this...',
        "rating": 4,
        'created_at': '2022-10-04 15:17:08'
    },
    {
        'biz_id': 188,
        'review_body': "I absolutely love this restaurant! It's my favorite place to eat and I have always been seated pretty quickly. The food is delicious, the drinks are...",
        "rating": 5,
        'created_at': '2022-09-20 10:19:16'
    },
    {
        'biz_id': 188,
        'review_body': 'The food is excellent. The service needs improvement. Servers were rushing us through appetizers, drinks, dinner, and dessert. For an upscale restaurant,...',
        "rating": 4,
        'created_at': '2022-09-04 11:52:54'
    },
    {
        'biz_id': 188,
        'review_body': 'Atmosphere: 5/5\n' +
        'Food: 4.5/5\n' +
        'Drinks: 5/5\n' +
        'Service: 5/5\n' +
        '\n' +
        'I had such a great time here catching up with a friend. The whole place is decked out in flowers so...',
        "rating": 5,
        'created_at': '2022-09-30 14:52:54'
    },
    {
        'biz_id': 189,
        'review_body': "14 years ago, some friends of mine convinced me to go to a Vietnamese Restaurant to try some Crab and my life hasn't been the same since.\n" +
        '\n' +
        'When they talk...',
        "rating": 5,
        'created_at': '2022-08-31 10:37:04'
    },
    {
        'biz_id': 189,
        'review_body': 'I came here with a party of 7 on a Saturday night, and we were able to get seated quickly. They brought us upstairs where they host groups with 5+ people....',
        "rating": 4,
        'created_at': '2022-10-09 18:57:21'
    },
    {
        'biz_id': 189,
        'review_body': 'Food 4.0/5.0\n' +
        'Service 3.5/5.0\n' +
        'Value 3.0/5.0\n' +
        'Decor 3.0/5.0\n' +
        'Overall 4.0/5.0\n' +
        '\n' +
        'Nice old school crab spot tucked away on the western edge of Outer Sunset....',
        "rating": 4,
        'created_at': '2022-10-03 19:41:01'
    }
]

instances = []

type_dict = {}

for type in types:
    ty = (Type(type=type['title'], alias=type['alias']))
    instances.append(ty)
    type_dict[type['alias']] = ty

delivery = Transaction(transaction='delivery')
pickup = Transaction(transaction='pickup')
restaurant_reservation = Transaction(transaction='restaurant_reservation')

instances.append(delivery)
instances.append(pickup)
instances.append(restaurant_reservation)

transaction_dict = {
  'delivery': delivery,
  'pickup': pickup,
  'restaurant_reservation': restaurant_reservation
}

# dup_biz = {8,  10,  12,  17,  25,  32,  36,  37,  44, 45,  59,  65,  69,  88,  94,  96,  97,  98, 100, 104, 109, 113,
#            116, 117, 124, 129, 132, 141, 156, 157, 162, 164, 166, 167, 169, 173, 174, 186, 200, 203, 204, 222, 228, 232, 236, 237}
# dup_rev = {9,  11,  13,  18,  26,  33,  37,  38,  45, 46,  60,  66,  70,  89,  95,  97,  98,  99, 101, 105, 110, 114,
#            117, 118, 125, 130, 133, 142, 157, 158, 163, 165, 167, 168, 170, 174, 175, 187, 201, 204, 223, 229, 233, 237, 238}
count = 1
for i in range(0, len(bizzies)):
    name = bizzies[i]['name']
    city = bizzies[i]['location']['city']
    state = bizzies[i]['location']['state']
    country = bizzies[i]['location']['country']
    address = ''
    if len(bizzies[i]['address']) == 2:
        address = bizzies[i]['address'][0]
    else:
        address = ' '.join(bizzies[i]['address'][0:2])
    zipcode = bizzies[i]['location']['zip_code']
    lat = bizzies[i]['lat']
    lng = bizzies[i]['lng']
    price_range = bizzies[i]['price']
    phone_number = bizzies[i]['phone']
    business_id = count
    url = bizzies[i]['url']
    start_time = bizzies[i]['hours']['start']
    end_time = bizzies[i]['hours']['end']
    transactions = [transaction_dict[t] for t in bizzies[i]['transactions']]
    types = [type_dict[t] for t in bizzies[i]['categories']]

    instances.append(Business(
                                  name=name,
                                  owner_id=1,
                                  city=city,
                                  state=state,
                                  country=country,
                                  address=address,
                                  zipcode=zipcode,
                                  lat=lat,
                                  lng=lng,
                                  price_range=price_range,
                                  phone_number=phone_number,
                                  preview_img=url,
                                  start_time=start_time,
                                  end_time=end_time,
                                  transactions=transactions,
                                  types=types))

        # for cat in bizzies[i]['categories']:
        #   if cat in types_alias:
        #     type_id = types_alias.index(cat)+1
        #     new_businessType = BusinessType(type_id=type_id, business_id=business_id)
        #     instances.append(new_businessType)

        # for tra in bizzies[i]['transactions']:
        #     instances.append(BusinessTransaction(transaction_id=transaction_types.index(tra)+1, business_id=business_id))

    for img in bizzies[i]['photos']:
        instances.append(
            Image(business_id=business_id, review_id=None, url=img))
    count += 1


biz_id = 1
biz_count = 1
users = {1}
for i in range(0, len(reviews)):
    user_id = choice([2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12,
                     13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])
    while user_id in users:
        user_id = choice([2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12,
                         13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])
    users.add(user_id)
    instances.append(Review(business_id=biz_id, user_id=user_id,
                     review_body=reviews[i]['review_body'], rating=reviews[i]['rating'], created_at=reviews[i]['created_at']))
    if (i+1) % 3 == 0:
        biz_count += 1
        users = {1}
    # if not biz_count in dup_rev and (i+1) % 3 == 0 and biz_id + 1 != 195:
    #     biz_id += 1

# hopefully this doesnt break


def seed_all_data_sans_users():
    for instance in instances:
        db.session.add(instance)
    db.session.commit()



def undo_all_data_sans_users():
    db.session.execute('TRUNCATE businesses RESTART IDENTITY CASCADE;')
    db.session.execute('TRUNCATE reviews RESTART IDENTITY CASCADE;')
    db.session.execute('TRUNCATE types RESTART IDENTITY CASCADE;')
    db.session.execute('TRUNCATE transactions RESTART IDENTITY CASCADE;')
    db.session.execute('TRUNCATE images RESTART IDENTITY CASCADE;')
    db.session.commit()
