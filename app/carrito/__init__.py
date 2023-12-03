from flask import Blueprint

carrito = Blueprint('carrito', __name__, template_folder='templates')

from . import routes
