from flask import Blueprint, jsonify, redirect, request
from ..models import db, User, Business, Review, Image
from flask_login import current_user, login_user, logout_user, login_required
from ..forms.edit_review_form import EditReviewForm
from ..forms.delete_review_form import DeleteReviewForm
from ..forms.add_review_img_form import AddReviewImgForm


reviews_routes = Blueprint("reviews", __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = {}
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages[field] = error
    return errorMessages


# 1. LOAD ALL USER REVIEWS
@reviews_routes.route("/current")
@login_required
def user_reviews():
    user = current_user.to_dict()
    reviews_query = Review.query.filter(Review.user_id == user['id']).all()
    user_reviews = [review.to_dict() for review in reviews_query]

    for user_review in user_reviews:
        review_biz = Business.query.filter(user_review['business_id'] == Business.id).first()
        print("REVIEW", user_review)
        user_review['Business'] = review_biz.to_dict()
        user_review['Review_Images'] = Image.query.filter(user_review['id'] == Image.review_id).all()

    return jsonify({ "Reviews": user_reviews })


# 2. ADD A REVIEW --- THIS IS IN THE BIZ ROUTES


# 3. UPDATE A REVIEW
@reviews_routes.route("/<int:review_id>", methods=['PUT'])
@login_required
def update_review(review_id):
    """
    Updates a review
    """
    form = EditReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    review_to_update = Review.query.get(review_id)
    if not review_to_update:
        return jsonify({
            "message": "Review couldn't be found",
            "status_code": 404
        }), 404

    if form.validate_on_submit():
        user = current_user.to_dict()

        if review_to_update.user_id == user['id']:
            review_to_update.review_body = form.data['review_body']
            review_to_update.rating = form.data['rating']

            db.session.commit()

            return review_to_update.to_dict()

        else:
            return { "message": "Forbidden", "status_code": 403 }, 403

    return {'errors': validation_errors_to_error_messages(form.errors)}, 400

# 4. DELETE A REVIEW
@reviews_routes.route("/<int:review_id>", methods=['DELETE'])
@login_required
def delete_review(review_id):
    """
    Deletes a review
    """
    form = DeleteReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    review_to_delete = Review.query.get(review_id)
    if not review_to_delete:
        return jsonify({
            "message": "Review couldn't be found",
            "status_code": 404
        }), 404

    if form.validate_on_submit():
        user = current_user.to_dict()

        if review_to_delete.to_dict()['user_id'] == user['id']:
            db.session.delete(review_to_delete)

            db.session.commit()

            return { "message": "Successfully deleted", "status_code": 200 }

        else:
            return { "message": "Forbidden", "status_code": 403 }, 403

    # return { "message": "Review couldn't be found", "status_code": 404 }, 404


# 5. ADD A REVIEW IMG
@reviews_routes.route("/<int:review_id>/images", methods=['POST'])
@login_required
def add_review_img(review_id):
    """
    Add an image to a review based on the review's id
    """
    form = AddReviewImgForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    review = Review.query.get(review_id)
    if not review:
        return jsonify({
            "message": "Review couldn't be found",
            "status_code": 404
        }), 404

    if form.validate_on_submit():
        user = current_user.to_dict()

        if review.to_dict()['user_id'] == user['id']:
            biz_id = review.to_dict()['business_id']

            review_img = Image(
                review_id = review_id,
                business_id = biz_id,
                url = form.data['url']
            )

            db.session.add(review_img)
            db.session.commit()

            return review_img.to_dict()

        else:
            return { "message": "Forbidden", "status_code": 403 }, 403

    # return { "message": "Review couldn't be found", "status_code": 404 }, 404


# 6. DELETE A REVIEW IMG --- THIS IS IN THE IMAGES ROUTES
