from flask import redirect, render_template, url_for
from . import venta
from .forms import VentaForm

from flask_login import login_user, login_manager, logout_user, login_required

@venta.route('/venta')
@login_required
def ventaPage():
    form = VentaForm()
    return render_template('venta.html', form=form)

@venta.route('/venta', methods=['POST'])
@login_required
def ingresarVenta():
    form = VentaForm()
    if form.validate_on_submit():
        return redirect(url_for('venta.ventaPage'))
    return render_template('venta.html', form=form, mostrar_modal=form.errors)