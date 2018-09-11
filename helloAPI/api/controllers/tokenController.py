from flask import Blueprint


token_blueprint = Blueprint('token_blueprint', __name__, template_folder='views', url_prefix='/token')


@token_blueprint.route('/', methods=['POST'])
def authenticate():
    pass
