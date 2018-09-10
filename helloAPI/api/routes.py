from api import app
from api.controllers import appVersionController

app.register_blueprint(appVersionController.app_version_blueprint)
