from flask import redirect, render_template, url_for, request

from . import categoria
from .forms import CategoriaForm

#modelo
from .models.CategoriaModel import CategoriaModel

#entidad
from .models.entities.CategoriaEntity import Categoria

from flask_login import login_user, login_manager, logout_user, login_required



@categoria.route('/categoria', methods=['GET'])
@login_required
def categoriaPage():
    form = CategoriaForm()

    categoria = CategoriaModel.listar_categorias()

    #Paginación
    page = request.args.get('page', 1, type=int)
    per_page = 5
    total_pages = (len(categoria) + per_page - 1) // per_page
    items_on_page = categoria[(page - 1) * per_page: page * per_page]

    return render_template(template_name_or_list='categoria.html', form=form, categoria=categoria, items_on_page=items_on_page, total_pages=total_pages, page=page, mostrar_modal=form.errors)

@categoria.route('/ingresar_categoria', methods=['POST'])
@login_required
def ingresarCategoria():
    form = CategoriaForm()
    if form.validate_on_submit():
        categoria = Categoria('',request.form.get('categoriaNombre'), '')
        categoria_registrada = CategoriaModel.register(categoria)
        if categoria_registrada:
            print("categoria registrada")
        else:
            print("No se pudo registrar la categoria")
        return redirect(url_for('categoria.categoriaPage'))

    #Obtener campos para la paginación
    categoria = CategoriaModel.listar_categorias()
    
    # Resto del código para la paginación
    page = request.args.get('page', 1, type=int)
    per_page = 5

    total_pages = (len(categoria) + per_page - 1) // per_page
    items_on_page = categoria[(page - 1) * per_page: page * per_page]

    return render_template(template_name_or_list='categoria.html', form=form, categoria=categoria, items_on_page=items_on_page, total_pages=total_pages, page=page, mostrar_modal=form.errors)
 
