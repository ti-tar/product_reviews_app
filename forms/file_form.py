from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField


class FileForm(FlaskForm):
    """ ... """
    file = FileField("CSV File", validators=[])
    submit = SubmitField('Submit')
