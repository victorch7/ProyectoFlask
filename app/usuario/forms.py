from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField
from wtforms.validators import InputRequired

class UsuarioForm(FlaskForm):
    usuarioNombre = StringField('Nombre del usuario', validators=[InputRequired(message="Ingrese nombre del usuario")])
    usuario = StringField('Nombre de usuario', validators=[InputRequired(message="Ingrese apodo del usuario")])
    contrasena = PasswordField('Contraseña', validators=[InputRequired(message="Contraseña requerida")])
    opciones_perfil = [('','Seleccione una opción'),('administrador', 'Administrador')]
    usuarioPerfil = SelectField('Perfil del usuario', choices=opciones_perfil, validators=[InputRequired(message="Seleccione un perfil del usuario")])
    opciones_estado = [('','Seleccione una opción'),(True, 'Activo'), (False, 'Inactivo')]
    usuarioEstado = SelectField('Estado del usuario', choices=opciones_estado, validators=[InputRequired(message="Seleccione un estado del usuario")])

    # usuarioEstado = StringField('Estado', validators=[InputRequired(message="El usuario debe tener un estado")])
"""     usuarioUltimoLogin = StringField('Último login', validators=[InputRequired()]) """

