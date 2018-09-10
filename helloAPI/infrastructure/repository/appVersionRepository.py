from typing import List

from infrastructure.repository import engineFactory


class AppVersionRepository:

    def __init__(self):
        self.engine = engineFactory.engine

    def get_app_versions(self) -> List[str]:
        connection = self.engine.connect()
        result = self.engine.execute('GetAppVersions')
        connection.close()
        app_versions: List[str] = []
        for row in result:
            app_versions.append(row['PlatformName'])

        return app_versions
