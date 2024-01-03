from flask import Blueprint, render_template

categoria = Blueprint('categoria', __name__, template_folder='templates')

from . import routes