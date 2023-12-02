from flask import Blueprint

carrito = Blueprint('carritoCompras', __name__, template_folder='templates')

from . import routes
