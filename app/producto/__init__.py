from flask import Blueprint, render_template

producto = Blueprint('producto', __name__, template_folder='templates', static_folder='static/css')

from . import routes