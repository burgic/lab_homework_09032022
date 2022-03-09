from flask import render_template
from app import app
from models.order_list import order_list

@app.route('/orders')
def index():
    return render_template('index.html', title='WineTopia', order_list=order_list)

@app.route('/order/<index>')
def get_order(index):
    order = order_list[int(index)]
    return render_template('order.html', title=index, order=order)