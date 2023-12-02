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
        if request.method == 'POST':
                form = LoginForm()
                if form.validate_on_submit():
                        # Aquí puedes manejar la lógica de inicio de sesión con los datos del formulario
                        # Por ejemplo, podrías verificar las credenciales y redirigir al usuario
                        return render_template('carritoCompras.carrito.html')  # Redirigir a la vista del carrito después del inicio de sesión exitoso
        return render_template('login.html')

@auth.route("/registro", methods=['GET', 'POST'])
def register(): 
    form = LoginForm()
    if form.validate_on_submit():
        _nombre = request.form['nombre']
        _usuario = request.form['usuario']
        _telefono = request.form['telefono']
        _direccion = request.form['direccion']
        _password = request.form['contrasena']
        
        sql = "INSERT INTO cliente (nombre, usuario, telefono, direccion, password) VALUES (%s, %s, %s, %s, %s)"
        datos = (_nombre, _usuario, _telefono, _direccion, _password)
        
        try:
            conexion = current_app.conexion()
            cursor = conexion.cursor()
            cursor.execute(sql,datos)
            conexion.commit()
            conexion.close()
            return redirect(url_for('auth.login'))  # Redirigir al inicio de sesión después del registro exitoso
        except Exception as e:
            mensaje = f"Error al insertar datos: {str(e)}"
            return render_template('registro.html', form=form, mensaje=mensaje)
    return render_template('registro.html', form=form)
