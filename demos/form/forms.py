# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li
    :license: MIT, see LICENSE for more details.
"""
from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, IntegerField, \
    TextAreaField, SubmitField, MultipleFileField
from wtforms.validators import DataRequired, Length, ValidationError, Email


# 4.3.1 basic form example
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')


# custom validator
class FortyTwoForm(FlaskForm):
    answer = IntegerField('The Number')
    submit = SubmitField()

    def validate_answer(form, field):
        if field.data != 42:
            raise ValidationError('Must be 42.')


# upload form
class UploadForm(FlaskForm):
    photo = FileField('Upload Image', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    submit = SubmitField()


# multiple files upload form
class MultiUploadForm(FlaskForm):
    photo = MultipleFileField('Upload Image', validators=[DataRequired()])
    submit = SubmitField()


# multiple submit button
class NewPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 50)])
    body = TextAreaField('Body', validators=[DataRequired()])
    save = SubmitField('Save')
    publish = SubmitField('Publish')


class SigninForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    submit1 = SubmitField('Sign in')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 254)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    submit2 = SubmitField('Register')


class SigninForm2(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 24)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    submit = SubmitField()


class RegisterForm2(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 24)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 254)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    submit = SubmitField()


# CKEditor Form
class RichTextForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 50)])
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField('Publish')
