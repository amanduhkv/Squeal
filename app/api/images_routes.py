from flask import Blueprint, request
from flask_login import current_user, login_user, logout_user, login_required
from ..models import db, Image
from ..forms.delete_review_img_form import DeleteReviewImgForm

images_routes = Blueprint("images", __name__)


# DELETE A REVIEW IMG
@images_routes.route("/<int:image_id>", methods=['DELETE'])
@login_required
def delete_review_img(image_id):
    """
    Deletes a review image
    """
    form = DeleteReviewImgForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        review_img_to_delete = Image.query.get(image_id)
        user = current_user.to_dict()
        if review_img_to_delete.user_id == user['id']:
            review_img_to_delete.session.delete()

            db.session.commit()

            return { "message": "Successfully delete", "status_code": 200 }
        else:
            return { "message": "Forbidden", "status_code": 403 }

    # return {'errors': validation_errors_to_error_messages(form.errors)}, 401
    return { "message": "Review couldn't be found", "status_code": 404 }
