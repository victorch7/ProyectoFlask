from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, DataRequired, Email, Length, Regexp, EqualTo

class LoginForm(FlaskForm):
    
    usuario = StringField('Usuario', validators=[
        DataRequired(message='Campo de usuario requerido'),
        Email(message='Formato de usuario inválido, Ej: juan@gmail.com')
    ])
    contrasena = PasswordField('Contrasena', validators=[
        InputRequired(message='Campo de contrasena requerido'),
        Length(min=6, message='La contraseña debe tener al menos 6 caracteres')
    ])
    submit = SubmitField('Ingresar')

class RegisterForm(FlaskForm):
        nombre = StringField('Nombre', validators=[
        DataRequired(message='Campo de nombre requerido'),
        Regexp(r'^[a-zA-Z\s]+$', message='El nombre solo puede contener letras')
    ])
        usuario = StringField('Usuario', validators=[
        DataRequired(message='Campo de usuario requerido'),
        Email(message='Formato de usuario inválido, Ej: juan@gmail.com')
    ])
        telefono = StringField('Telefono', validators=[
        DataRequired(message='Campo de telefono requerido'),
        Length(min=10, message='El número de teléfono debe tener 10 dígitos')
    ])
        direccion = StringField('Direccion', validators=[
        DataRequired(message='Campo de dirección requerido')
    ])
        contrasena = PasswordField('Contrasena', validators=[
        InputRequired(message='Campo de contrasena requerido'),
        Length(min=6, message='La contraseña debe tener al menos 6 caracteres')
    ])
        confirmar_contrasena = PasswordField('Confirmar Contrasena', validators=[
        InputRequired(message='Campo de confirmación de contraseña requerido'),
        EqualTo('contrasena', message='Las contraseñas deben coincidir')
    ])

        submit = SubmitField('Ingresar')