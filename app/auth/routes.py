from flask import render_template, request, current_app, redirect, url_for
from . import auth
from .forms import LoginForm

@auth.route('/')
def index():
    return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@auth.route('/ingresar',  methods=['POST'])
def ingresar():
    form = LoginForm()
    if form.validate_on_submit():
        # Aquí puedes manejar la lógica de inicio de sesión con los datos del formulario
        # Por ejemplo, podrías verificar las credenciales y redirigir al usuario
        return redirect(url_for('inicio.dashboard'))
    return render_template('login.html', form=form)

@auth.route("/registro")
def register(): 
        form = LoginForm()
        return render_template('registro.html')

@auth.route("/add_usuario", methods=['POST'])
def add():
        if request.method == 'POST':
                _nombre = request.form['nombre']
                _apellido = request.form['apellido']
                _telefono = request.form['telefono']
                _email = request.form['email']
                _password = request.form['password']
                
                sql = "INSERT INTO usuario (nombre, apellido, telefono, email, password) VALUES (%s, %s, %s, %s, %s)"
                datos = (_nombre, _apellido, _telefono, _email, _password)
                
                try:
                        conexion = current_app.conexion()
                        cursor = conexion.cursor()
                        cursor.execute(sql,datos)
                        conexion.commit()
                        conexion.close()
                        mensaje = "¡Datos insertados correctamente en la base de datos!"
                except Exception as e:
                        mensaje = f"Error al insertar datos: {str(e)}"
                
                return mensaje
        return mensaje