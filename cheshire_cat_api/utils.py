from cheshire_cat_api.api_client import ApiClient
from cheshire_cat_api.api import (
    EmbedderApi, LargeLanguageModelApi, MemoryApi, PluginsApi,
    PromptApi, RabbitHoleApi, SettingsApi, StatusApi
)


class CatAPI:
    """"The class to instantiate the Cat API endpoints"""

    def __init__(self, client: ApiClient):
        self.memory = MemoryApi(client)
        self.plugins = PluginsApi(client)
        self.rabbit_hole = RabbitHoleApi(client)
        self.status = StatusApi(client)
        self.embedder = EmbedderApi(client)
        self.general = SettingsApi(client)
        self.llm = LargeLanguageModelApi(client)
        self.prompt = PromptApi(client)


class WebSocketSettings:
    """
    Class containing the WebSocket configuration options and variables used by ccat-api package
    """

    def __init__(self, path='ws', retries=3, delay=5000, on_failed=None, user_id=None):
        # Websocket path to use to communicate with the CCat
        self.path = path
        # The maximum number of retries before calling on_failed
        self.retries = retries
        # The delay for reconnect, in milliseconds
        self.delay = delay
        # The function to call after failing to reconnect
        self.on_failed = on_failed
        # User to connect with
        self.user_id = user_id


class Settings:
    """
    Class containing all the configuration options and variables used by ccat-api package
    """

    def __init__(self,
                 base_url='localhost',
                 auth_key='',
                 port=1865,
                 secure=False,
                 timeout=10000,
                 instant=True,
                 ws=WebSocketSettings(),
                 ):
        # The URL to which connect to the Cat
        self.base_url = base_url
        # The key to authenticate the Cat endpoints
        self.auth_key = auth_key
        # The port to which connect to the Cat
        self.port = port
        # Choose to either use the secure protocol or not
        self.secure = secure
        # Timeout for the endpoints, in milliseconds
        self.timeout = timeout
        # Choose to either instantly initialize websocket and api client or not
        self.instant = instant
        # WebSocket Settings
        self.ws = ws
