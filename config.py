# Файл для конфигурации приложения

import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very-complex-set-of-words-for-the-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('C:\SomeStaff\Flask-Blog\/app.db') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 25
