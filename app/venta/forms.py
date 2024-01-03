from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DecimalField, SelectField, DateField
from wtforms.validators import InputRequired

class VentaForm(FlaskForm):
    ventaCliente = StringField('Cliente', validators=[InputRequired(message="Ingrese nombre del cliente")])
    ventaProductos = TextAreaField('Productos', validators=[InputRequired(message="Ingrese los productos")])
    ventaTotal = DecimalField('Total', validators=[InputRequired(message="Ingrese el total de la venta")])
    opciones_metodo_pago = [('', 'Seleccione método de pago'), ('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta')]
    ventaMetodoPago = SelectField('Método de pago', choices=opciones_metodo_pago, validators=[InputRequired(message="ingrese el método de pago")])
    ventaFecha = DateField('Fecha', validators=[InputRequired(message="ingrese fecha de la venta")])
    # Otros campos del formulario
