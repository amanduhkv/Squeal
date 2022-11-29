from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class AddReviewImgForm(FlaskForm):
    url = StringField('Review Image URL')
    submit = SubmitField('Submit')
