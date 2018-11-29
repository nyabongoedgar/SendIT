from flask import Flask, Blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*":{"origins":"*"}})



from application.api.views.parcel_views import parcel
app.register_blueprint(api.views.parcel_views.parcel)

from application.api.views.user_views import user_blueprint
app.register_blueprint(api.views.user_views.user_blueprint)

app.config.from_object('config.BaseConfig')






