""" This module defines and sets the environment  """
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CRSF_ENABLED = True
    SECRET_KEY = '\x84\x16\xdb\xc2`\xf3@K\x81\x9c5\xbf\x1b)\tg\xce),b\x930('   

class ProductionConfig(Config):
    """ This class sets the PRODUCTION environment variables """
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT =True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    DATABASE_NAME=test_db

class TestingConfig(Config):
    """ This class sets the TEST environment variables """
    TESTING = True
    DATABASE_NAME=test_db



class DevelopmentConfig(BaseConfig):
    """ This class sets the DEVELOPMENT environment variables """
    DEBUG = True



