# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li
    :license: MIT, see LICENSE for more details.
"""
import time

from flask import Flask, url_for, redirect, request, flash, render_template
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

app.config['SECRET_KEY'] = 'dev key'

app.config['CACHE_TYPE'] = 'simple'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

cache = Cache(app)
toolbar = DebugToolbarExtension(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/foo')
def foo():
    time.sleep(1)
    return render_template('foo.html')


@app.route('/bar')
@cache.cached(timeout=10 * 60)
def bar():
    time.sleep(1)
    return render_template('bar.html')


@app.route('/baz')
@cache.cached(timeout=60 * 60)
def baz():
    time.sleep(1)
    return render_template('baz.html')


@app.route('/qux')
@cache.cached(query_string=True)
def qux():
    time.sleep(1)
    page = request.args.get('page', 1)
    return render_template('qux.html', page=page)


@app.route('/update/bar')
def update_bar():
    cache.delete('view/%s' % url_for('bar'))
    flash('Cached data for bar have been deleted.')
    return redirect(url_for('index'))


@app.route('/update/baz')
def update_baz():
    cache.delete('view/%s' % url_for('baz'))
    flash('Cached data for baz have been deleted.')
    return redirect(url_for('index'))


@app.route('/update/all')
def update_all():
    cache.clear()
    flash('All cached data deleted.')
    return redirect(url_for('index'))


# cache other function
@cache.cached(key_prefix='add')
def add(a, b):
    time.sleep(2)
    return a + b


# cache memorize (with argument)
@cache.memoize()
def add_pro(a, b):
    time.sleep(2)
    return a + b


def del_add_cache():
    cache.delete('add')


# delete memorized cache
def del_pro_cache():
    cache.delete_memoized(add_pro)
