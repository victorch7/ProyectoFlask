from flask import Flask, render_template, redirect, url_for

# Configuración
from .config import config

# Flask-login
from flask_login import LoginManager, login_user, logout_user, login_required

# Formulario
from flask_wtf.csrf import CSRFProtect

# Models
from .auth.models.ModelClient import ModelClient

# Logs
import logging

# Registrar blueprints
from .auth import auth
from .inicio import inicio
from .acercade import acercade_bp
from .carrito import carrito

#admin blueprints
from .auth_admin import auth_admin
from .dashboard import dashboard
from .categoria import categoria
from .producto import producto
from .cliente import cliente
from .usuario import usuario
from .venta import venta

#flask-mails
from flask_mail import Mail

# Models:
from .auth_admin.models.ModelUser import ModelUser

# Configurar el sistema de logs
logging.basicConfig(filename='app.log', filemode='a', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def page_not_found(e):
    return render_template('error404.html'), 404

def status_401(error):
    return redirect(url_for('error500.html'))

def status_500(error):
    return render_template('error500.html'), 500

def create_app():
    app = Flask(__name__, template_folder='templates')


    # CSRF
    csrf = CSRFProtect()
    csrf.init_app(app)

    # Cargar usuario y sesión
    login_manager = LoginManager(app)

    @login_manager.user_loader
    def load_client(id):
        return ModelClient.get_by_id(id)
    
    @login_manager.user_loader
    def load_user(id):
        return ModelUser.get_by_id(id)
    
    #registrar blueprints
    app.register_blueprint(auth)
    app.register_blueprint(inicio)
    app.register_blueprint(acercade_bp)
    app.register_blueprint(carrito)

    #registrar blueprints admin
    app.register_blueprint(auth_admin)
    app.register_blueprint(categoria)
    app.register_blueprint(producto)
    app.register_blueprint(cliente)
    app.register_blueprint(usuario)
    app.register_blueprint(venta)
    app.register_blueprint(dashboard)
    

    # Configuración
    app.config.from_object(config['development'])
    
    # Inicializar Flask-Mail
    mail = Mail(app)
    app.mail = mail

    # Errores
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(401, status_401)
    app.register_error_handler(500, status_500)

    return app
