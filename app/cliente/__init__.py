from flask import Blueprint, render_template

cliente = Blueprint('cliente', __name__, template_folder='templates', static_folder='static/css')

from . import routes