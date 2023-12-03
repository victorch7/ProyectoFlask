from flask import Flask
from flask_mysqldb import MySQL

db = MySQL()

def create_app():
    
    app = Flask(__name__, template_folder='templates')
    app.config.from_pyfile('config/configuracion.cfg')
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'kliche'    
    
    db.init_app(app)
    
    app.config['db'] = db 
    
    from . import conexion
    # Registrar Blueprints
    from .auth import auth
    from .inicio import inicio
    from .acercade import acercade_bp
    from .carrito import carrito
    
    app.register_blueprint(auth)
    app.register_blueprint(inicio)
    app.register_blueprint(acercade_bp)
    app.register_blueprint(carrito)
    
    app.conexion = conexion.conectar
    return app
