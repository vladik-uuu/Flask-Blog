# Файл для конфигурации приложения

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very-complex-set-of-words-for-the-key'
