from flask import flash, render_template, current_app, session, redirect, url_for, session, jsonify, request
from flask_login import login_required

#modelos
from .models.ModelCarrito import ModelCarrito

#entidades

#blueprint
from . import carrito

#formulario cantidad
from .form import AgregarProductoForm


@carrito.route('/productos', methods=['POST', 'GET'])
@login_required
def mostrarProductos():
    try:
        formProducto = AgregarProductoForm()
        productos = ModelCarrito.mostrarListaProductos()
        return render_template('carrito.html', productos=productos, form=formProducto)

    except Exception as error: 
        print(error)
        return "Error al conectar a MySQL"


@carrito.route('/carrito')
@login_required
def verCarrito():
    try:
        # Verifica si hay un carrito en la sesión
        if 'carrito' in session:
            print("Hay un carrito en la sesión.")
            print("Productos en el carrito:", session['carrito'])
            carrito_productos = session.get('carrito', [])
            return render_template('vercarrito.html', carrito=carrito_productos)
        else:
            print("No hay un carrito en la sesión.")
            return render_template('vercarrito.html')
    except Exception as error:
        print("Error al conectar a MySQL:", error)
        return error



@carrito.route('/agregar/<int:producto_id>/<producto_nombre>/<float:producto_precio>/<int:producto_cantidad>', methods=['POST'])
def agregar_producto(producto_id, producto_nombre, producto_precio, producto_cantidad):

    if 'carrito' not in session:
        session['carrito'] = []

    cantidad = int(request.form.get('cantidad'))  # Obtener la cantidad del formulario, usar 1 por defecto si no se proporciona

    if cantidad > producto_cantidad:
        flash("No hay suficiente stock de este producto", 'error')
        return redirect(url_for('carrito.mostrarProductos'))

    if not session['carrito'] or producto_id not in [item['id'] for item in session['carrito']]:
        # Guardar información del producto en la sesión
        session['carrito'].append({
            'id': producto_id,
            'nombre': producto_nombre,
            'precio': producto_precio,
            'cantidad': cantidad
        })
        session.modified = True  # Marcar la sesión como modificada

    print("Productos en el carrito:", session['carrito'])

    return redirect(url_for('carrito.mostrarProductos'))



@carrito.route('/eliminar/<int:producto_id>')
def eliminar_producto(producto_id):
    if 'carrito' in session:
        carrito_productos = session['carrito']

        # Find the index of the product with the specified id
        index_to_remove = next((index for index, producto in enumerate(carrito_productos) if producto['id'] == producto_id), None)

        if index_to_remove is not None:
            # Remove the product from the list
            removed_product = carrito_productos.pop(index_to_remove)
            session.modified = True  # Mark the session as modified

    return redirect(url_for('carrito.verCarrito'))


@carrito.route('/vaciar_carrito')
def vaciar_carrito():
    # Eliminar la sesión del carrito
    session.pop('carrito', None)

    return redirect(url_for('carrito.mostrarProductos'))