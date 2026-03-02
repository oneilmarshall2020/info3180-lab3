from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[
            DataRequired(message="Please enter your name."),
            Length(min=2, max=100, message="Name must be between 2 and 100 characters.")
        ]
    )

    email = StringField(
        'Email',
        validators=[
            DataRequired(message="Please enter your email address."),
            Email(message="Please enter a valid email address.")
        ]
    )

    subject = StringField(
        'Subject',
        validators=[
            DataRequired(message="Please enter a subject."),
            Length(min=2, max=150, message="Subject must be between 2 and 150 characters.")
        ]
    )

    message = TextAreaField(
        'Message',
        validators=[
            DataRequired(message="Please enter your message."),
            Length(min=10, message="Message must be at least 10 characters long.")
        ]
    )

    submit = SubmitField('Send Message')