from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length


class CreateDepotForm(FlaskForm):
    """Create new depot form."""
    name = StringField("Name", [DataRequired()])
    description = StringField("Beschreibung")
    submit = SubmitField("Bestätigen")
