from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from api.models.appVersionModel import AppVersionModel
from domain.mobilePlatform import MobilePlatform
from infrastructure.repository.appVersionRepository import AppVersionRepository

app_version_blueprint = Blueprint('app_version_blueprint', __name__, template_folder='views', url_prefix='/app-version')


@app_version_blueprint.route('/', methods=['GET'])
@jwt_required
def list_app_versions():
    repository = AppVersionRepository()

    app_versions = repository.get_app_versions()

    return jsonify([AppVersionModel(domain).serialize() for domain in app_versions])


@app_version_blueprint.route('/<platform_name>', methods=['GET'])
@jwt_required
def get_app_version(platform_name):
    repository = AppVersionRepository()

    if platform_name.lower() == 'android':
        platform_filter = MobilePlatform.ANDROID
    elif platform_name.lower() == 'ios':
        platform_filter = MobilePlatform.IOS
    else:
        return jsonify({'message': 'Invalid platform name'}), 400

    app_versions = repository.get_app_versions()

    selected_version = next((AppVersionModel(domain) for domain in app_versions if domain.platform == platform_filter), None)

    return jsonify(selected_version.serialize())
