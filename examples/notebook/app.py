import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import click
from flask import Flask, redirect, url_for, render_template, flash, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, String, Text, MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length
from faker import Faker

SQLITE_PREFIX = 'sqlite:///' if sys.platform.startswith('win') else 'sqlite:////'
SQLITE_PATH = Path(__file__).resolve().parent / 'data.db'


class Base(DeclarativeBase):
    metadata = MetaData(naming_convention={
        'ix': 'ix_%(column_0_label)s',
        'uq': 'uq_%(table_name)s_%(column_0_name)s',
        'ck': 'ck_%(table_name)s_%(constraint_name)s',
        'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
        'pk': 'pk_%(table_name)s'
    })


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret string')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', SQLITE_PREFIX + str(SQLITE_PATH))
db = SQLAlchemy(app, model_class=Base)


# models
class Note(db.Model):
    __tablename__ = 'note'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    body: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[Optional[datetime]] = mapped_column(onupdate=datetime.now)

    def __repr__(self):
        return f'<Note {self.id}: {self.title}>'  # pragma: no cover


# callbacks
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Note=Note)  # pragma: no cover


# commands
@app.cli.command('init')
@click.option('--drop-table', is_flag=True, help='Re-create the tables.')
def init_command(drop_table):
    """Initialize the application."""
    if drop_table:
        click.confirm(
            'This operation will delete the tables, do you want to continue?',
            abort=True
        )
        db.drop_all()
        click.echo('Dropped tables.')
    db.create_all()
    click.echo('Initialized.')


@app.cli.command('lorem')
@click.option('--count', default=20, help='Quantity of notes, default is 20.')
def lorem_command(count):
    """Generate fake data."""
    db.drop_all()
    db.create_all()

    fake = Faker()

    for _ in range(count):
        note = Note(
            title=fake.sentence(5),
            body=fake.text(200),
            created_at=fake.date_time_this_year(),
        )
        db.session.add(note)

    db.session.commit()
    click.echo(f'Created {count} notes.')


# forms
class NoteForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 50)])
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField()


class DeleteNoteForm(FlaskForm):
    submit = SubmitField('Delete')


# views
@app.route('/')
def index():
    notes = db.session.scalars(select(Note)).all()
    delete_form = DeleteNoteForm()
    return render_template('index.html', notes=notes, delete_form=delete_form)


@app.route('/new', methods=['GET', 'POST'])
def new_note():
    form = NoteForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        note = Note(title=title, body=body)
        db.session.add(note)
        db.session.commit()
        flash('Note saved.')
        return redirect(url_for('index'))
    return render_template('new_note.html', form=form)


@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    form = NoteForm()
    note = db.session.get(Note, note_id)
    if form.validate_on_submit():
        note.title = form.title.data
        note.body = form.body.data
        db.session.commit()
        flash('Note updated.')
        return redirect(url_for('index'))
    if request.method == 'GET':
        # pre-fill form
        form.title.data = note.title
        form.body.data = note.body
    return render_template('edit_note.html', form=form)


@app.route('/delete/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    # note = db.session.get(Note, note_id)
    # db.session.delete(note)
    # db.session.commit()
    # flash('Note deleted.')
    # return redirect(url_for('index'))
    form = DeleteNoteForm()
    if form.validate_on_submit():
        note = db.session.get(Note, note_id)  # 获取对应记录
        db.session.delete(note)  # 删除记录
        db.session.commit()  # 提交修改
        flash('Note deleted.')
    else:
        flash('Delete failed, please try again.')
    return redirect(url_for('index'))
