# -*- coding:utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <nightfalldust@163.com>'
    FLASKY_ADMIN = 'nightfalldust@163.com'
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    FLASKY_POSTS_PER_PAGE = 10
    FLASKY_FOLLOWERS_PER_PAGE = 10
    FLASKY_FOLLOWERS_PER_PAGE = 10
    #CELERY_ACCEPT_CONTENT = ['json']
    #CELERY_TASK_SERIALIZER = 'json'

    @staticmethod
    def init_app(app):
      pass

class DevelopConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'nightfalldust'
    MAIL_PASSWORD = '19840412'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProductionConfig(Config):
    pass

config = {
    'development': DevelopConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopConfig,
}