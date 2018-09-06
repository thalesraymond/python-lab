from api import app
from flask import Blueprint

home_blueprint = Blueprint('home_blueprint', __name__, template_folder='templates', url_prefix='/home')

@home_blueprint.route('/')
def get():
    return ":D"
