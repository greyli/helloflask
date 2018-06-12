from app import app
from waitress import serve

serve(app, listen='127.0.0.1:5000')
