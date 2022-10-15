from flask import Blueprint, redirect, request
from ..models import db, User, Business, Review, Image
from flask_login import current_user, login_user, logout_user, login_required
from ..forms.edit_review_form import EditReviewForm
from ..forms.delete_review_form import DeleteReviewForm
from ..forms.add_review_img_form import AddReviewImgForm
from ..forms.delete_review_img_form import DeleteReviewImgForm

reviews_routes = Blueprint("reviews", __name__)


# TODO:
# 1. LOAD ALL USER REVIEWS
@reviews_routes.route("/current")
def user_reviews():
    user = current_user.to_dict()
    _user_reviews = Review.query.filter(Review.user_id == user['id']).all()
    return dict(_user_reviews)


# 2. ADD A REVIEW --- THIS IS IN THE BIZ ROUTE


# 3. UPDATE A REVIEW
@reviews_routes.route("/<int:review_id>", methods=['PUT'])
def update_review(review_id):
    """
    Updates a review
    """
    form = EditReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        review_to_update = Review.query.get(review_id)
        review_to_update.review_body = form.data['review_body']
        review_to_update.rating = form.data['rating']

        db.session.commit()

        return review_to_update.to_dict()
    # return {'errors': validation_errors_to_error_messages(form.errors)}, 401
    return { "message": "Review couldn't be found", "status_code": 404 }



# 4. DELETE A REVIEW
@reviews_routes.route("/<int:review_id>", methods=['DELETE'])
def delete_review(review_id):
    """
    Deletes a review
    """
    form = DeleteReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        review_to_delete = Review.query.get(review_id)
        review_to_delete.session.delete()

        db.session.commit()

        return { "message": "Successfully delete", "status_code": 200 }
    # return {'errors': validation_errors_to_error_messages(form.errors)}, 401
    return { "message": "Review couldn't be found", "status_code": 404 }



# 5. ADD A REVIEW IMG
@reviews_routes.route("/images/<int:review_id>", methods=['POST'])
def add_review_img(review_id):
    """
    Add an image to a review based on the review's id
    """
    form = AddReviewImgForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():

        review = Review.query.get(review_id)
        biz_id = review['business_id']

        review_img = Image(
            review_id = review_id,
            business_id = biz_id,
            url = form.data['url']
        )

        db.session.add(review_img)
        db.session.commit()

        return review_img.to_dict
    # return {'errors': validation_errors_to_error_messages(form.errors)}, 401
    return { "message": "Review couldn't be found", "status_code": 404 }



# 6. DELETE A REVIEW IMG
@reviews_routes.route("/images/<int:image_id>", methods=['DELETE'])
def delete_review_img(image_id):
    """
    Deletes a review image
    """
    form = DeleteReviewImgForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        review_img_to_delete = Image.query.get(image_id)
        review_img_to_delete.session.delete()

        db.session.commit()

        return { "message": "Successfully delete", "status_code": 200 }
    # return {'errors': validation_errors_to_error_messages(form.errors)}, 401
    return { "message": "Review couldn't be found", "status_code": 404 }
