from flask import render_template
from app import app
from models.order_list import order_list

@app.route('/orders')
def index():
    return render_template('index.html', title='WineTopia', order_list=order_list)
