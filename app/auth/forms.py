#-*- coding:utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(Form):
  email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
  password = PasswordField('Password', validators=[Required()])
  remember_me = BooleanField('Keep me login in')
  submit = SubmitField('Log in')

class RegistrationForm(Form):
  email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
  username = StringField('Username', validators=[Required(), Length(1, 64), 
    Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Username must have only letters, numbers. dots or underlines')])
  password = PasswordField('Password', validators=[Required(), EqualTo('password2', message='Password must match.')])
  password2 = PasswordField('Comfirm password', validators=[Required()])  
  ubmit = SubmitField('Register')

  def validate_email(self, field):
    if User.query.filter_by(email = field.data).first():
      raise ValidationError('Email already registered!')

  def validate_username(self, field):
    if User.query.filter_by(username = field.data).first():
      raise ValidationError('Username already registered!')     