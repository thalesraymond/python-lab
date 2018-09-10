from domain.mobilePlatform import MobilePlatform
from datetime import datetime


class AppVersion:
    platform: MobilePlatform
    version: str
    enableVideoChat: bool
    lastUpdate: datetime
    updatedBy: str

    def __init__(self, platform: MobilePlatform, version: str, enable_video_chat: bool, last_update: datetime, updated_by: str):
        self.platform = MobilePlatform.ANDROID if platform == '1' else MobilePlatform.IOS
        self.version = version
        self.enableVideoChat = enable_video_chat
        self.lastUpdate = last_update
        self.updatedBy = updated_by
