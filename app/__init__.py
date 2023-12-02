from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='templates')

    app.config.from_pyfile('config/configuracion.cfg')

    from . import conexion
    
    # Registrar Blueprints
    from .inicio import inicio
    from .acercade import acercade_bp
    from .auth import auth
    from .carritoCompras import carrito

    app.register_blueprint(inicio)
    app.register_blueprint(acercade_bp)
    app.register_blueprint(auth)
    app.register_blueprint(carrito)
    
    app.conexion = conexion.conectar
    
    return app
