from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length


class CreateDepotForm(FlaskForm):
    name = StringField("Name", [DataRequired()])
    description = StringField("Beschreibung")
    submit = SubmitField("Bestätigen")


class BuyShareForm(FlaskForm):
    #share_name = StringField("Firma")
    symbol = StringField("Tickersymbol")
    submit = SubmitField("Suchen")
    amount = IntegerField("Anzahl")
    buybutton = SubmitField("Kaufen")
