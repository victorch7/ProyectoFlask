from flask import Blueprint

inicio_bp = Blueprint('inicio', __name__, template_folder='templates')

from . import routes
