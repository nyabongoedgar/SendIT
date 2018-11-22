import os
class BaseConfig():
    DEBUG = False
    SECRET_KEY = '\x84\x16\xdb\xc2`\xf3@K\x81\x9c5\xbf\x1b)\tg\xce),b\x930('
    


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
