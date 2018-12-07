""" This module defines and sets the environment  """
import os
class BaseConfig():
    DEBUG = False
    SECRET_KEY = '\x84\x16\xdb\xc2`\xf3@K\x81\x9c5\xbf\x1b)\tg\xce),b\x930('
    


class TestConfig(BaseConfig):
    """ This class sets the TEST environment variables """
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False


class DevelopmentConfig(BaseConfig):
    """ This class sets the DEVELOPMENT environment variables """
    DEBUG = True

class ProductionConfig(BaseConfig):
    """ This class sets the PRODUCTION environment variables """
    DEBUG = False
