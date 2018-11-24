""" This module defines and sets the environment  """
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CRSF_ENABLED = True
    SECRET_KEY = '\x84\x16\xdb\xc2`\xf3@K\x81\x9c5\xbf\x1b)\tg\xce),b\x930(' 
    DATABASE_URI=os.environ['DATABASE_URI']  

class ProductionConfig(Config):
    """ This class sets the PRODUCTION environment variables """
    DEBUG = False
    DATABASE_NAME = 'defb17uf0pchi7'
    DB_USER ='fvheujobpptfos'
    DB_HOST='ec2-23-21-201-12.compute-1.amazonaws.com'
    DB_PASSWORD='5b404bb6671defebfed8c63f4df98f14594660f26675b1c225ddc97b51c5cee3'
    

class StagingConfig(Config):
    DEVELOPMENT =True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    DATABASE_NAME=sendit
    DB_USER ='postgres'
    DB_HOST='localhost
    DB_PASSWORD=''

class TestingConfig(Config):
    """ This class sets the TEST environment variables """
    TESTING = True
    DATABASE_NAME=test_db
    DB_USER ='postgres'
    DB_HOST='localhost'
    DB_PASSWORD=''



