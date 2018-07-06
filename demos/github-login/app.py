# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li
    :license: MIT, see LICENSE for more details.
"""
import os
import sys

import click
from flask import Flask, request, g, session, redirect, url_for, render_template, jsonify, flash
from flask_github import GitHub
from flask_sqlalchemy import SQLAlchemy

# sqlite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret string')
# Flask-SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', prefix + os.path.join(app.root_path, 'data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# GitHub-Flask
app.config['GITHUB_CLIENT_ID'] = '723b66409490cad030f0'
app.config['GITHUB_CLIENT_SECRET'] = 'bb60af3c5a4d8c98b8442314a7cff32dcefe0660'

db = SQLAlchemy(app)
github = GitHub(app)


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    access_token = db.Column(db.String(200))


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])


@app.route('/')
def index():
    if g.user:
        is_login = True
        response = github.get('user')
        avatar = response['avatar_url']
        username = response['name']
        url = response['html_url']
        return render_template('index.html', is_login=is_login, avatar=avatar, username=username, url=url)
    is_login = False
    return render_template('index.html', is_login=is_login)


@app.route('/star/helloflask')
def star():
    github.put('user/starred/greyli/helloflask', headers={'Content-Length': '0'})
    flash('Star success.')
    return redirect(url_for('index'))


@github.access_token_getter
def token_getter():
    user = g.user
    if user is not None:
        return user.access_token


@app.route('/callback/github')
@github.authorized_handler
def authorized(access_token):
    if access_token is None:
        flash('Login failed.')
        return redirect(url_for('index'))

    response = github.get('user', access_token=access_token)
    username = response['login']  # get username
    user = User.query.filter_by(username=username).first()
    if user is None:
        user = User(username=username, access_token=access_token)
        db.session.add(user)
    user.access_token = access_token  # update access token
    db.session.commit()
    flash('Login success.')
    # log the user in
    # if you use flask-login, just call login_user() here.
    session['user_id'] = user.id
    return redirect(url_for('index'))


@app.route('/login')
def login():
    if session.get('user_id', None) is None:
        return github.authorize(scope='repo')
    flash('Already logged in.')
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Goodbye.')
    return redirect(url_for('index'))


@app.route('/user')
def get_user():
    return jsonify(github.get('user'))
