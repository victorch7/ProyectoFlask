from flask import render_template
from . import acercade_bp

@acercade_bp.route('/contacto')
def index():
    return render_template('contacto.html')