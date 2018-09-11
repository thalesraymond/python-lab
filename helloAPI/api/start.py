from flask import Flask
from flask_jwt_extended import JWTManager

from api.controllers import appVersionController, tokenController

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret'  # Not so secret
jwt = JWTManager(app)

if __name__ == '__main__':
    app.run()

app.register_blueprint(appVersionController.app_version_blueprint)
app.register_blueprint(tokenController.token_blueprint)


@app.route('/')
def index():
    return 'Root'
