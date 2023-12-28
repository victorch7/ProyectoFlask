from flask_wtf import FlaskForm
from wtforms import IntegerField,  SubmitField
from wtforms.validators import InputRequired, DataRequired, Email, Length,Regexp, NumberRange

class AgregarProductoForm(FlaskForm):
    cantidad = IntegerField('Cantidad', validators=[
        InputRequired(message="La cantidad es obligatoria."),
        NumberRange(min=1, message="La cantidad debe ser al menos 1."),
    ], default=1)
    submit = SubmitField('Agregar al carrito')