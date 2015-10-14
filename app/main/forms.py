__author__ = 'jenking'

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(Form):
    name = StringField('Hi,What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
