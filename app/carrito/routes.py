from flask import render_template, current_app,redirect,url_for,session,jsonify,request
from flask_login import login_required
from flask_mysqldb import MySQL

from . import carrito

@carrito.route('/carrito', methods=['POST', 'GET'])
@login_required
def mostrar_carrito():
    try:
        conexion = current_app.conexion() 
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, categoria, descripcion, imagen, precio, stock FROM producto")
        productos = cursor.fetchall()
        conexion.close()
        return render_template('carrito.html', productos=productos)

    except Exception as error: 
        print("Error al conectar a MySQL:", error)
        return "Error al conectar a MySQL"
    

@carrito.route('/vercarrito')
@login_required
def vercarrito():
    try:
        conexion = current_app.conexion() 
        cursor = conexion.cursor()
        cursor.execute("SELECT carrito.idCarrito, producto.nombre, producto.precio, producto.imagen, carrito.cantidad FROM carrito INNER JOIN producto ON carrito.idProducto = producto.id")
        carrito = cursor.fetchall()
        cursor.close()
        conexion.close()
        return render_template('vercarrito.html', carrito=carrito)
    except Exception as error: 
        print("Error al conectar a MySQL:", error)
        return "Error al conectar a MySQL"


# @carrito.route('/agregar-al-carrito/<int:id>', methods=['POST'])
# @login_required
# def agregar_al_carrito(id):
#     cursor = None
#     try:
#         _cant = int(request.form['cant'])
#         _idProd = request.form['idProd']
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close() 
#         conexion.close()