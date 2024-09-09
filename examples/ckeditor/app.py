import os

from flask_ckeditor import CKEditor
from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_ckeditor import CKEditorField
from bleach import clean

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')
ckeditor = CKEditor(app)

def clean_html(html):
    allowed_tags = ['a', 'abbr', 'b', 'br', 'blockquote', 'code',
                    'del', 'div', 'em', 'img', 'p', 'pre', 'strong',
                    'span', 'ul', 'li', 'ol']
    allowed_attributes = ['src', 'title', 'alt', 'href', 'class']
    return clean(html, tags=allowed_tags, attributes=allowed_attributes)


class ArticleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 50)])
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField('Publish')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ArticleForm()
    if form.validate_on_submit():
        title = form.title.data
        body = clean_html(form.body.data)
        flash('Your article is published!')
        return render_template('article.html', title=title, body=body)
    return render_template('index.html', form=form)
