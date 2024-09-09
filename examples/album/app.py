import os
import uuid
from pathlib import Path

from flask import Flask, render_template, flash, session, redirect, url_for, send_from_directory
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed, FileSize

app = Flask(__name__)
app.config['UPLOAD_PATH'] = Path(app.root_path) / 'uploads'
app.secret_key = os.getenv('SECRET_KEY', 'secret string')


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
