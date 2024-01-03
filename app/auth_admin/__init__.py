from flask import Blueprint

auth_admin = Blueprint('auth_admin', __name__, template_folder='templates', static_folder='static/css')

from . import routes