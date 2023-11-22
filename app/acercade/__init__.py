from flask import Blueprint

acercade_bp = Blueprint('acercade', __name__, template_folder='templates')

from . import routes