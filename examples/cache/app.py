import os
from flask import Flask, url_for, redirect, request, flash, render_template
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')  # Load secret key from environment variable
app.config['CACHE_TYPE'] = 'simple'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

cache = Cache(app)
toolbar = DebugToolbarExtension(app)

# Use parameterized queries to build SQL queries with user input
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