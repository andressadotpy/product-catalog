import os
basedir = os.path.abspath(os.path.dirname(__file__))



class Config:
    SECRET_KEY = (os.environ.get('SECRET_KEY') or '02a9e795e3b4413a876e78bb9b54dc74')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLACHEMY_DATABASE_URI = (os.environ.get('DEV_DATABASE_URL') or
                            'sqlite:///' + os.path.join(basedir, 'dev.db'))
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (os.environ.get('TEST_DATABASE_URL') or
                            'sqlite:///' + os.path.join(basedir, 'testing.db'))


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
