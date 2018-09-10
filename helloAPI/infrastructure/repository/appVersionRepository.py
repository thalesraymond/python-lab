from typing import List
from dateutil import parser

from domain.appVersion import AppVersion
from infrastructure.repository import engineFactory


class AppVersionRepository:

    def __init__(self):
        self.engine = engineFactory.engine

    def get_app_versions(self) -> List[AppVersion]:
        connection = self.engine.connect()
        result = self.engine.execute('GetAppVersions')
        connection.close()

        return [AppVersion(row['PlatformId'], row['Version'], bool(row['EnableVideoChat']), parser.parse(row['LastUpdate']), row['UpdatedBy']) for row in result]
