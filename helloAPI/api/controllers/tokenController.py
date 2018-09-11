from flask import Blueprint, request, jsonify
from api.authorizationProvider import AuthorizationProvider
from domain.user import User

token_blueprint = Blueprint('token_blueprint', __name__, template_folder='views', url_prefix='/token')


@token_blueprint.route('/login', methods=['POST'])
def authenticate():
    if not request.is_json:
        return '', 401

    model = request.get_json()

    user = User(None, model['username'], model['password'])

    if user.authenticate():
        return jsonify({'token': str(AuthorizationProvider.encode_auth_token(user.userId))})
