import click
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello, world!</h1>'


@app.route('/ping')
@app.route('/pong')
def hello_flask():
    return '<h1>Hello, Flask!</h1>'


@app.route('/greet', defaults={'name': 'Programmer'})  # 为 name 变量设定一个默认值
@app.route('/greet/<name>')
def greet(name):
    return f'<h1>Hello, {name}!</h1>'


# 命令函数 $ flask hello
@app.cli.command()
def hello():
    """Just say hello."""
    click.echo('Hello, Human!')
