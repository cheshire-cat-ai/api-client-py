import json
import time
from typing import Dict, Callable
from websocket import WebSocketApp
from threading import Thread
from cheshire_cat_api.api_client import ApiClient
from cheshire_cat_api.configuration import Configuration
from cheshire_cat_api.utils import Settings, CatAPI


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
        self.is_started = False
        # Closed by the user
        self.explicitly_closed = False
        # Number of retries already done
        self.retried = 0
        # Start instantly
        if self.settings.instant:
            self.run()

    @property
    def url(self):
        """"Compose the WebSocket and API address"""
        secure = 's://' if self.settings.secure else '://'
        port = f":{self.settings.port}" if self.settings.port else ''
        return f"{secure}{self.settings.base_url}{port}"

    def _connect(self):
        """"Connect to the WebSocket in a separate thread"""
        self._ws = WebSocketApp(
            f"ws{self.url}/{self.settings.ws.path}",
            on_message=self.on_ws_message,
            on_error=self.on_ws_error,
            on_close=self.on_ws_close,
            on_open=self.on_ws_open
        )

        self.conn = Thread(target=self._ws.run_forever)
        self.conn.start()

    def run(self):
        """"Instantiate the WebSocket and Cat API client with configuration"""
        if self.is_started:
            raise Exception("The Cheshire Cat Client was already initialized")
        else:
            self._connect()
            config = Configuration()
            config.host = f'http{self.url}'
            self.api = CatAPI(ApiClient(
                configuration=config,
                header_name='access_token',
                header_value=self.settings.auth_key
            ))
            self.is_started = True

    def on_ws_open(self, ws):
        """"Default message handler on conneciton opening"""

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
        if not self.explicitly_closed:
            self.retried += 1
            if self.settings.ws.retries < 0 or self.retried < self.settings.ws.retries:
                self._connect()
                time.sleep(self.settings.ws.delay / 1000)
            else:
                self.settings.ws.on_failed()
            return

        self.is_closed = True if close_status_code is not None else False

        # Run user custom function
        if callable(self.on_close):
            self.on_close(close_status_code, msg)
            return

        print(f"Connection closed: {msg}")

    def send(self, message: str, prompt_settings: Dict = {}):
        """Send a message to WebSocket server using a separate thread"""
        if not self.is_closed:
            self._ws.send(json.dumps({
                "text": message,
                "prompt_settings": prompt_settings
            }))

    def close(self):
        # Close connection
        self.explicitly_closed = True
        self._ws.close()
