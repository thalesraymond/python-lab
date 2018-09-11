from flask_jwt_extended import create_access_token

from flask import current_app as app


class AuthorizationProvider:
    @staticmethod
    def encode_auth_token(user_id):
        return create_access_token(identity=user_id)
