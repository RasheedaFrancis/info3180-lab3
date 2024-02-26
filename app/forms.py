from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, validators, TextAreaField
from wtforms.validators import InputRequired


class ContactForm(FlaskForm):
    name = StringField('Name',
    validators = [InputRequired()])
    email = EmailField('Email address',
    [validators.DataRequired(), 
    validators.Email()])

    subject = StringField('Subject',
    validators = [InputRequired()])

    message = TextAreaField('Message',
    validators = [InputRequired()])