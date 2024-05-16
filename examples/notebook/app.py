import os
import sys
from datetime import datetime

import click
from flask import Flask, redirect, url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, Column, Integer, String, Text, DateTime
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length
from faker import Faker


# SQLite URI compatible
prefix = 'sqlite:///' if sys.platform.startswith('win') else 'sqlite:////'


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret string')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', prefix + os.path.join(app.root_path, 'data.db')
)
db = SQLAlchemy(app)


# Models
class Note(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    body = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)

    def __repr__(self):
        return f'<Note {self.id}: {self.title}>'  # pragma: no cover


# Callbacks
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Note=Note)  # pragma: no cover


# Commands
@app.cli.command()
@click.option('--drop-table', is_flag=True, help='Re-create the tables.')
def init(drop_table):
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


@app.cli.command()
@click.option('--count', default=20, help='Quantity of notes, default is 20.')
def fake(count):
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


# Forms
class NoteForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 50)])
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField()


# Views
@app.route('/')
def index():
    notes = db.session.execute(select(Note)).scalars().all()
    return render_template('index.html', notes=notes)


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
    # Pre-fill form
    form.title.data = note.title
    form.body.data = note.body
    return render_template('edit_note.html', form=form)


@app.route('/delete/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    note = db.session.get(Note, note_id)
    db.session.delete(note)
    db.session.commit()
    flash('Note deleted.')
    return redirect(url_for('index'))
