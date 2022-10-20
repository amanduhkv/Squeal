from flask import Blueprint, jsonify, request
from flask_login import current_user, login_user, logout_user, login_required
from ..models import db, Image, Review, Business
from ..forms.delete_review_img_form import DeleteReviewImgForm

images_routes = Blueprint("images", __name__)


# DELETE A REVIEW IMG
# @images_routes.route("/<int:image_id>", methods=['DELETE'])
# @login_required
# def delete_review_img(image_id):
#     """
#     Deletes a review image
#     """
#     form = DeleteReviewImgForm()
#     form['csrf_token'].data = request.cookies['csrf_token']

#     review_img_to_delete = Image.query.get(image_id)
#     if not review_img_to_delete:
#         return jsonify({
#             "message": "Review couldn't be found",
#             "status_code": 404
#         }), 404

#     if form.validate_on_submit():
#         user = current_user.to_dict()

#         # FIND OWNER OF REVIEW IMG:
#         review_id = review_img_to_delete.to_dict()['review_id']
#         review = Review.query.get(review_id)
#         review_owner_id = review.to_dict()['user_id']


#         if review_owner_id == user['id']:
#             db.session.delete(review_img_to_delete)

#             db.session.commit()

#             return { "message": "Successfully deleted", "status_code": 200 }

#         else:
#             return { "message": "Forbidden", "status_code": 403 }, 403

#     return { "message": "Review couldn't be found", "status_code": 404 }, 404


# @images_routes.route("/<int:img_id>", methods=['DELETE'])
# @login_required
# def delete_business_img(img_id):
#     """
#     DELETES a business image
#     """
#     user = current_user.to_dict()
#     user_id = user['id']

#     biz_img_to_delete = Image.query.get(img_id)
#     if not biz_img_to_delete:
#         return jsonify({
#             "message": "Image couldn't be found",
#             "status_code": 404
#         })

#     # biz_of_img = Business.query.get(biz_img_to_delete.to_dict()['business_id']).to_dict()
#     biz_img_biz_id = biz_img_to_delete.to_dict()['business_id']
#     biz_of_img = Business.query.get(biz_img_biz_id)

#     if user_id == biz_of_img['owner_id']:
#         db.session.delete(biz_img_to_delete)
#         db.session.commit()
#         return { "message": "Successfully deleted", "status_code": 200 }
#     else:
#         return { "message": "Forbidden", "status_code": 403 }, 403
