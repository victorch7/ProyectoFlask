from flask import Flask,render_template,redirect,url_for
from flask_mysqldb import MySQL
#flask-login
from flask_login import LoginManager, login_user, logout_user, login_required

#formulario
from flask_wtf.csrf import CSRFProtect

# Models:
from .auth.models.ModelClient import ModelClient

#logs
import logging

 # Configurar el sistema de logs
logging.basicConfig(filename='app.log',filemode='a' ,level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def page_not_found(e):
        return render_template('error404.html'), 404

def status_401(error):
        return redirect(url_for('auth.login'))
    
db = MySQL()

def create_app():
    
    app = Flask(__name__, template_folder='templates')
    app.config.from_pyfile('config/configuracion.cfg')
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'kliche'    
    
    db.init_app(app)
    
    #Cargar usuario y sesión
    login_manager = LoginManager(app)

    @login_manager.user_loader
    def load_client(id):
        return ModelClient.get_by_id(db,id)
    
    #csrf
    csrf = CSRFProtect()
    csrf.init_app(app)
    
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
    
    #Errores
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(401, status_401)
    
    app.conexion = conexion.conectar
    return app
