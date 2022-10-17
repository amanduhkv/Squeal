from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class AddBusinessForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])

    submit = SubmitField('Submit')
