from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, DataRequired, Email
from wtforms.validators import Length

class CategoriaForm(FlaskForm):
    categoriaNombre = StringField('Nombre de la categoría', validators=[InputRequired(message="Ingrese nombre de la categoría")])