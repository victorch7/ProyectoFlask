from flask import redirect, render_template, url_for, request, flash, current_app


# blueprints
from . import auth_admin

# formulario
from .forms import LoginForm

# modelos
from .models.ModelUser import ModelUser

# entidades
from .models.entities.User import User
from flask_login import current_user, login_user, login_manager, logout_user, login_required

#logs
import logging

@auth_admin.route('/admin', methods=['GET', 'POST'])
def loginAdmin():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User('', request.form.get('usuario'), request.form.get('contrasena'), '', '', '', '','')
            logged_user = ModelUser.login(user)
            
            if logged_user is not None:
                if logged_user.contrasena:
                    login_user(logged_user)
                    logging.info(f"Usuario {current_user.usuario} ha iniciado sesión")
                    return redirect(url_for('dashboard.dashboard'))
                else:
                    flash('Contraseña incorrecta')
            else:
                flash('Usuario no encontrado')
                
    return render_template('loginadmin.html', form=form)

@auth_admin.route('/adminlogout')
def logoutAdmin():
    logout_user()
    return redirect(url_for('auth_admin.loginAdmin'))

