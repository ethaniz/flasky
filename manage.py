#-*- coding:utf-8 -*-
import os
from app import create_app, db, mail
from app.models import User, Role, Post
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand


app = create_app('default')
print "app's id = ", id(app)

manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Post=Post)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def test():
  """Run the unit tests."""
  import unittest
  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)


def make_celery():
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

if __name__ == '__main__':
    manager.run()