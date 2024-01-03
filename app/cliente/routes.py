from flask import redirect, render_template, url_for, request
from . import cliente
from .forms import ClienteForm

#modelos
from .models.ClienteModel import ClienteModel

#entidades
from .models.entities.ClienteEntity import Cliente

from flask_login import login_user, login_manager, logout_user, login_required


@cliente.route('/cliente', methods=['GET'])
@login_required
def clientePage():
    form = ClienteForm()

    clientes = ClienteModel.listar_clientes()

    page = request.args.get('page', 1, type=int)
    per_page = 5
    total_pages = (len(clientes) + per_page - 1) // per_page
    items_on_page = clientes[(page - 1) * per_page: page * per_page]

    return render_template(template_name_or_list='cliente.html', form=form, clientes=clientes, items_on_page=items_on_page, total_pages=total_pages, page=page, mostrar_modal=form.errors)   

@cliente.route('/ingresar_cliente', methods=['POST'])
@login_required
def ingresarCliente():
    form = ClienteForm()
    if form.validate_on_submit():
        cliente = Cliente('', request.form.get('clienteNombre'), request.form.get('clienteContrasena'), request.form.get('clienteDireccion'), request.form.get('clienteTelefono'), request.form.get('clienteEmail'), request.form.get('clienteFechaNacimiento'),'')
        cliente_registrado = ClienteModel.register(cliente)
        print(cliente)
        if cliente_registrado:
            print("cliente registrado")
        else:
            print("No se pudo registrar el cliente")

        return redirect(url_for('cliente.clientePage'))
    
    #paginacion
    clientes = ClienteModel.listar_clientes()

    page = request.args.get('page', 1, type=int)
    per_page = 5
    total_pages = (len(clientes) + per_page - 1) // per_page
    items_on_page = clientes[(page - 1) * per_page: page * per_page]

    return render_template('cliente.html', form=form, clientes=clientes, items_on_page=items_on_page, total_pages=total_pages, page=page, mostrar_modal=form.errors)