from flask import render_template
from . import inicio_bp

@inicio_bp.route('/home')
@inicio_bp.route('/')
def inicio():
    """Pagina de inicio"""
    return render_template('home.html')
