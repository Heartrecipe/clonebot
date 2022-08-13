#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5412740624:AAHa9qqN9cx_yzRrhb1L5ELawXgqALKsEOM")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "19302982"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "6b23af62bed230868f6d2b7d69aa27d7")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5338017254").split())

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://frdbot:frdbot@cluster0.t9ma9wq.mongodb.net/?retryWrites=true&w=majority")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
