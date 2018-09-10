from flask import render_template
from api import app
from api.controllers import homeController

app.register_blueprint(homeController.home_blueprint)