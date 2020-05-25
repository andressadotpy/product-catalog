from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class SellerForm(FlaskForm):
    """Form for admin user add or edit a seller."""
    seller_name = StringField('Name', validators=[DataRequired()])
    seller_email = StringField('Email', validators=[Length(1, 64), Email()])
    seller_phone = StringField('Phone', validators=[DataRequired()])
    seller_site = StringField('Site')
    submit = SubmitField('Submit')
