from flask import Blueprint, redirect
from ..models import db, User, Business, Review
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
# added to biz route

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
