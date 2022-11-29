from flask import Blueprint, jsonify, redirect, request
from ..models import db, User, Business, Review, Image
from flask_login import current_user, login_user, logout_user, login_required
from ..forms.edit_review_form import EditReviewForm
from ..forms.delete_review_form import DeleteReviewForm
from ..forms.add_review_img_form import AddReviewImgForm
from ..forms.delete_review_img_form import DeleteReviewImgForm
from app.awss3 import (
    upload_file_to_s3, allowed_file, get_unique_filename, delete_file_from_s3)


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

# 0. LOAD ALL REVIEWS
@reviews_routes.route('/')
def all_reviews():
    reviews_query = Review.query.all()
    all_revs = [review.to_dict() for review in reviews_query]

    for rev in all_revs:
        review_biz = Business.query.filter(Business.id == rev['business_id']).first()
        rev['Business'] = review_biz.to_dict() if review_biz else None
        user_info = User.query.filter_by(id=rev['user_id']).first()
        rev['User'] = user_info.to_dict()
        img = Image.query.filter(Image.business_id == rev['business_id']).first()
        rev['Image'] = img.to_dict() if img else None

    return jsonify({ 'Reviews': all_revs })


# 1. LOAD ALL USER REVIEWS
@reviews_routes.route("/current")
@login_required
def user_reviews():
    user = current_user.to_dict()
    reviews_query = Review.query.filter(Review.user_id == user['id']).all()
    user_reviews = [review.to_dict() for review in reviews_query]

    for user_review in user_reviews:
        review_biz = Business.query.filter(user_review['business_id'] == Business.id).first()
        user_review['Business'] = review_biz.to_dict() if review_biz else None
        img = Image.query.filter(Image.business_id == user_review['business_id']).first()
        user_review['Business']['PreviewImage'] = img.to_dict() if img else None
        user_review['Review_Images'] = [img.to_dict() for img in Image.query.filter(user_review['id'] == Image.review_id).all()]

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

            # DELETE ALL THE REVIEW IMAGES FIRST
            review_imgs_to_delete = Image.query.filter(Image.review_id == review_id).all()

            for img in review_imgs_to_delete:
                url = img.to_dict()['url']
                deleteMsg = delete_file_from_s3(url)
                if not deleteMsg:
                    { "message": "Successfully deleted from AWS" }

            # THEN DELETE THE ACTUAL REVIEW:
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
    if "image" not in request.files:
        return {"errors": "image required"}, 400

    image = request.files["image"]

    if not allowed_file(image.filename):
        return {"errors": "file type not permitted"}, 400

    image.filename = get_unique_filename(image.filename)

    upload = upload_file_to_s3(image)

    if "url" not in upload:
        # if the dictionary doesn't have a url key
        # it means that there was an error when we tried to upload
        # so we send back that error message
        return upload, 400

    url = upload["url"]
    # flask_login allows us to get the current user from the request
    # new_image = Image(user=current_user, url=url)
    # db.session.add(new_image)
    # db.session.commit()
    # return {"url": url}

    form = AddReviewImgForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    review = Review.query.get(review_id)

    if not review:
        return jsonify({
            "message": "Review couldn't be found",
            "status_code": 404
        }), 404

    # Body validation error handlers:
    login_val_error = {
        "message": "Validation error",
        "status_code": 400,
        "errors": {}
    }

    if not url:
        login_val_error["errors"]["url"] = "Image url is required"
    if len(login_val_error["errors"]) > 0:
        return jsonify(login_val_error), 400

    if form.validate_on_submit():
        user = current_user.to_dict()

        if review.to_dict()['user_id'] == user['id']:
            biz_id = review.to_dict()['business_id']

            review_img = Image(
                review_id = review_id,
                business_id = biz_id,
                url = url
            )

            db.session.add(review_img)
            db.session.commit()

            return review_img.to_dict()

        else:
            return { "message": "Forbidden", "status_code": 403 }, 403

    return {'errors': validation_errors_to_error_messages(form.errors)}, 400


# 6. DELETE A REVIEW IMG
@reviews_routes.route("/images/<int:image_id>", methods=['DELETE'])
@login_required
def delete_review_img(image_id):
    """
    Deletes a review image
    """
    form = DeleteReviewImgForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    review_img_to_delete = Image.query.get(image_id)

    url = review_img_to_delete.to_dict()['url']

    if not review_img_to_delete:
        return jsonify({
            "message": "Review couldn't be found",
            "status_code": 404
        }), 404

    user = current_user.to_dict()

    # FIND OWNER OF REVIEW IMG:
    review_id = review_img_to_delete.to_dict()['review_id']
    review = Review.query.get(review_id)
    review_owner_id = review.to_dict()['user_id']


    if review_owner_id == user['id']:
        deleteMsg = delete_file_from_s3(url)
        if not deleteMsg:
            { "message": "Successfully deleted from AWS" }

        db.session.delete(review_img_to_delete)
        db.session.commit()

        return { "message": "Successfully deleted", "status_code": 200 }

    else:
        return { "message": "Forbidden", "status_code": 403 }, 403



    # if form.validate_on_submit():
    #     user = current_user.to_dict()

    #     # FIND OWNER OF REVIEW IMG:
    #     review_id = review_img_to_delete.to_dict()['review_id']
    #     review = Review.query.get(review_id)
    #     review_owner_id = review.to_dict()['user_id']


    #     if review_owner_id == user['id']:
    #         db.session.delete(review_img_to_delete)

    #         db.session.commit()

    #         return { "message": "Successfully deleted", "status_code": 200 }

    #     else:
    #         return { "message": "Forbidden", "status_code": 403 }, 403

    # return { "message": "Review couldn't be found", "status_code": 404 }, 404
