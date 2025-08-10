import os
import uuid
from flask import Flask, render_template, flash, redirect, url_for, request, send_from_directory, session
from flask_ckeditor import CKEditor, upload_success, upload_fail
from flask_dropzone import Dropzone
from flask_wtf.csrf import validate_csrf
from wtforms import ValidationError
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')

# Custom config
app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')

if not os.path.exists(app.config['UPLOAD_PATH']):
    os.makedirs(app.config['UPLOAD_PATH'])

app.config['ALLOWED_EXTENSIONS'] = ['png', 'jpg', 'jpeg', 'gif']

# Flask config
# set request body's max length
# app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024  # 3Mb

# Flask-CKEditor config
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_FILE_UPLOADER'] = 'upload_for_ckeditor'

# Flask-Dropzone config
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image'
app.config['DROPZONE_MAX_FILE_SIZE'] = 3
app.config['DROPZONE_MAX_FILES'] = 30

ckeditor = CKEditor(app)
dropzone = Dropzone(app)

class LoginForm(FlaskForm):
    username = InputRequired()

class FortyTwoForm(FlaskForm):
    pass

class NewPostForm(FlaskForm):
    save = InputRequired()
    publish = InputRequired()

class UploadForm(FlaskForm):
    photo = InputRequired()

class MultiUploadForm(FlaskForm):
    photo = InputRequired()

class SigninForm(FlaskForm):
    username = InputRequired()
    submit1 = InputRequired()

class RegisterForm(FlaskForm):
    username = InputRequired()
    submit2 = InputRequired()

class RichTextForm(FlaskForm):
    title = InputRequired()
    body = InputRequired()

class SigninForm2(FlaskForm):
    username = InputRequired()
    submit = InputRequired()

class RegisterForm2(FlaskForm):
    username = InputRequired()
    submit = InputRequired()

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/html', methods=['GET', 'POST'])
def html():
    form = LoginForm()
    if request.method == 'POST':
        username = request.form.get('username')
        flash('Welcome home, %s!' % username)
        return redirect(url_for('index'))
    return render_template('pure_html.html')

# ... (rest of the routes remain the same)

# handle image upload for ckeditor
@app.route('/upload-ck', methods=['POST'])
def upload_for_ckeditor():
    f = request.files.get('upload')
    if not allowed_file(f.filename):
        return upload_fail('Image only!')
    filename = secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    url = url_for('get_file', filename=filename)
    return upload_success(url, filename)

if __name__ == '__main__':
    app.run(debug=True)