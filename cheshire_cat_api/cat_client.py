import json
import time
from typing import Callable
from websocket import WebSocketApp
from threading import Thread
from cheshire_cat_api.api_client import ApiClient
from cheshire_cat_api.configuration import Configuration
from cheshire_cat_api.utils import Settings
from cheshire_cat_api.api import (
    EmbedderApi, LargeLanguageModelApi, MemoryApi, PluginsApi,
    RabbitHoleApi, SettingsApi, StatusApi
)


class CatClient:
    """
    The class to communicate with the Cheshire Cat AI
    """

    def __init__(self,
                 settings: Settings | None = None,
                 on_open: Callable | None = None,
                 on_close: Callable | None = None,
                 on_message: Callable | None = None,
                 on_error: Callable | None = None
                 ):
        # Instantiate user message handlers if any, otherwise use default
        self.on_message = on_message
        self.on_error = on_error
        self.on_close = on_close
        self.on_open = on_open

        # WebSocket settings
        self.settings = settings if settings is not None else Settings()

        # Connection status
        self.is_closed = False

        # Number of retries already done
        self.retried = 0

        self._connect_api()
        self._connect_ws()

        self.is_started = False

    def _connect_api(self):
        config = Configuration(host=f"http://{self.settings.base_url}")
        client = ApiClient(
            configuration=config,
            header_name='access_token',
            header_value=self.settings.auth_key
        )
        self.memory = MemoryApi(client)
        self.plugins = PluginsApi(client)
        self.rabbit_hole = RabbitHoleApi(client)
        self.status = StatusApi(client)
        self.embedder = EmbedderApi(client)
        self.general = SettingsApi(client)
        self.llm = LargeLanguageModelApi(client)

    def _connect_ws(self):
        # Closed by the user
        self.explicitly_closed = False

        url = self.settings.get_websocket_url()

        self._ws = WebSocketApp(
            url,
            on_message=self.on_ws_message,
            on_error=self.on_ws_error,
            on_close=self.on_ws_close,
            on_open=self.on_ws_open
        )

        self.conn = Thread(target=self._ws.run_forever)
        self.conn.start()

    def on_ws_open(self, ws):
        """"Default message handler on connection opening"""

        # Run user custom function
        if callable(self.on_open):
            self.on_open()
            return

        print("Connection established")

    def on_ws_message(self, ws, message: str):
        """"Default message handler when receiving a message"""
        # Run user custom function
        if callable(self.on_message):
            self.on_message(message)
            return

        answer = json.loads(message)
        print(answer["content"])

    def on_ws_error(self, ws, error: str):
        """"Default message handler on WebSocket error"""
        # Run user custom function
        if callable(self.on_error):
            self.on_error(error)
            return

        print(f"Encountered error: {error}")

    def on_ws_close(self, ws, close_status_code: int, msg: str):
        """"Default message handler on closed connection"""

        # Retry to connect if connection fails
        if self.explicitly_closed:
            return

        self.retried += 1
        if self.retried <= self.settings.retries:
            self._connect_ws()
            time.sleep(self.settings.delay / 1000)
        else:
            if self.settings.on_failed is not None:
                self.settings.on_failed()

        self.is_closed = True if close_status_code is not None else False

        # Run user custom function
        if callable(self.on_close):
            self.on_close(close_status_code, msg)
            return

        print(f"Connection closed: {msg}")

    def send(self, message: str, **kwargs):
        """Send a message to WebSocket server using a separate thread"""
        if not self.is_closed:
            self._ws.send(json.dumps({
                "text": message,
                **kwargs
            }))

    def close(self):
        # Close connection
        self.explicitly_closed = True
        self._ws.close()
