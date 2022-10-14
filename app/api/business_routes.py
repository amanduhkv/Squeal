from flask import Blueprint, jsonify, session, request
from app.models import Business, Review, db
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required
from ..forms.add_review_form import AddReviewForm

business_routes = Blueprint('business', __name__)

@business_routes.route('/')
def get_all_businesses():
    businesses = Business.query.all()
    biz = [business.to_dict() for business in businesses ]
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
            business_id=form.data['business_id'],
            user_id=form.data['user_id'],
            review_body=form.data['review_body'],
            rating=form.data['rating']
        )
        db.session.add(review)
        db.session.commit()
        return review.to_dict()
    # return {'errors': validation_errors_to_error_messages(form.errors)}, 401
    return "Bad data"