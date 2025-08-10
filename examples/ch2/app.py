from sqlalchemy import text

@app.route('/')
@app.route('/hello')
def hello():
    name = request.args.get('name')
    query = text("SELECT * FROM users WHERE name = :name")
    result = db.session.execute(query, {'name': name})
    response = f'<h1>Hello, {result.fetchone()[0]}!</h1>'
    # ...