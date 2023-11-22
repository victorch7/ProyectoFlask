from flask import render_template
from . import authentication_bp


@authentication_bp.route("/login", methods=["GET","POST"])
def login():
        return render_template("login.html")
  
@authentication_bp.route("/register", methods=["GET","POST"])
def register(): 
      return render_template('registro.html')