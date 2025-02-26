import os
import logging

from dotenv import load_dotenv


if load_dotenv():
    DS_USER_TOKEN = os.getenv("DS_USER_TOKEN")
    BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(filename="bot.log", level="DEBUG")
logger = logging.Logger("BOT")
