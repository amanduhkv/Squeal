from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, ValidationError

# ------ CUSTOM VALIDATORS ------ #
def check_review(form, field):
    # password = field.data
    review = form.data['review_body']
    if not review:
        raise ValidationError('Review text is required')

def check_rating(form, field):
    # password = field.data
    rating = form.data['rating']
    if not rating:
        raise ValidationError('Rating is required')
    if rating < 1 or rating > 5:
        raise ValidationError('Rating must be an integer from 1 to 5')


class EditReviewForm(FlaskForm):
    review_body = StringField('Review Body', validators=[check_review])
    rating = IntegerField('Rating', validators=[DataRequired(), check_rating])
    # # submit button not necessary
    # submit = SubmitField('Submit')
