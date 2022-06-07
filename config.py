import os # Import variaveis de ambiente OS


class Config:  # Classe de configuração das variaveis de ambiente 
    FLASK_APP = os.getenv('FLASK_APP') # Seleciona arquivo como index/app 
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') # Importa endereço do banco de dados
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

    # Inicio configurações de e-mail
    SECRET_KEY = os.environ.get('SECRET_KEY') # SECRET_KEY foi gerado utilizando https://randomkeygen.com/
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # Termino configurações de e-mail

class DevelopmentConfig(Config): # Classe para ambiente de DESENVOLVIMENTO
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') 
    #or \ 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config): # Classe para ambiente de TESTES
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') 
    #or \c'sqlite://'

class ProductionConfig(Config): # Classe para ambiente de PRODUÇÃO
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 
    #or \'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {  # Variavel de instancia de ambientes
'development': DevelopmentConfig,
'testing': TestingConfig,
'production': ProductionConfig,
'default': DevelopmentConfig
}



