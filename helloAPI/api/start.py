from flask import Flask

from api.controllers import appVersionController, tokenController

app = Flask(__name__)

if __name__ == '__main__':
    app.run()


app.register_blueprint(appVersionController.app_version_blueprint)
app.register_blueprint(tokenController.token_blueprint)


@app.route('/')
def index():
    return 'Root'
