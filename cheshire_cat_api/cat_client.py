import json
import logging
from typing import Callable, Optional
from websocket import WebSocketApp
from threading import Thread
from cheshire_cat_api.api_client import ApiClient
from cheshire_cat_api.configuration import Configuration
from cheshire_cat_api.settings import Settings
from cheshire_cat_api.api import (
    EmbedderApi, LargeLanguageModelApi, MemoryApi, PluginsApi,
    RabbitHoleApi, SettingsApi, StatusApi
)


class CatClient:
    """
    The class to communicate with the Cheshire Cat AI
    """

    def __init__(self,
                 settings: Optional[Settings] = None,
                 on_open: Optional[Callable] = None,
                 on_close: Optional[Callable] = None,
                 on_message: Optional[Callable] = None,
                 on_error: Optional[Callable] = None
                 ):

        # Instantiate user message handlers if any, otherwise use default
        self.on_message = on_message
        self.on_error = on_error
        self.on_close = on_close
        self.on_open = on_open

        # Settings
        self.settings = settings if settings is not None else Settings()

        self._ws = None
        self.memory = None
        self.plugins = None
        self.rabbit_hole = None
        self.status = None
        self.embedder = None
        self.general = None
        self.llm = None

        self._connect_api()
        self._connect_ws()

        self.is_started = False

    def _connect_api(self):
        protocol = "https" if self.settings.secure_connection else "http"
        config = Configuration(host=f"{protocol}://{self.settings.base_url}")

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
        self.settings = SettingsApi(client)
        self.llm = LargeLanguageModelApi(client)

    def connect_ws(self):
        protocol = "wss" if self.settings.secure_connection else "ws"
        url = f"{protocol}://{self.settings.base_url}:{self.settings.port}/ws/{self.settings.user_id}"

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
        
        logging.info(f"Websocket connection established with id {self.settings.user_id}")

        # Run user custom function
        if callable(self.on_open):
            self.on_open()

    def on_ws_message(self, ws, message: str):
        """"Default message handler when receiving a message"""
        # Run user custom function
        if callable(self.on_message):
            self.on_message(message)
            return

        answer = json.loads(message)
        print(answer["content"])

    def on_ws_error(self, ws, error: Exception):
        """"Default message handler on WebSocket error"""

        logging.exception(f"An error occurred in ws connection with id {self.settings.user_id}: {error}", exc_info=True)

        # Run user custom function
        if callable(self.on_error):
            self.on_error(error)
        
    def on_ws_close(self, ws, status_code: int, msg: str):
        """"Default message handler on closed connection"""

        logging.info(f"Connection with id {self.settings.user_id} closed with code {status_code}: {msg}")

        # Run user custom function
        if callable(self.on_close):
            self.on_close(status_code, msg)

    def send(self, message: str, **kwargs):
        """Send a message to WebSocket server using a separate thread"""

        if self._ws is None:     
            logging.warning("WebSocket connection is not available. Message not sent.")
        else:
            self._ws.send(json.dumps({
                "text": message,
                **kwargs
            }))

    def close(self):
        # Close connection
        self._ws.close()
