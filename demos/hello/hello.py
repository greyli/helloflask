# -*- coding: utf-8 -*-
"""
    :author: 林旺
    :url: None
    :copyright: © 2019 SangeWang
"""

import click

#从flask包中导入Flask类，这个类表示一个Flask程序

from flask import Flask 
#实例化这个类，就可以得到程序实例
app = Flask(__name__)


# the minimal Flask application
#最小的flask程序 => hello world
#在需要启动的机器上直接 127.0.0.1:PORT 可以直接访问 / 代表跟路径
@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


# bind multiple URL for one view function
@app.route('/hi') #=> 127.0.0.1:PORT/hi
@app.route('/hello') #=> 127.0.0.1:PORT/hello
def say_hello():
    return '<h1>Hello, Flask!</h1>'ls


# dynamic route, URL variable default
# 设置动态路由，加入一些参数进行处理
@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name


# custom flask cli command
@app.cli.command()
def hello():
    """Just say hello."""
    click.echo('Hello, Human!')

