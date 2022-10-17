from flask import Blueprint, jsonify, session, request
from app.models import Business, Review, Image, User, db
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required
from ..forms.add_review_form import AddReviewForm
from sqlalchemy import func, inspect

business_routes = Blueprint('business', __name__)


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}

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

@business_routes.route("/<int:biz_id>/reviews", methods=['POST'])
def add_review(biz_id):
    """
    Creates a new review
    """
    form = AddReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        review = Review(
            business_id=biz_id,
            user_id=current_user[id],
            review_body=form.data['review_body'],
            rating=form.data['rating']
        )
        db.session.add(review)
        db.session.commit()
        return review.to_dict()
    # return {'errors': validation_errors_to_error_messages(form.errors)}, 401
    return "Bad data"

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
