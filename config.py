import os

class Config:
    FLASK_APP = os.getenv('FLASK_APP')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

config = {
    'default': Config
}


# class Config:
# SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
# MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
# MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
# MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
# ['true', 'on', '1']
# MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
# MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
# FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
# FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
# FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
# SQLALCHEMY_TRACK_MODIFICATIONS = False

#tem que comentar tudo




# class DevelopmentConfig(Config):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
#     'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

# class TestingConfig(Config):
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
#     'sqlite://'

# class ProductionConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#     'sqlite:///' + os.path.join(basedir, 'data.sqlite')

# config = {
# 'development': DevelopmentConfig,
# 'testing': TestingConfig,
# 'production': ProductionConfig,
# 'default': DevelopmentConfig
# }
