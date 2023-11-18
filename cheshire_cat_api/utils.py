from cheshire_cat_api.api_client import ApiClient
from cheshire_cat_api.api import (
    EmbedderApi, LargeLanguageModelApi, MemoryApi, PluginsApi,
    RabbitHoleApi, SettingsApi, StatusApi
)


class Settings:
    """
    Class containing all the configuration options and variables used by ccat-api package
    """

    def __init__(
            self,
            base_url='localhost',
            port=1865,
            user_id="user",
            auth_key='',
            secure_connection=False,
            timeout=10000,
            retries=3,
            delay=5000,
            on_failed=None
            ):

        self.base_url = base_url
        self.port = port
        self.user_id = user_id
        self.auth_key = auth_key
        self.secure_connection = secure_connection
        self.timeout = timeout
        self.retries = retries
        self.delay = delay
        self.on_failed = on_failed

    def get_websocket_url(self):
        protocol = "ws"
        if self.secure_connection:
            protocol = "wss"

        return f"{protocol}://{self.base_url}:{self.port}/{self.user_id}"
