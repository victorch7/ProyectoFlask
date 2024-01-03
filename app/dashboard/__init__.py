from flask import Blueprint, render_template

dashboard = Blueprint('dashboard', __name__, template_folder='templates')

from . import routes