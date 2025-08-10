import os

if 'SECRET_KEY' in os.environ:
    app.secret_key = os.environ['SECRET_KEY']
else:
    app.secret_key = os.urandom(24)