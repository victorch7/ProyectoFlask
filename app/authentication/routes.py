from . import authentication_bp
from flask import render_template, request, current_app

@authentication_bp.route("/login", methods=["GET","POST"])
def login():
        return render_template("login.html")
  
@authentication_bp.route("/register")
def register(): 
        return render_template('registro.html')

@authentication_bp.route("/add_usuario", methods=['POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        password = request.form['password']

        mysql = current_app.config['mysql']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuarios (nombre, apellido, email, telefono, password) VALUES (%s, %s, %s, %s, %s)',
                    (nombre, apellido, email, telefono, password))
        mysql.connection.commit()
        cur.close()

        return "Registrado exitosamente"
    return "Error en el registro"
