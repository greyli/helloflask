from jinja2.utils import generate_lorem_ipsum
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    post_body = generate_lorem_ipsum(n=3)
    return render_template('index.html', post_body=post_body)


@app.route('/more')
def more():
    return generate_lorem_ipsum(n=3)
