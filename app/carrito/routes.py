from flask import render_template
from . import carrito

@carrito.route('/carrito')
def carrito():
    return render_template("carrito.html")





