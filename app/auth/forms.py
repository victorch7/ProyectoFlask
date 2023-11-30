from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, DataRequired, Email
from wtforms.validators import Length

class LoginForm(FlaskForm):
    usuario = StringField('Usuario',
                           validators=[
                               DataRequired(message='Campo de usuario requerido'),

                               ])
    contrasena = PasswordField('Contrasena', validators=[
                                InputRequired(message='Campo de contrasena requerido'),
                                DataRequired()  
                                ])
    submit = SubmitField('Ingresar')