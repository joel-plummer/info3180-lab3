from flask_wtf import *
from wtforms import *
from wtforms.validators import *

class ContactForm(FlaskForm):
    name = StringField('Name  ', validators=[InputRequired()])
    email = EmailField('E-mail  ', validators=[InputRequired(), Email()])
    subject = StringField('Subject  ', validators=[InputRequired()])
    message = TextAreaField('Message  ', validators=[InputRequired()])