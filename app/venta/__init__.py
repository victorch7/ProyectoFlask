from flask import Blueprint, render_template

venta = Blueprint('venta', __name__, template_folder='templates', static_folder='static/css')

from . import routes
