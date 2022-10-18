from flask import Blueprint, jsonify, session, request
from app.models import Business, Review, Image, User, Type, Transaction, db
from app.forms.delete_biz_form import DeleteBusinessForm
from flask_login import current_user, login_user, logout_user, login_required
from ..forms.add_review_form import AddReviewForm
from ..forms.add_business_form import AddBusinessForm
from ..forms.add_business_img_form import AddBizImgForm
from ..forms.edit_business_form import EditBusinessForm
from sqlalchemy import func

business_routes = Blueprint('business', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = {}
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages[field] = error
    return errorMessages


# LOAD ALL BIZ
@business_routes.route('/')
def get_all_businesses():
    """
    Gets all business
    """
    businesses = Business.query.all()
    biz = [[business.to_dict(), business] for business in businesses]
    for b in biz:
        print(">>>>>> B", b)
        query = db.session.query(func.round(
            func.avg(Review.rating) * 2)/2).filter_by(business_id=b[0]['id']).first()
        avg_rating = list(query)[0]
        b[0]['avg_rating'] = avg_rating
        types_list = [type.to_dict() for type in b[1].types]
        transactions_list = [transaction.to_dict()
                         for transaction in b[1].transactions]

        b[0]['types'] = types_list
        b[0]['transactions'] = transactions_list

    biz = [business[0] for business in biz]
    return jsonify({
        "Businesses": biz
    })


# LOAD SINGLE BIZ
@business_routes.route("/<int:biz_id>")
def get_one_business(biz_id):
    """
    Gets one business' details
    """
    biz = Business.query.get(biz_id)
    if not biz:
        return jsonify(
            {"message": "Business couldn't be found.",
            "status_code": 404}), 404

    business = biz.to_dict()
    query = db.session.query(func.round(
        func.avg(Review.rating) * 2)/2).filter_by(business_id=biz_id).first()
    avg_rating = list(query)[0]
    business_images = Image.query.filter_by(business_id=biz_id)
    images = [{"id": img.to_dict()['id'], "url": img.to_dict()['url'], "review_id": img.to_dict()['review_id']}
              for img in business_images]
    owner = User.query.filter_by(id=business['owner_id']).first().to_dict()
    types_list = [type.to_dict() for type in biz.types]
    transactions_list = [transaction.to_dict() for transaction in biz.transactions]

    business['types'] = types_list
    business['transactions'] = transactions_list
    business['avg_rating'] = avg_rating
    business['Business_Images'] = images
    business['Owner'] = owner

    return business


# LOAD CURRENT USER'S BIZ
@business_routes.route("/current")
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
@business_routes.route("", methods=['POST'])
@login_required
def add_new_business():
    """
    Creates a new business
    """
    user = current_user.to_dict()
    user_id = user['id']
    form = AddBusinessForm()
    form['csrf_token'].data = request.cookies['csrf_token']


    # Body validation error handlers:
    login_val_error = {
        "message": "Validation error",
        "status_code": 400,
        "errors": {}
    }

    if not form.data['name']:
        login_val_error["errors"]["name"] = "Name of business is is required."
    if not form.data['address']:
        login_val_error["errors"]["address"] = "Address is required."
    if not form.data['city']:
        login_val_error["errors"]["city"] = "City is required."
    if not form.data['state']:
        login_val_error["errors"]["state"] = "State is required."
    if not form.data['country']:
        login_val_error["errors"]["country"] = "Country is required."
    if not form.data['zipcode']:
        login_val_error["errors"]["zipcode"] = "Zip code is required."
    if form.data['lat'] != 0 and not form.data['lat']:
        login_val_error["errors"]["lat"] = "Latitude is required."
    if form.data['lng'] and not form.data['lng']:
        login_val_error["errors"]["lng"] = "Longitude is required."
    if form.data['lat'] < -90 or form.data['lat'] > 90 :
        login_val_error["errors"]["lat"] = "Latitude must be between -90 and 90."
    if form.data['lng'] < -180 or form.data['lng'] > 180 :
        login_val_error["errors"]["lng"] = "Longitude must be between -180 and 180."
    if not form.data['price_range']:
        login_val_error["errors"]["price_range"] = "Price range is required."
    if not form.data['phone_number']:
        login_val_error["errors"]["phone_number"] = "Business phone number is required."
    if not form.data['start_time']:
        login_val_error["errors"]["start_time"] = "Business start time is required."
    if not form.data['end_time']:
        login_val_error["errors"]["end_time"] = "Business end time is required."
    if len(login_val_error["errors"]) > 0:
        return jsonify(login_val_error), 400


    if form.validate_on_submit():
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
        db.session.add(business)
        db.session.commit()

        types_list = [type.to_dict() for type in business.types]
        transactions_list = [transaction.to_dict() for transaction in business.transactions]

        biz = business.to_dict()
        biz['types'] = types_list
        biz['transactions'] = transactions_list

        return biz

    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


# UPDATE A BIZ
@business_routes.route("/<int:biz_id>", methods=['PUT'])
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
    if not business_to_update:
        return jsonify({
            "message": "Business couldn't be found",
            "status_code": 404
        })


    # Body validation error handlers:
    login_val_error = {
        "message": "Validation error",
        "status_code": 400,
        "errors": {}
    }

    if not form.data['name']:
        login_val_error["errors"]["name"] = "Name of business is is required."
    if not form.data['address']:
        login_val_error["errors"]["address"] = "Address is required."
    if not form.data['city']:
        login_val_error["errors"]["city"] = "City is required."
    if not form.data['state']:
        login_val_error["errors"]["state"] = "State is required."
    if not form.data['country']:
        login_val_error["errors"]["country"] = "Country is required."
    if not form.data['zipcode']:
        login_val_error["errors"]["zipcode"] = "Zip code is required."
    if form.data['lat'] != 0 and not form.data['lat']:
        login_val_error["errors"]["lat"] = "Latitude is required."
    if form.data['lng'] and not form.data['lng']:
        login_val_error["errors"]["lng"] = "Longitude is required."
    if form.data['lat'] < -90 or form.data['lat'] > 90 :
        login_val_error["errors"]["lat"] = "Latitude must be between -90 and 90."
    if form.data['lng'] < -180 or form.data['lng'] > 180 :
        login_val_error["errors"]["lng"] = "Longitude must be between -180 and 180."
    if not form.data['price_range']:
        login_val_error["errors"]["price_range"] = "Price range is required."
    if not form.data['phone_number']:
        login_val_error["errors"]["phone_number"] = "Business phone number is required."
    if not form.data['start_time']:
        login_val_error["errors"]["start_time"] = "Business start time is required."
    if not form.data['end_time']:
        login_val_error["errors"]["end_time"] = "Business end time is required."
    if len(login_val_error["errors"]) > 0:
        return jsonify(login_val_error), 400


    if user_id != business_to_update.to_dict()['owner_id']:
        return {"message": "Forbidden", "status_code": 403}, 403
    if user_id == business_to_update.to_dict()['owner_id']:
        if form.validate_on_submit():
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

            types_list = [type.to_dict() for type in business_to_update.types]
            transactions_list = [transaction.to_dict() for transaction in business_to_update.transactions]

            biz = business_to_update.to_dict()
            biz['types'] = types_list
            biz['transactions'] = transactions_list

            return biz
        else:
            return {'errors': validation_errors_to_error_messages(form.errors)}, 400

    else:
        return {"message": "Forbidden", "status_code": 403}, 403

# DELETE BIZ
@business_routes.route("/<int:biz_id>", methods=['DELETE'])
@login_required
def delete_biz(biz_id):
    """
    Deletes a business
    """
    form = DeleteBusinessForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    biz_to_delete = Business.query.get(biz_id)
    if not biz_to_delete:
        return jsonify({
            "message": "Business couldn't be found",
            "status_code": 404
        }), 404

    if form.validate_on_submit():
        user = current_user.to_dict()

        if biz_to_delete.to_dict()['owner_id'] == user['id']:
            db.session.delete(biz_to_delete)

            db.session.commit()

            return {"message": "Successfully deleted", "status_code": 200}

        else:
            return {"message": "Forbidden", "status_code": 403}, 403

# ADD A BUSINESS IMG
@business_routes.route("/<int:biz_id>/images", methods=['POST'])
@login_required
def add_biz_img(biz_id):
    """
    Add an image to a biz based on the biz's id
    """
    form = AddBizImgForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    biz = Business.query.get(biz_id)
    if not biz:
        return jsonify({
            "message": "Business couldn't be found",
            "status_code": 404
        }), 404

    if form.validate_on_submit():
        user = current_user.to_dict()

        if biz.to_dict()['owner_id'] == user['id']:

            biz_img = Image(
                business_id = biz_id,
                url = form.data['url'],
                review_id = None
            )

            db.session.add(biz_img)
            db.session.commit()

            return biz_img.to_dict()

        else:
            return { "message": "Forbidden", "status_code": 403 }, 403


# -------------------- REVIEWS STUFF -------------------- #

# LOAD ALL BIZ REVIEWS BY BIZ ID
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


    user = current_user.to_dict()

    reviews_query = Review.query.filter(Review.business_id == biz_id).all()
    biz_reviews = [biz.to_dict() for biz in reviews_query]
    for biz_review in biz_reviews:
        if biz_review['user_id'] == user['id']:
            return jsonify({
                "message": "User already has a review for this business",
                "status_code": 403
            }), 403


    # Body validation error handlers:
    login_val_error = {
        "message": "Validation error",
        "status_code": 400,
        "errors": {}
    }

    if not form.data['review_body']:
        login_val_error["errors"]["review_body"] = "Review text is required"
    if form.data['rating'] < 1 or form.data['rating'] > 5:
        login_val_error["errors"]["rating"] = "Rating must be an integer from 1 to 5"
    if len(login_val_error["errors"]) > 0:
        return jsonify(login_val_error), 400


    if form.validate_on_submit():

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
