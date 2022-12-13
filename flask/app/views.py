from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/ngk')
def ngk():
    from .parser import get_title
    return render_template('ngk.html', title=get_title())