from api import app
from flask import Blueprint
from flask import jsonify

home_blueprint = Blueprint('home_blueprint', __name__, template_folder='templates', url_prefix='/home')

@home_blueprint.route('/')
def get():
    return jsonify([1,2,3,4,5,6,7,8,9,10])
