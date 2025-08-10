import os
import uuid
from pathlib import Path
from flask import Flask, render_template, flash, session, redirect, url_for, send_from_directory
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed, FileSize
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['UPLOAD_PATH'] = Path(app.root_path) / 'uploads'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')  # Load secret key from environment variable

# Initialize SQLAlchemy and Bcrypt
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class UploadPhotoForm(FlaskForm):
    photo = FileField('Upload Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'jpeg', 'png', 'gif']),
        FileSize(5 * 1024 * 1024)
    ])
    submit = SubmitField()

def random_filename(origin_filename):
    ext = Path(origin_filename).suffix
    new_filename = f'{uuid.uuid4().hex}{ext}'
    return new_filename

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/photos/<path:filename>')
def get_photo(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadPhotoForm()
    if form.validate_on_submit():
        photo = form.photo.data
        filename = random_filename(photo.filename)
        photo.save(app.config['UPLOAD_PATH'] / filename)
        flash('Upload success.')
        session['photos'] = [filename]
        return redirect(url_for('index'))
    return render_template('upload.html', form=form)

# Example of using parameterized query to prevent SQL injection
@app.route('/example')
def example():
    username = 'example_user'
    query = db.session.query(User).filter_by(username=username)
    results = query.all()
    return render_template('example.html', results=results)