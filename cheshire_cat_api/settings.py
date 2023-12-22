from dataclasses import dataclass

@dataclass
class Settings:
    """
    Class containing all the configuration options and variables used by ccat-api package
    """  
    base_url: str = 'localhost'
    port: int = 1865
    user_id: str = "user"
    auth_key: str = ''
    secure_connection: bool = False
