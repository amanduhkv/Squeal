from flask import Blueprint, jsonify, session, request
from app.models import Business, Review, Image, User, Type, Transaction, db
from app.forms.delete_biz_form import DeleteBusinessForm
from flask_login import current_user, login_user, logout_user, login_required
from ..forms.add_review_form import AddReviewForm
from ..forms.add_business_form import AddBusinessForm
# from ..forms.add_business_img_form import AddBizImgForm
from ..forms.edit_business_form import EditBusinessForm
from sqlalchemy import func

business_routes = Blueprint('business', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages


# LOAD ALL BIZ
@business_routes.route('/')
def get_all_businesses():
    """
    Gets all business
    """
    businesses = Business.query.all()
    biz = [business.to_dict() for business in businesses]
    for b in biz:
        query = db.session.query(func.round(
            func.avg(Review.rating) * 2)/2).filter_by(business_id=b['id']).first()
        avg_rating = list(query)[0]
        b['avg_rating'] = avg_rating
    return jsonify({
        "Businesses": biz
    })


# LOAD ALL BIZ REVIEWS
@business_routes.route("/<int:biz_id>/reviews")
def biz_reviews(biz_id):
    """
    Gets all business reviews
    """

    biz = Business.query.get(biz_id)
    if not biz:
        return jsonify({
            "message": "Business couldn't be found",
            "status_code": 404
        }), 404

    reviews_query = Review.query.filter(Business.id == biz_id).all()
    biz_reviews = [biz.to_dict() for biz in reviews_query]
    curr_biz = Business.query.filter(Business.id == biz_id).first()

    for biz_review in biz_reviews:
        biz_review['Business'] = curr_biz.to_dict()
        biz_review['Review_Images'] = Image.query.filter(
            biz_review['id'] == Image.review_id).all()

    return jsonify({"Reviews": biz_reviews})


# ADD A REVIEW
# TODO: ADD ERROR VALIDATION FOR USER ALREADY HAS A REVIEW FOR THIS BIZ
@business_routes.route("/<int:biz_id>/reviews", methods=['POST'])
@login_required
def add_review(biz_id):
    """
    Creates a new review
    """
    form = AddReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    biz = Business.query.get(biz_id)
    if not biz:
        return jsonify({
            "message": "Business couldn't be found",
            "status_code": 404
        }), 404

    if form.validate_on_submit():
        user = current_user.to_dict()

        review = Review(
            business_id=biz_id,
            user_id=user['id'],
            review_body=form.data['review_body'],
            rating=form.data['rating']
        )
        db.session.add(review)
        db.session.commit()
        return review.to_dict()

    return {'errors': validation_errors_to_error_messages(form.errors)}, 400


# LOAD SINGLE BIZ
@business_routes.route("/<int:biz_id>/")
def get_one_business(biz_id):
    """
    Gets one business' details
    """
    business = Business.query.get(biz_id).to_dict()
    query = db.session.query(func.round(
        func.avg(Review.rating) * 2)/2).filter_by(business_id=biz_id).first()
    avg_rating = list(query)[0]
    business_images = Image.query.filter_by(business_id=biz_id)
    images = [{"id": img.to_dict()['id'], "url": img.to_dict()['url'], "review_id": img.to_dict()['review_id']}
              for img in business_images]
    owner = User.query.filter_by(id=business['owner_id']).first().to_dict()

    business['avg_rating'] = avg_rating
    business['Business_Images'] = images
    business['Owner'] = owner

    return jsonify({
        "Businesses": business
    })


# LOAD CURRENT USER'S BIZ
@business_routes.route("/current/")
@login_required
def get_current_user_business():
    """
    Gets current user's business' details
    """
    user = current_user.to_dict()
    user_id = user['id']
    if not user:
        return 'User must be logged in'
    businesses = Business.query.filter_by(owner_id=user_id)
    all_businesses = [b.to_dict() for b in businesses]
    current_businesses = []
    if len(all_businesses) > 0:
        for business in all_businesses:
            query = db.session.query(func.round(
                func.avg(Review.rating) * 2)/2).filter_by(business_id=business['id']).first()
            avg_rating = list(query)[0]
            business_images = Image.query.filter_by(business_id=business['id'])
            images = [{"id": img.to_dict()['id'], "url": img.to_dict()['url'], "review_id": img.to_dict()['review_id']}
                      for img in business_images]

            business['avg_rating'] = avg_rating
            business['Business_Images'] = images
            current_businesses.append(business)

        return jsonify({
            "Businesses": current_businesses
        })
    return 'Current user does not have any listed businesses'


all_types_list = [
    {'alias': 'bakeries', 'title': 'Bakeries'},
    {'alias': 'bubbletea', 'title': 'Bubble Tea'},
    {'alias': 'cocktailbars', 'title': 'Cocktails'},
    {'alias': 'bars', 'title': 'Bars'},
    {'alias': 'brazilian', 'title': 'Brazilian'},
    {'alias': 'coffee', 'title': 'Coffee & Tea'},
    {'alias': 'chickenshop', 'title': 'Chicken Shop'},
    {'alias': 'desserts', 'title': 'Desserts'},
    {'alias': 'donuts', 'title': 'Donuts'},
    {'alias': 'dimsum', 'title': 'Dim Sum'},
    {'alias': 'ethiopian', 'title': 'Ethiopian'},
    {'alias': 'icecream', 'title': 'Ice Cream & Frozen Yogurt'},
    {'alias': 'juicebars', 'title': 'Juice Bars & Smoothies'},
    {'alias': 'bbq', 'title': 'Barbeque'},
    {'alias': 'breakfast_brunch', 'title': 'Breakfast & Brunch'},
    {'alias': 'burgers', 'title': 'Burgers'},
    {'alias': 'cafes', 'title': 'Cafes'},
    {'alias': 'chicken_wings', 'title': 'Chicken Wings'},
    {'alias': 'chinese', 'title': 'Chinese'},
    {'alias': 'gluten_free', 'title': 'Gluten-Free'},
    {'alias': 'german', 'title': 'German'},
    {'alias': 'gastropubs', 'title': 'Gastropubs'},
    {'alias': 'french', 'title': 'French'},
    {'alias': 'hotdogs', 'title': 'Fast Food'},
    {'alias': 'indpak', 'title': 'Indian'},
    {'alias': 'latin', 'title': 'Latin'},
    {'alias': 'italian', 'title': 'Italian'},
    {'alias': 'japanese', 'title': 'Japanese'},
    {'alias': 'korean', 'title': 'Korean'},
    {'alias': 'newamerican', 'title': 'American (New)'},
    {'alias': 'mediterranean', 'title': 'Mediterranean'},
    {'alias': 'mexican', 'title': 'Mexican'},
    {'alias': 'pizza', 'title': 'Pizza'},
    {'alias': 'ramen', 'title': 'Ramen'},
    {'alias': 'noodles', 'title': 'Noodles'},
    {'alias': 'raw_food', 'title': 'Raw Food'},
    {'alias': 'salad', 'title': 'Salad'},
    {'alias': 'sandwiches', 'title': 'Sandwiches'},
    {'alias': 'soulfood', 'title': 'Soul Food'},
    {'alias': 'soup', 'title': 'Soup'},
    {'alias': 'seafood', 'title': 'Seafood'},
    {'alias': 'steak', 'title': 'Steakhouses'},
    {'alias': 'sushi', 'title': 'Sushi Bars'},
    {'alias': 'tacos', 'title': 'Tacos'},
    {'alias': 'tradamerican', 'title': 'American (Traditional)'},
    {'alias': 'taiwanese', 'title': 'Taiwanese'},
    {'alias': 'thai', 'title': 'Thai'},
    {'alias': 'tapasmallplates', 'title': 'Tapas/Small Plates'},
    {'alias': 'vegetarian', 'title': 'Vegetarian'},
    {'alias': 'vegan', 'title': 'Vegan'},
    {'alias': 'vietnamese', 'title': 'Vietnamese'},
    {'alias': 'waffles', 'title': 'Waffles'},
]
all_transactions_list = ['pickup', 'delivery', 'restaurant_reservation']


# CREATE A BIZ
@business_routes.route("/", methods=['POST'])
@login_required
def add_new_business():
    """
    Creates a new business
    """
    user = current_user.to_dict()
    user_id = user['id']
    form = AddBusinessForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        # print(">>>>>>>>>>>> IVE BEEN VALIDATED")

        type_list = []
        for alias in form.data['types']:
            filtered = [i for i in all_types_list if i['alias'] == alias][0]
            ty = (Type(type=filtered['title'], alias=alias))
            type_list.append(ty)

        transaction_list = []
        for transaction in form.data['transactions']:
            tr = (Transaction(transaction=transaction))
            transaction_list.append(tr)

        business = Business(
            owner_id=user_id,
            name=form.data['name'],
            city=form.data['city'],
            state=form.data['state'],
            country=form.data['country'],
            address=form.data['address'],
            zipcode=form.data['zipcode'],
            price_range=form.data['price_range'],
            start_time=form.data['start_time'],
            end_time=form.data['end_time'],
            preview_img=form.data['preview_img'],
            phone_number=form.data['phone_number'],
            types=type_list,
            transactions=transaction_list,
            lat='33.0',
            lng='64.0',
            # ^placeholders
        )
        # print(">>>>>>>> BUSINESS",business.to_dict())
        db.session.add(business)
        db.session.commit()
        return business.to_dict()

    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


# UPDATE A BIZ
@business_routes.route("/<int:biz_id>/", methods=['PUT'])
@login_required
def edit_business(biz_id):
    """
    Edits an existing business
    """
    user = current_user.to_dict()
    user_id = user['id']

    form = EditBusinessForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    business_to_update = Business.query.get(biz_id)

    print(">>>>>>>>>>>> BUSINESS TO UPDATE", business_to_update)
    print(">>>>>>>>>>>> BUSINESS TO UPDATE TODICT", business_to_update.to_dict())

    if not business_to_update:
        return jsonify({
            "message": "Business couldn't be found",
            "status_code": 404
        })

    if user_id != business_to_update.to_dict()['owner_id']:
        return {"message": "Forbidden", "status_code": 403}, 403
    if user_id == business_to_update.to_dict()['owner_id']:
        if form.validate_on_submit():
            print(">>>>>>>>>>>> IVE BEEN VALIDATED")
            type_list = []
            for alias in form.data['types']:
                filtered = [
                    i for i in all_types_list if i['alias'] == alias][0]
                ty = (Type(type=filtered['title'], alias=alias))
                type_list.append(ty)

            transaction_list = []
            for transaction in form.data['transactions']:
                tr = (Transaction(transaction=transaction))
                transaction_list.append(tr)

            business_to_update.owner_id = user_id
            business_to_update.name = form.data['name']
            business_to_update.city = form.data['city']
            business_to_update.state = form.data['state']
            business_to_update.country = form.data['country']
            business_to_update.address = form.data['address']
            business_to_update.zipcode = form.data['zipcode']
            business_to_update.price_range = form.data['price_range']
            business_to_update.start_time = form.data['start_time']
            business_to_update.end_time = form.data['end_time']
            business_to_update.preview_img = form.data['preview_img']
            business_to_update.phone_number = form.data['phone_number']
            business_to_update.types = type_list
            business_to_update.transactions = transaction_list
            business_to_update.lat = '33.0'
            business_to_update.lng = '64.0'
            # ^placeholders

            db.session.commit()

            return business_to_update.to_dict()
        else:
            return {'errors': validation_errors_to_error_messages(form.errors)}, 400

    else:
        return {"message": "Forbidden", "status_code": 403}, 403
