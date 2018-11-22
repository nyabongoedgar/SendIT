from flask import Flask, Blueprint
app = Flask(__name__)

from application.api.views import mod
app.register_blueprint(api.views.mod)

app.config.from_object('config.ProductionConfig')

# import config
# app.config.from_object(config.ProductionConfig)
# app.config[DEBUG_MODE]


