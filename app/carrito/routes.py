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

        #cantidad de productos de la lista sesión['carrito']
        if 'carrito' not in session:
            totalproductos = 0
        else:
            totalproductos = len(session['carrito'])
                        

        return render_template('carrito.html', productos=productos, form=formProducto, totalproductos=totalproductos)
    except Exception as error: 
        print(error)
        return error


@carrito.route('/carrito')
@login_required
def verCarrito():
    try:
        # Verifica si hay un carrito en la sesión
        if 'carrito' in session:
            print("Hay un carrito en la sesión.")
            print("Productos en el carrito:", session['carrito'])
            
            #precio total
            totalprecio = 0
            for producto in session['carrito']:
                totalprecio += (producto['precio'] * producto['cantidad'])
                    
            return render_template('vercarrito.html', total=totalprecio)
        else:
            print("No hay un carrito en la sesión.")
            return render_template('vercarrito.html', carrito=[] ,total=0)
    except Exception as error:
        print("Error al conectar a MySQL:", error)
        return error


@carrito.route('/comprar/<int:preciototal>')
def comprarCarrito(preciototal):
    carrito_datos = session['carrito']
    carrito_guardado = ModelCarrito.comprarDetallesCarrito(carrito_datos, preciototal)
    
    if carrito_guardado:
        # Eliminar la sesión del carrito
        if 'carrito' in session:
            session.pop('carrito')
        session.modified = True
        flash('Carrito comprado', 'success')
    else:
        flash('Error al comprar el carrito', 'danger')

    return redirect(url_for('carrito.verCarrito'))

@carrito.route('/agregar/<int:producto_id>/<producto_nombre>/<float:producto_precio>/<int:producto_cantidad>', methods=['POST'])
def agregar_producto(producto_id, producto_nombre, producto_precio, producto_cantidad):

    if 'carrito' not in session:
        session['carrito'] = []

    cantidad = int(request.form.get('cantidad'))  # Obtener la cantidad del formulario, usar 1 por defecto si no se proporciona

    if cantidad > producto_cantidad:
        flash("No hay suficiente stock de este producto", 'danger')
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
        flash("Producto agregado al carrito", 'success')
    else:
        flash("El producto ya se encuentra en el carrito", 'info')

    print("Productos en el carrito:", session['carrito'])
    return redirect(url_for('carrito.mostrarProductos'))


@carrito.route('/eliminar/<int:producto_id>')
def eliminar_producto(producto_id):
    if 'carrito' in session:
        carrito_productos = session['carrito']
        # Encuentra el index del producto en el carrito para eliminarlo
        index_to_remove = next((index for index, producto in enumerate(carrito_productos) if producto['id'] == producto_id), None)

        if index_to_remove is not None:
            # remueve el producto de la lista
            carrito_productos.pop(index_to_remove)
            session.modified = True  # marcar la sesión como modificada
    return redirect(url_for('carrito.verCarrito'))


@carrito.route('/vaciar_carrito')
def vaciar_carrito():
    # Eliminar la sesión del carrito
    if 'carrito' in session:
        session.pop('carrito')
    session.modified = True
    return redirect(url_for('carrito.mostrarProductos'))