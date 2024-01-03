from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, IntegerField
from wtforms.validators import InputRequired 

from flask_wtf.file import FileField, FileAllowed, FileRequired

class ProductoForm(FlaskForm):
    opciones_categoria = [('', 'Seleccione categoría'), ('categoria1', 'Categoría 1'), ('categoria2', 'Categoría 2')]
    productoCategoria = SelectField('Categoría del producto', choices=opciones_categoria, validators=[InputRequired(message="Ingrese una categoría")])

    productoNombre = StringField('Nombre del producto', validators=[InputRequired(message="Ingrese nombre del producto")])
    productoDescripcion = TextAreaField('Descripción del producto', validators=[InputRequired(message="Ingrese una descripción")])
    productoImagen = FileField('Imagen del producto', validators=[
     
    ] )
    productoPrecio = StringField('Precio de venta', validators=[InputRequired(message="El precio no debe ir vacio")])

    productoStock = IntegerField('Stock', validators=[InputRequired(message="El stock no debe ir vacio")])