from flask import render_template
from . import prod_bp

@prod_bp.route('/lista-productos')
def listProducts():
    return render_template("product-list.html")



