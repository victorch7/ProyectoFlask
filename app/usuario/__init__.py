from flask import Blueprint

usuario = Blueprint('usuario', __name__, template_folder='templates', static_folder='static/css')

from . import routes