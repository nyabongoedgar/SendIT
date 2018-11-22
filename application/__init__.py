from flask import Flask, Blueprint
app = Flask(__name__)

<<<<<<< HEAD
from application.api.routes import mod

app.register_blueprint(api.routes.mod)
=======
from application.api.views.parcel_views import parcel
app.register_blueprint(api.views.parcel_views.parcel)

from application.api.views.user_views import user_blueprint
app.register_blueprint(api.views.user_views.user_blueprint)

app.config.from_object('config.BaseConfig')
>>>>>>> feedback-two




