import email_validator
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField


class SellerForm(FlaskForm):
    """Form for admin user add or edit a seller."""
    seller_name = StringField('Name', validators=[DataRequired()])
    seller_email = StringField('Email', validators=[Length(1, 64), Email()])
    seller_phone = StringField('Phone', validators=[DataRequired()])
    seller_site = StringField('Site')
    submit = SubmitField('Submit')


class CategoryForm(FlaskForm):
    """Form for admin user add or edit a category for the products."""
    category = StringField('Category name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class ProductForm(FlaskForm):
    """Form for admin user add products and assign it for categories and sellers."""
    product_name = StringField('Name', validators=[DataRequired()])
    sellers = QuerySelectMultipleField(query_factory=lambda: Seller.query.all(), get_label='sellers name')
    category = QuerySelectField(query_factory=lambda: Category.query.all(), get_label='category name')
    submit = SubmitField('Submit')
