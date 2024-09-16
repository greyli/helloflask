import os
import uuid
from pathlib import Path

from flask_ckeditor import CKEditor, upload_success, upload_fail
from flask import Flask, render_template, flash, request, url_for, send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_ckeditor import CKEditorField
from bleach import clean

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')
app.config['CKEDITOR_FILE_UPLOADER'] = 'upload_image'
app.config['UPLOAD_PATH'] = Path(app.root_path) / 'uploads'

ckeditor = CKEditor(app)


class ArticleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 50)])
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField('Publish')


def clean_html(html):
    allowed_tags = ['a', 'abbr', 'b', 'br', 'blockquote', 'code',
                    'del', 'div', 'em', 'img', 'p', 'pre', 'strong',
                    'span', 'ul', 'li', 'ol']
    allowed_attributes = ['src', 'title', 'alt', 'href', 'class']
    return clean(html, tags=allowed_tags, attributes=allowed_attributes)


def allowed_file(filename):
    extension = Path(filename).suffix.lower()
    return '.' in filename and extension in ['.jpg', '.gif', '.png', '.jpeg']


def random_filename(old_filename):
    ext = Path(old_filename).suffix
    new_filename = uuid.uuid4().hex + ext
    return new_filename


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ArticleForm()
    if form.validate_on_submit():
        title = form.title.data
        body = clean_html(form.body.data)
        flash('Your article is published!')
        return render_template('article.html', title=title, body=body)
    return render_template('index.html', form=form)


@app.route('/uploads/<path:filename>')
def get_image(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


@app.route('/upload', methods=['POST'])
def upload_image():
    f = request.files.get('upload')
    if not allowed_file(f.filename):
        return upload_fail('Image only!')
    filename = random_filename(f.filename)
    f.save(app.config['UPLOAD_PATH'] / filename)
    image_url = url_for('get_image', filename=filename)
    return upload_success(image_url, filename)
 