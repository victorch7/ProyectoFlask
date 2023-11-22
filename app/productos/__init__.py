from flask import Blueprint

prod_bp = Blueprint('productos', __name__, template_folder='templates')

from . import routes
