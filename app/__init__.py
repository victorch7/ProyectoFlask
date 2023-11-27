from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()

def create_app():
    app = Flask(__name__, template_folder='templates')

    app.config.from_pyfile('config/configuracion.cfg')
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'kliche'
    
    mysql.init_app(app)
    
    app.config['mysql'] = mysql

    # Registrar Blueprints
    from .inicio import inicio_bp
    from .acercade import acercade_bp
    from .authentication import authentication_bp
    from .productos import prod_bp

    app.register_blueprint(inicio_bp)
    app.register_blueprint(acercade_bp)
    app.register_blueprint(authentication_bp)
    app.register_blueprint(prod_bp)
    
    return app
