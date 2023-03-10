from jinja2.utils import generate_lorem_ipsum
from flask import Flask, jsonify, render_template

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')


@app.route('/')
def index():
    post_body = generate_lorem_ipsum(n=3)
    return render_template('index.html', post_body=post_body)


@app.route('/more')
def load_post():
    return generate_lorem_ipsum(n=3)
