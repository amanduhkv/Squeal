from flask_wtf import FlaskForm
from wtforms import SubmitField


class DeleteBusinessForm(FlaskForm):
    submit = SubmitField('Submit')
