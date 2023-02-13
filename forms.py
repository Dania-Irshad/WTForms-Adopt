from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, NumberRange, URL, Optional


class AddPetForm(FlaskForm):
    """Add Pets Form"""
    name = StringField("Pet Name",
                       validators=[InputRequired()])
    species = SelectField("Species", choices=[("cat", "Cat"), 
                          ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()])
    age = IntegerField("Age",
                       validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes",
                          validators=[Optional()])


class EditPetForm(FlaskForm):
    """Edit Existing Pet Form."""

    photo_url = StringField("Photo URL", 
                            validators=[Optional(), URL()])

    notes = TextAreaField("Notes",
                          validators=[Optional()])

    available = BooleanField("Available")