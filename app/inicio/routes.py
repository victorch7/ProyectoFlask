from flask import render_template
from . import inicio

@inicio.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@inicio.route('/home')
@inicio.route('/')
def inicio():
    """Pagina de inicio"""
    return render_template('home.html')
