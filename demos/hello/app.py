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
@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


# bind multiple URL for one view function
@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello, Flask!</h1>'


# dynamic route, URL variable default
@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name


# custom flask cli command
@app.cli.command()
def hello():
    """Just say hello."""
    click.echo('Hello, Human!')
