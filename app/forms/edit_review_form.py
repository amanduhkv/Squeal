from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class EditReviewForm(FlaskForm):
    review_body = StringField('Review Body', validators=[DataRequired()])
    rating = IntegerField('Rating', validators=[DataRequired()])
    # # submit button not necessary
    # submit = SubmitField('Submit')
