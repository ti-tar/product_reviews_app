from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ReviewForm(FlaskForm):
    """ Review form for product """

    title = StringField('Title', validators=[
        DataRequired('Please fill this field.'),
    ])

    review = StringField('review', validators=[
        DataRequired('Please fill this field.'),
    ])

    submit = SubmitField('Add review')
