from flask import Flask, render_template, send_from_directory,redirect,url_for
import os
from config import Config
from .inicio.routes import inicio_bp
from .acercade.routes import acercade_bp
from  .authentication.routes import authentication_bp
from  .productos.routes import prod_bp

app = Flask(__name__, static_folder='static', static_url_path='/static')

def favicon():
    return send_from_directory(os.path.join(app.root_path,'app/static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

def page_not_found(e):
    return render_template('error404.html'), 404


def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Registrar Blueprints
    app.register_blueprint(inicio_bp)
    app.register_blueprint(acercade_bp)
    app.register_blueprint(authentication_bp)
    app.register_blueprint(prod_bp)
    

    #Registro manejo de erroes
    app.register_error_handler(404, page_not_found)
    return app