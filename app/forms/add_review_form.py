from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class AddReviewForm(FlaskForm):
    # business_id = IntegerField('Business ID', validators=[DataRequired()])
    # user_id = IntegerField('User ID', validators=[DataRequired()])
    review_body = StringField('Review Body', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    submit = SubmitField('Submit')
