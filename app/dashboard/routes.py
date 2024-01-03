from flask import render_template
from . import dashboard


from flask_login import login_user, login_manager, logout_user, login_required


@dashboard.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

