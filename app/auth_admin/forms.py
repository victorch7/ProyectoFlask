from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    usuario = StringField('Usuario',
                          validators=[DataRequired(message='Campo de usuario requerido')],
                          render_kw={'placeholder': 'Usuario'})
    contrasena = PasswordField('Contraseña',
                                validators=[DataRequired(message='Campo de contraseña requerido')],
                                render_kw={'placeholder': 'Contraseña'})
    submit = SubmitField('Ingresar', render_kw={'class': 'btn btn-primary'})
