import os
import random, string

class Config(object):
    CSRF_ENABLED = True
    SECRET = ':<U4[x0G{7zDk%,b/AXI|#?2;SWh#1G]jaffjb*R&<wEo0tjBq'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)
    DB_USER = 'solid'
    DB_PWD = 'solid'
    DB_HOST = '172.17.0.2'
    DB_NAME = 'solid'
    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s/%s' % (DB_USER, DB_PWD, DB_HOST, DB_NAME)

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost' # Aqui geralmente é um IP de um servidor na nuvem e não o endereço da máquina local
    PORT_HOST = 5000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    IP_HOST = 'localhost' # Aqui geralmente é um IP de um servidor na nuvem e não o endereço da máquina local
    PORT_HOST = 8080

app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig()
}

app_active = os.getenv('FLASK_ENV')