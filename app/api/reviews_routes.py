from flask import Blueprint, redirect
from ..models import db, User, Business, Review, Review_Image
from flask_login import current_user, login_user, logout_user, login_required
from ..forms import add_review_form

reviews_routes = Blueprint("reviews", __name__)

# routes to /test
@reviews_routes.route("/")
def test():
    return "<h1>Test Reviews Route</h1>"


# TODO:
# 1. LOAD ALL USER REVIEWS
@reviews_routes.route("/current")
def user_reviews():
    user = current_user.to_dict()
    _user_reviews = Review.query.filter(Review.user_id == user['id']).all()
    return dict(_user_reviews)


# # 2. ADD A REVIEW --- THIS NEEDS TO GO IN THE BIZ ROUTE
# @bp.route("/<int:review_id>", methods=['POST'])
# def add_review():
#     """
#     Creates a new review
#     """
#     form = AddReviewForm()
#     form['csrf_token'].data = request.cookies['csrf_token']
#     if form.validate_on_submit():
#         review = Review(
#             business_id=form.dta['business_id'],
#             user_id=form.data['user_id'],
#             review_body=form.data['review_body'],
#             rating=form.data['rating']
#         )
#         db.session.add(review)
#         db.session.commit()
#         return review.to_dict()
#     # return {'errors': validation_errors_to_error_messages(form.errors)}, 401
#     return "Bad data"


# 3. UPDATE A REVIEW
@reviews_routes.route("/<int:review_id>", methods=['PUT'])
def update_review():
    pass



# 4. DELETE A REVIEW
@reviews_routes.route("/<int:review_id>", methods=['DELETE'])
def delete_review():
    pass



# 5. ADD A REVIEW IMG
@reviews_routes.route("/images/<int:review_id>", methods=['POST'])
def add_review_img():
    pass



# 6. DELETE A REVIEW IMG
@reviews_routes.route("/images/<int:review_id>", methods=['DELETE'])
def delete_review_img():
    pass
