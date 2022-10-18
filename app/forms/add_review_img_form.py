from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class AddReviewImgForm(FlaskForm):
    # review_id = IntegerField('Review ID', validators=[DataRequired()])
    # business_id = IntegerField('Business ID', validators=[DataRequired()])
    url = StringField('Review Image URL', validators=[DataRequired()])
    submit = SubmitField('Submit')
