from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class AddBizImgForm(FlaskForm):
    url = StringField('Review Image URL', validators=[DataRequired()])
    submit = SubmitField('Submit')
