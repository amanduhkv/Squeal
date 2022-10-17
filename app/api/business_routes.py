from flask import Blueprint, jsonify, session, request
from app.models import Business, Review, Image, User, db
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required
from ..forms.add_review_form import AddReviewForm
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


@business_routes.route('/')
def get_all_businesses():
    """
    Gets all business
    """
    businesses = Business.query.all()
    biz = [business.to_dict() for business in businesses]
    for b in biz:
        query = db.session.query(func.round(func.avg(Review.rating) * 2)/2).filter_by(business_id=b['id']).first()
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
        biz_review['Review_Images'] = Image.query.filter(biz_review['id'] == Image.review_id).all()

    return jsonify({ "Reviews": biz_reviews })


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

    reviews_query = Review.query.filter(Business.id == biz_id).all()
    biz_reviews = [biz.to_dict() for biz in reviews_query]
    for biz_review in biz_reviews:
        if biz_review['user_id'] == user['id']:
            return jsonify({
                "message": "User already has a review for this business",
                "status_code": 403
        }), 403

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


@business_routes.route("/<int:biz_id>/")
def get_one_business(biz_id):
    """
    Gets one business' details
    """
    business = Business.query.get(biz_id)
    avg_rating = Review.query(func.avg(Review.rating)).filter_by(business_id=biz_id).first()
    business_images = Image.query.filter_by(business_id=biz_id).first()
    owner = User.query.filter_by(owner_id=business['owner']).first()

    business['avg_rating'] = avg_rating
    business['Business_Images'] = business_images.to_dict()
    business['Owner'] = owner.to_dict()

    return jsonify({
        "Businesses": business
    })
