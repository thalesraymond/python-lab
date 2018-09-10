from flask import Blueprint
from flask import jsonify

from api.models.appVersionModel import AppVersionModel
from infrastructure.repository.appVersionRepository import AppVersionRepository

home_blueprint = Blueprint('home_blueprint', __name__, template_folder='templates', url_prefix='/home')


@home_blueprint.route('/')
def get():
    repository = AppVersionRepository()
    app_versions = repository.get_app_versions()
    return jsonify([AppVersionModel(domain).serialize() for domain in app_versions])
