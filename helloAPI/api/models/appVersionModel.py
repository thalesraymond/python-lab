from domain.appVersion import AppVersion
from domain.mobilePlatform import MobilePlatform


class AppVersionModel:
    platform: int
    platformName: str
    version: str
    enableVideoChat: bool
    lastUpdate: str
    updatedBy: str

    def __init__(self, domain: AppVersion):
        if domain is None:
            return

        self.platform = int(domain.platform)
        self.platformName = 'Android' if domain.platform == MobilePlatform.ANDROID else 'iOS'
        self.version = domain.version
        self.enableVideoChat = domain.enableVideoChat
        self.lastUpdate = domain.lastUpdate.strftime('%d/%m/%Y')
        self.updatedBy = domain.updatedBy

    def serialize(self):
        return {
            'platform': self.platform,
            'platformName': self.platformName,
            'version': self.version,
            'enableVideoChat': self.enableVideoChat,
            'lastUpdate': self.lastUpdate,
            'updatedBy': self.updatedBy,
        }
