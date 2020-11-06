from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class searchForm(FlaskForm):
    search_term = StringField('Search Term', validators=[DataRequired()])
    submit = SubmitField('Search')

class categoryForm(FlaskForm):
    category_form = SelectField("Category", choices = [("Technology", "Technology"), ("Sports", "Sports"), ("Entertainment", "Entertainment")])