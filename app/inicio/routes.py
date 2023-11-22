from flask import render_template,redirect,url_for
from . import inicio_bp

@inicio_bp.route('/')
def inicio():
    return render_template('home.html')

@inicio_bp.route('/home')
def home():
    return redirect(url_for('inicio'))  
