from cheshire_cat_api.api_client import ApiClient
from cheshire_cat_api.api import (
    MemoryApi, PluginsApi, RabbitHoleApi, StatusApi,
    SettingsEmbedderApi, SettingsGeneralApi, SettingsLargeLanguageModelApi, SettingsPromptApi)


class CatAPI:
    """"The class to instantiate the Cat API endpoints"""

    def __init__(self, client: ApiClient):
        self.memory = MemoryApi(client)
        self.plugins = PluginsApi(client)
        self.rabbit_hole = RabbitHoleApi(client)
        self.status = StatusApi(client)
        self.embedder = SettingsEmbedderApi(client)
        self.general = SettingsGeneralApi(client)
        self.llm = SettingsLargeLanguageModelApi(client)
        self.prompt = SettingsPromptApi(client)


class WebSocketSettings:
    """
    Class containing the WebSocket configuration options and variables used by ccat-api package
    """

    def __init__(self):
        # Websocket path to use to communicate with the CCat
        self.path = 'ws'
        # The maximum number of retries before calling on_failed
        self.retries = 3
        # The delay for reconnect, in milliseconds
        self.delay = 5000
        # The function to call after failing to reconnect
        self.on_failed = None


class Settings:
    """
    Class containing all the configuration options and variables used by ccat-api package
    """

    def __init__(self):
        # The URL to which connect to the Cat
        self.base_url = 'localhost'
        # The key to authenticate the Cat endpoints
        self.auth_key = ''
        # The port to which connect to the Cat
        self.port = 1865
        # Choose to either use the secure protocol or not
        self.secure = False
        # Timeout for the endpoints, in milliseconds
        self.timeout = 10000
        # Choose to either instantly initialize websocket and api client or not
        self.instant = True
        # WebSocket Settings
        self.ws = WebSocketSettings()
