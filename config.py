import os


class Config:
    '''
    General configuration parent class
    '''

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lorddoyo:adanog@localhost/pitc'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("johnkojo7777@gmail.com")
    MAIL_PASSWORD = os.environ.get("soliderclone")
    SUBJECT_PREFIX = 'PITCH'
    SENDER_EMAIL = ('johnkojo7777@gmail.com')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    # simplemde confirgurations
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lorddoyo:adanog@localhost/pitc_test'


class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config : the parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lorddoyo:adanog@localhost/pitc'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test':TestConfig
}
