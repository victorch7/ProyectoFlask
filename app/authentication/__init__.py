from flask import Blueprint

authentication_bp = Blueprint('authentication', __name__, template_folder='templates')

from . import routes

# from flask_mysqldb import MySQL

# mysql = MySQL()

# @authentication_bp.record_once
# def on_load(state):
#     mysql.init_app(state.app)
#     state.app.config['mysql'] = mysql

#     with state.app.app_context():
#         authentication_bp.db_connection = mysql.connection
#         from . import routes