from flask import render_template
from . import carrito

@carrito.route('/carrito-list')
def listProducts():
    return render_template("carrito.html")





