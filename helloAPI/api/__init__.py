from flask import Flask

app = Flask(__name__)

from api import routes

if __name__ == "__main__":
    app.run()

@app.route('/')
def index():
    return 'Test'
