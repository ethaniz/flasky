# -*- coding:utf-8 -*-
#from flask import Flask, render_template, session, redirect, url_for, flash
#from flask.ext.bootstrap import Bootstrap
#from flask.ext.wtf import Form
#from wtforms import StringField, SubmitField
#from wtforms.validators import Required
#from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.script import Manager, Shell
#from flask.ext.migrate import Migrate, MigrateCommand
#from flask.ext.mail import Mail, Message
#from celery import Celery

#import os

#basedir = os.path.abspath(os.path.dirname(__file__))

#app = Flask(__name__)
#app.config['debug'] = True
#app.config['SECRET_KEY'] = 'hard to guess string'
#app.config['SQLALCHEMY_DATABASE_URI'] =\
#    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#app.config['MAIL_SERVER'] = 'smtp.163.com'
#app.config['MAIL_PORT'] = 25
#app.config['MAIL_USE_TLS'] = False
#app.config['MAIL_USE_SSL'] = False
#app.config['MAIL_USERNAME'] = 'nightfalldust'
#app.config['MAIL_PASSWORD'] = '19840412'
#app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
#app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <nightfalldust@163.com>'
#app.config['FLASKY_ADMIN'] = 'nightfalldust@163.com'

#app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
#app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

def test_email():
  msg = Message('test subject', sender='nightfalldust@163.com', recipients=['nightfalldust@163.com'])
  msg.body = 'body'
  msg.html = '<b>HTML</b> body'
  mail.send(msg)

@celery.task
def send_async_mail(msg):
  with app.app_context():
    mail.send(msg)


def send_email(to ,subject, template, **kwargs):
  print "in send_email()"
  msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, 
    sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
  #msg.body = render_template(template + '.text', **kwargs)
  #msg.html = render_template(template + '.html', **kwargs)
  msg.body = 'body'
  msg.html = '<b>HTML</b> body' 
  print "about to send mail..."
  send_async_mail.delay(msg)


#db = SQLAlchemy(app)
#bootstrap = Bootstrap(app)
#manager = Manager(app)
#
#migrate = Migrate(app, db)
#manager.add_command('db', MigrateCommand)

#mail = Mail(app)


#@app.route('/', methods=['GET', 'POST'])
#def index():
#    form = NameForm()
#    if form.validate_on_submit():
#        print "In form.submit()"
#        print "form.name.data = ", form.name.data
#        user = User.query.filter_by(username=form.name.data).first()
#        print "User = ", User
#        if user is None:
#            user = User(username = form.name.data)
#            db.session.add(user)
#            session['known'] = False
#            if app.config['FLASKY_ADMIN']:
#                flash('Sending email to {0}'.format(app.config['FLASKY_ADMIN']))
#                send_email(app.config['FLASKY_ADMIN'], 'New User', 'mail/new_user', user=user)
#        else:
#            session['known'] = True
#        session['name'] = form.name.data
#        form.name.data = ''
#        return redirect(url_for('index'))
#    return render_template('index.html', form = form, name = session.get('name'),
#                            known = session.get('known', False))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)

#@app.errorhandler(404)
#def page_not_found(e):
#    return render_template('404.html'), 404

#@app.errorhandler(500)
#def internel_server_error(e):
#    return render_template('500.html'), 500


#class NameForm(Form):
#    name = StringField('What is your name?', validators = [Required()])
#    submit = SubmitField('Submit')

#class Role(db.Model):
#    __tablename__ = 'roles'
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(64), unique=True)
#    users = db.relationship('User', backref='role')
#
#    def __repr__(self):
#        return '<Role %r>' % self.name
#
#class User(db.Model):
#    __tablename__ = 'users'
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(64), unique=True)
#    age = db.Column(db.Integer)
#    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
#
#    def __repr__(self):
#        return '<User %r>' % self.username



#def make_shell_context():
#    return dict(app=app, db=db, User=User, Role=Role)
#manager.add_command("shell", Shell(make_context=make_shell_context))


#if __name__ == '__main__':
#    manager.run()