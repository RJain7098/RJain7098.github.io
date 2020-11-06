from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class masterForm(FlaskForm):
    search_term = StringField('Search Term', validators=[DataRequired()])
    submit = SubmitField('Search')
    category_form = SelectField("Category", choices = 
        [("Technology", "Technology"), ("Sports", "Sports"), ("Entertainment", "Entertainment")])