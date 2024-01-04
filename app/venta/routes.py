from flask import redirect, render_template, request, url_for

from app.venta.models.VentaModel import VentaModel
from . import venta
from .forms import VentaForm

from flask_login import login_user, login_manager, logout_user, login_required

@venta.route('/venta')
@login_required
def ventaPage():
    form = VentaForm()
    ventas = VentaModel.listar_ventas()
    page = request.args.get('page', 1, type=int)
    per_page = 5
    total_pages = (len(ventas) + per_page - 1) // per_page
    items_on_page = ventas[(page - 1) * per_page: page * per_page]
    return render_template('venta.html', form=form, ventas=items_on_page, total_pages=total_pages, page=page, mostrar_modal=form.errors)

@venta.route('/venta', methods=['POST'])
@login_required
def ingresarVenta():
    form = VentaForm()
    if form.validate_on_submit():
        return redirect(url_for('venta.ventaPage'))
    return render_template('venta.html', form=form, mostrar_modal=form.errors)