from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class ReviewForm(FlaskForm):
    """ Review form for product """

    title = StringField('Title', validators=[
        DataRequired('Please fill this field.'),
    ])

    review = TextAreaField('review', validators=[
        DataRequired('Please fill this field.'),
    ])

    submit = SubmitField('Add review')
