from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, DataRequired, Email, Length,Regexp

class LoginForm(FlaskForm):
    
    usuario = StringField('Usuario', validators=[
        DataRequired(message='Campo de usuario requerido')
        # Email(message='Formato de usuario inválido, Ej: juan@gmail.com')
    ])
    contrasena = PasswordField('Contrasena', validators=[
        InputRequired(message='Campo de contrasena requerido'),
        Length(min=6, message='La contraseña debe tener al menos 6 caracteres')
    ])
    submit = SubmitField('Ingresar')
