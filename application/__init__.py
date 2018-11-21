from flask import Flask, Blueprint
app = Flask(__name__)

from application.api.views import mod
app.register_blueprint(api.views.mod)

config_name = ""
if os.getenv('CONFIG_NAME') == 'testing':
    config_name = os.getenv('TESTING_CONF')
elif os.getenv('CONFIG_NAME') == 'develop':
	config_name = os.getenv('DEVELOPMENT_CONF')
elif os.getenv('CONFIG_NAME') == 'heroku':
	config_name = os.getenv('PRODUCTION_CONF')
else:
    config_name = os.getenv('DEPLOYMENT_CONF')

app.config.from_object(config_app[config_name])
print(app.config['DATABASE'])


