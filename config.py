from typing import Dict

from dotenv import dotenv_values


class Config:
    def __init__(self):
        config: Dict[str, str] = dotenv_values(".env")
        self.token: str = config["BOT_TOKEN"]
