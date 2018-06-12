from flask import Flask, render_template, redirect, url_for
from flask_sse import sse

app = Flask(__name__)
app.config['REDIS_URL'] = 'redis://localhost'

app.register_blueprint(sse, url_prefix='/stream')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/broadcast')
def broadcast():
    sse.publish({'message': 'hi'}, type='greeting')
    return redirect(url_for('index'))


@app.route('/hello/<username>')
def hello(username):
    sse.publish({'message': 'hi'}, channel='%s' % username)
    return redirect(url_for('index'))


@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)



