from flask import Blueprint
from flask import jsonify
from flask import Response

from api.models.appVersionModel import AppVersionModel
from domain.mobilePlatform import MobilePlatform
from infrastructure.repository.appVersionRepository import AppVersionRepository

app_version_blueprint = Blueprint('app_version_blueprint', __name__, template_folder='templates', url_prefix='/app-version')


@app_version_blueprint.route('/', methods=['GET'])
def get():
    repository = AppVersionRepository()

    app_versions = repository.get_app_versions()

    return jsonify([AppVersionModel(domain).serialize() for domain in app_versions])


@app_version_blueprint.route('/<platform_name>', methods=['GET'])
def post(platform_name):
    repository = AppVersionRepository()

    platform_filter = MobilePlatform.ANDROID if platform_name.lower() == 'android' else MobilePlatform.IOS

    app_versions = repository.get_app_versions()

    selected_version = next((AppVersionModel(domain) for domain in app_versions if domain.platform == platform_filter), None)

    if selected_version is None:
        return Response('Invalid platform name', status=400)

    return jsonify(selected_version.serialize())
