from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField
from wtforms.validators import DataRequired


class ShortyForm(FlaskForm):
    url = StringField('Insert your URL here', validators=[DataRequired()])
    submit = SubmitField('Shorten')
