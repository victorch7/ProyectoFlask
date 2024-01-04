from flask import redirect, render_template, url_for, request


from . import producto
from .forms import ProductoForm

#imagen
from werkzeug.utils import secure_filename
import os
from flask import current_app

#modelo
from .models.ProductModel import ProductoModel


#entidad
from .models.entities.ProductoEntity import Producto

from flask_login import login_user, login_manager, logout_user, login_required

from decouple import config

@producto.route('/producto', methods=['GET'])
@login_required
def productoPage():
    form = ProductoForm()
    #Obtener campos para la paginación
    producto = ProductoModel.listar_productos() 
    # Resto del código para la paginación
    page = request.args.get('page', 1, type=int)
    per_page = 5
    total_pages = (len(producto) + per_page - 1) // per_page
    items_on_page = producto[(page - 1) * per_page: page * per_page]

    return render_template(template_name_or_list='producto.html', form=form, producto=producto, items_on_page=items_on_page, total_pages=total_pages, page=page, mostrar_modal=form.errors)

@producto.route('/ingresar_producto', methods=['POST'])
@login_required
def ingresarProducto():
    form = ProductoForm()
    if form.validate_on_submit():
        if form.validate_on_submit():

            image_file = form.productoImagen.data

            if image_file is not None:
                filename = secure_filename(image_file.filename)
                image_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            else:
                # Manejar el caso en que no se subió un archivo
                filename = "default_image.jpg"  # Por ejemplo, usa una imagen predeterminada

            producto = Producto('',request.form.get('productoNombre'), request.form.get('productoCategoria'), request.form.get('productoDescripcion'), filename, request.form.get('productoPrecio'), request.form.get('productoStock')) 
            producto_registrado = ProductoModel.register(producto)
            
            if producto_registrado:
                print("categoria registrada")
            else:
                print("No se pudo registrar la categoria")
            return redirect(url_for('producto.productoPage'))

    #Obtener campos para la paginación
    producto = ProductoModel.listar_productos()
    
    # Resto del código para la paginación
    page = request.args.get('page', 1, type=int)
    per_page = 5

    total_pages = (len(producto) + per_page - 1) // per_page
    items_on_page = producto[(page - 1) * per_page: page * per_page]
        
    return render_template(template_name_or_list='producto.html', form=form, producto=producto, items_on_page=items_on_page, total_pages=total_pages, page=page, mostrar_modal=form.errors)


@producto.route('/eliminar_producto/<int:id>', methods=['POST'])
def eliminarProducto(id):
    ProductoModel.eliminar_producto(id)
    return redirect(url_for('producto.productoPage'))