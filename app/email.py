#-*- coding:utf-8 -*-
#from celery import Celery
from threading import Thread
from flask.ext.mail import Mail, Message
from flask import current_app
from . import mail

#def make_celery(app):
#    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
#    celery.conf.update(app.config)
#    TaskBase = celery.Task
#    class ContextTask(TaskBase):
#        abstract = True
#        def __call__(self, *args, **kwargs):
#            with app.app_context():
#                return TaskBase.__call__(self, *args, **kwargs)
#    celery.Task = ContextTask
#    return celery
#
#celery = make_celery(flask_app)

#print "Now importing email..."
#celery = Celery(__name__, broker='redis://localhost:6379/0')

#@celery.task
#def send_async_mail(msg):
#  app = current_app._get_current_object()
#  app_ctx = app.app_context()
#  app_ctx.push()
#  #with app.app_context():
#  mail.send(msg)
#  app_ctx.pop()
#  print "send async mail...%s" % (msg.body)

def send_async_mail(app, msg):
  with app.app_context():
    mail.send(msg)

def send_email(to ,subject, template, **kwargs):
  app = current_app._get_current_object()
  #celery.conf.update(app.config)
  print "in send_email()", app
  msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, 
    sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
  #msg.body = render_template(template + '.text', **kwargs)
  #msg.html = render_template(template + '.html', **kwargs)
  msg.body = 'body'
  msg.html = '<b>HTML</b> body' 
  print "about to send mail..."
  #ctx = app.app_context()
  #send_async_mail.delay(app, msg)
  thr = Thread(target=send_async_mail, args=[app, msg])
  thr.start()
  return thr