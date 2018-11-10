from flask import Flask, Blueprint
app = Flask(__name__)

from application.api.routes import mod

app.register_blueprint(api.routes.mod)




