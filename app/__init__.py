# -*- coding:utf-8 -*-
from flask import Flask, render_template, session, redirect, url_for, flash
from flask.ext.bootstrap import Bootstrap
#from flask.ext.wtf import Form
#from wtforms import StringField, SubmitField
#from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.script import Manager, Shell
#from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.mail import Mail
from flask.ext.login import LoginManager
from celery import Celery
from config import config
from flask_admin import Admin
from flask_moment import Moment

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
admin = Admin()
admin.template_mode = 'bootstrap3'
moment = Moment()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    admin.init_app(app)

    moment.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

    return app




#celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
#celery.conf.update(app.config)
