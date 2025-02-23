import os

from dotenv import load_dotenv


if load_dotenv():
    DS_USER_TOKEN = os.getenv("DS_USER_TOKEN")
    BOT_TOKEN = os.getenv("BOT_TOKEN")
