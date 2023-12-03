from flask import redirect, render_template, url_for, request, flash, current_app
from flask_mysqldb import MySQL

# blueprints
from . import auth

# formulario
from .forms import LoginForm

# modelos
from .models.ModelClient import ModelClient

# entidades
from .models.entities.Client import Client

db = MySQL()

@auth.route('/ingresar', methods=['POST'])
def prueba():
    if request.method == 'POST':
        form = LoginForm()
        if form.validate_on_submit():
            client = Client('','',request.form.get('usuario'),'','',request.form.get('contrasena'),'','')
            logged_client = ModelClient.login(db,client)

            if logged_client != None:
                if logged_client.password:
                    print(client)
                    flash("Ingreso exitoso")
                    return redirect(url_for('carrito.carrito'))

                else:
                    flash("Contraseña incorrecta")
            else:
                flash("Usuario no encontrado")


@auth.route('/login', methods=['GET'])
def login():
    form = LoginForm()

    return render_template('login.html', form=form)

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