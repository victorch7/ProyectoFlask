from app import create_app
from flask import render_template

app = create_app()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)
